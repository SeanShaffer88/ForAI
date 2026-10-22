"""Read-only APK/XAPK/APKS inventory. Standard library; never extracts or executes input."""
import argparse,hashlib,json,struct,zipfile
from pathlib import Path

def sha256(path):
 h=hashlib.sha256()
 with path.open('rb') as f:
  for b in iter(lambda:f.read(1024*1024),b''):h.update(b)
 return h.hexdigest()

def elf_info(prefix):
 if prefix[:4]!=b'\x7fELF':return None
 bits=prefix[4];endian='<' if prefix[5]==1 else '>'
 if bits not in (1,2):return {'error':'unsupported ELF class'}
 machine=struct.unpack_from(endian+'H',prefix,18)[0]
 if bits==2:
  phoff=struct.unpack_from(endian+'Q',prefix,32)[0];phsize,phnum=struct.unpack_from(endian+'HH',prefix,54)
 else:
  phoff=struct.unpack_from(endian+'I',prefix,28)[0];phsize,phnum=struct.unpack_from(endian+'HH',prefix,42)
 loads=[]
 for i in range(phnum):
  off=phoff+i*phsize
  if off+phsize>len(prefix):return {'bits':32 if bits==1 else 64,'machine':machine,'error':'program headers exceed inspected prefix'}
  if bits==2:
   typ,flags,fileoff,va,pa,filesz,memsz,align=struct.unpack_from(endian+'IIQQQQQQ',prefix,off)
  else:
   typ,fileoff,va,pa,filesz,memsz,flags,align=struct.unpack_from(endian+'IIIIIIII',prefix,off)
  if typ==1:loads.append({'file_offset':fileoff,'virtual_address':va,'file_size':filesz,'memory_size':memsz,'alignment':align,'aligned_for_16k':align>=16384 and (va-fileoff)%16384==0})
 return {'bits':32 if bits==1 else 64,'machine':machine,'load_segments':loads,'all_loads_16k_compatible':bool(loads) and all(s['aligned_for_16k'] for s in loads)}

def inventory(path):
 result={'name':path.name,'bytes':path.stat().st_size,'sha256':sha256(path),'read_only':True}
 with zipfile.ZipFile(path) as z,path.open('rb') as raw:
  # Preserve raw ZIP names; Python normalizes backslashes in filename on Windows.
  infos=z.infolist();names=[i.orig_filename for i in infos]
  unsafe=[n for n in names if n.startswith(('/', '\\')) or '..' in n.replace('\\','/').split('/') or ':' in n.split('/')[0]]
  nested=[n for n in names if n.lower().endswith('.apk')]
  native=[]
  for i in infos:
   if not(i.orig_filename.startswith('lib/') and i.orig_filename.endswith('.so')):continue
   raw.seek(i.header_offset);header=raw.read(30)
   nlen,xlen=struct.unpack_from('<HH',header,26);start=i.header_offset+30+nlen+xlen
   with z.open(i) as f:prefix=f.read(min(i.file_size,1024*1024))
   native.append({'path':i.orig_filename,'bytes':i.file_size,'zip_method':i.compress_type,'stored':i.compress_type==0,'zip_data_offset':start,'stored_data_16k_aligned':i.compress_type==0 and start%16384==0,'elf':elf_info(prefix)})
  engine=[]
  if any('libunity.so' in n or 'global-metadata.dat' in n for n in names):engine.append('Unity IL2CPP' if any('global-metadata.dat' in n for n in names) else 'Unity; inspect scripting backend')
  if any('libflutter.so' in n or n.startswith('assets/flutter_assets/') for n in names):engine.append('Flutter')
  if any('libgodot' in n for n in names):engine.append('Godot')
  if any('libhermes.so' in n or n.endswith('index.android.bundle') for n in names):engine.append('React Native / Hermes candidate')
  result.update({'zip_entries':len(infos),'uncompressed_bytes':sum(i.file_size for i in infos),'duplicate_names':sorted(n for n in set(names) if names.count(n)>1),'unsafe_archive_paths':unsafe,'nonportable_archive_paths':[n for n in names if '\\' in n],'has_binary_android_manifest':'AndroidManifest.xml' in names,'dex_files':[n for n in names if '/' not in n and n.endswith('.dex')],'nested_apks':nested,'obb_files':[n for n in names if n.lower().endswith('.obb')],'abis':sorted({n.split('/')[1] for n in names if n.startswith('lib/') and len(n.split('/'))>2}),'native_libraries':native,'engine_candidates':engine,'largest_entries':[{'path':i.orig_filename,'bytes':i.file_size} for i in sorted(infos,key=lambda x:x.file_size,reverse=True)[:12]],'notes':['No signature verification or binary-manifest decoding performed. Use apksigner and apkanalyzer/aapt2.','ZIP alignment and ELF segment alignment are separate requirements; neither is a runtime compatibility guarantee.','Nested APKs are listed, not recursively executed or extracted.','SHA-256 records identity, not trust or provenance.']})
  if 'manifest.json' in names:
   i=z.getinfo('manifest.json')
   if i.file_size<=1024*1024:
    try:
     d=json.loads(z.read(i));result['container_manifest_fields']=sorted(d) if isinstance(d,dict) else ['non-object JSON']
    except (UnicodeError,ValueError):result['container_manifest_error']='not valid UTF-8 JSON'
 return result

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
 result=inventory(a.input);text=json.dumps(result,indent=2)
 if a.output:a.output.write_text(text+'\n',encoding='utf8')
 else:print(text)
if __name__=='__main__':main()
