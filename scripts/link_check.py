"""Check catalog URLs for reachability and redirects (stdlib only).

Reads resources.json and reports each URL as one of:
  ok       final response 2xx/3xx at the recorded URL
  moved    redirects to a different URL (target recorded)
  dead     404 or 410
  blocked  401 or 403 (checker-limited; the page may be fine for humans)
  error    any other status, timeout, or network failure

A successful check proves reachability only, never suitability.

Usage:
  python scripts/link_check.py [--only-unchecked] [--limit N]
                               [--report link-check-report.md]
                               [--json-out link-check-results.json]

Exit code is 1 when any URL is dead or moved, otherwise 0.
"""
import argparse
import json
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
UNCHECKED = {"", "not separately checked", "not independently measured",
             "not separately probed"}
UA = {"User-Agent": "ForAI-link-check/1.0 (+https://github.com/SeanShaffer88/ForAI)"}
CTX = ssl.create_default_context()


def check(row):
    url = row["url"]
    req = urllib.request.Request(url, headers=UA, method="GET")
    try:
        with urllib.request.urlopen(req, timeout=15, context=CTX) as resp:
            status, final = resp.status, resp.geturl()
    except urllib.error.HTTPError as e:
        status, final = e.code, e.geturl() or url
    except Exception as e:  # timeout, DNS, TLS, redirect loops
        return {**_base(row), "class": "error", "status": "",
                "final_url": "", "detail": type(e).__name__}
    if final.rstrip("/") != url.rstrip("/"):
        cls = "moved"
    elif status in (404, 410):
        cls = "dead"
    elif status in (401, 403):
        cls = "blocked"
    elif 200 <= status < 400:
        cls = "ok"
    else:
        cls = "error"
    return {**_base(row), "class": cls, "status": str(status),
            "final_url": final, "detail": ""}


def _base(row):
    return {"resource_id": row["resource_id"], "name": row["name"],
            "url": row["url"], "category": row["category"]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only-unchecked", action="store_true",
                    help="check only records with no recorded HTTP status")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--report", default="")
    ap.add_argument("--json-out", default="")
    args = ap.parse_args()

    rows = json.loads((ROOT / "resources.json").read_text(encoding="utf-8"))
    if args.only_unchecked:
        rows = [r for r in rows if str(r["http_status"]) in UNCHECKED]
    if args.limit:
        rows = rows[:args.limit]
    print(f"Checking {len(rows)} URLs...", file=sys.stderr)
    with ThreadPoolExecutor(max_workers=16) as pool:
        results = list(pool.map(check, rows))

    counts = {}
    for r in results:
        counts[r["class"]] = counts.get(r["class"], 0) + 1
    print(" ".join(f"{k}={counts.get(k, 0)}"
                   for k in ("ok", "moved", "dead", "blocked", "error")))

    if args.json_out:
        Path(args.json_out).write_text(
            json.dumps(results, indent=1) + "\n", encoding="utf-8")
    if args.report:
        lines = ["# Link check report", "",
                 "Reachability only — a live link is not an endorsement, "
                 "and a 401/403 usually means the checker was refused, "
                 "not that the page is gone.", ""]
        for cls in ("dead", "moved", "error", "blocked"):
            bad = [r for r in results if r["class"] == cls]
            if not bad:
                continue
            lines += [f"## {cls} ({len(bad)})", ""]
            for r in bad:
                extra = f" -> {r['final_url']}" if r["final_url"] else ""
                extra += f" ({r['detail']})" if r["detail"] else ""
                lines.append(f"- [{r['name']}]({r['url']}) — "
                             f"{r['category']} — status {r['status'] or 'n/a'}{extra}")
            lines.append("")
        lines.append(f"OK: {counts.get('ok', 0)} of {len(results)} checked.")
        Path(args.report).write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 1 if counts.get("dead") or counts.get("moved") else 0


if __name__ == "__main__":
    sys.exit(main())
