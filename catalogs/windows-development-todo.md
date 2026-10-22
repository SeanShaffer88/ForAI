# Windows development revival to-do list

Created 2026-10-21 at Sean's request. Status: nine open tasks and one completed; WR-007 shipped stable 0.2.0 with GitHub CI and publication; WR-001 is now in progress; the remaining tasks are queued or conditional. This is the shared local backlog for evaluating and carrying out useful Windows development revivals. It complements the 232-repository Windows development reference.

Priority expresses expected reuse and a bounded path to value, not a measured return on investment. These judgments are provisional because no specific consuming application has been selected. Every task starts by checking maintained forks and reproducing the baseline. If a maintained successor already meets the need, use it and close or redirect the task instead of duplicating its work.

Research: two Exa searches requested 20 results including duplicates; selected repository READMEs were retrieved. GitHub API archive flags and last-push dates were checked on 2026-10-21. An old last-push date alone does not prove abandonment. At initial backlog creation no source had been cloned or built; development subsequently started for WR-007 as recorded below.

## Next up

- [ ] **WR-001 — P1 / IN PROGRESS — native foundation: Revive [Microsoft IPC](https://github.com/microsoft/IPC).**
  Independent fork: https://github.com/SeanShaffer88/ipc-revival ; review: https://github.com/SeanShaffer88/ipc-revival/pull/1 . Upstream MIT commit 86df124c5f2a0447d6ec56af7a506dc41bbf5546 is preserved. Development commit dad6f5f91f89b6191a90bcd17f1a18d60871fff7.
  Selection: checked 122 direct forks; newest-pushed fork compares identical to upstream and no active direct continuation was identified. Compared active Boost.Interprocess, iceoryx2 (Windows tier 2 / separate C# bindings) and named pipes. Scope: existing typed native transport and reusable immutable shared blobs for trusted local workers, with a measured pipe baseline. Modest initial timing differences do not establish a general advantage.
  Implemented: C++17 CMake MSVC x64 build, checksum-pinned Boost 1.92; allocator/type-trait/consume adaptations; queue exception cleanup; scheduler drain notification fix and C++17 TLS replacement; original C++ calculator builds; bounded checksum worker and Win32 pipe baseline.
  Validation: local MSVC x64 Debug/Release each pass core regressions (3,200 scheduler callbacks plus queue/mapping checks) and 16 process integration checks, including normal/crash endpoint reuse, producer/server termination, response timeout and payloads through 256 KiB. GitHub CI: Debug and Release passed on tested development commit — https://github.com/SeanShaffer88/ipc-revival/actions/runs/39707551092 .
  Remaining: full upstream native suite, allocation/handle failures and deeper ownership/concurrency review; modern .NET bridge and mixed-language samples; stronger crash/lock and permissions testing; representative benchmark distributions and stable packaging. Shared allocator locks are not robust against arbitrary owner death. Both peers require matching ABI/Boost/configuration; trusted-peer IPC only. Native development milestone, not a stable release; WR-001 stays open.
  Checkout: (local research archive) . Report/evidence: (local research archive) .
- [ ] **WR-002 — P1: Modernize a minimal [Tx](https://github.com/microsoft/Tx) ETW query pipeline.**  
  Benefit: reuse LINQ/Rx queries over stored or live Windows event streams for diagnostics. Evidence: not archived; GitHub reports last push 2022-10-05, so classify as dormant rather than confirmed abandoned. First identify any maintained forks, verify the actual license, and choose one useful ETL query and a reproducible trace fixture. Port only its required reader/operators to the selected supported .NET/Rx stack. Done when an offline trace produces expected event counts and fields, failures are reported clearly, and a CLI example runs without restoring the old UI ecosystem. If live consumption is required, add cancellation and session-lifetime tests as a separate milestone. Compare with the TraceEvent library in [PerfView](https://github.com/microsoft/perfview) before committing to a fork. Scope: small-to-medium for an offline subset; larger for a full port.

- [ ] **WR-003 — P2: Restore [Visual Leak Detector](https://github.com/KindDragon/vld) for one current native Windows toolchain.**  
  Benefit: source-level leak reports with call stacks and module filtering for C++ tools, including cases beyond basic CRT leak reporting. Evidence: README explicitly calls the project inactive and seeks maintainers; GitHub reports last push 2023-05-22. First compare recent forks with [heob](https://github.com/ssbssa/heob), Dr. Memory and the toolchain's available diagnostics. Select one supported MSVC/UCRT combination and x64 initially; repair the minimum build and symbol-resolution path. Done when known positive and negative leak fixtures produce correct results across EXE/DLL boundaries and common allocator paths, without regressions in clean shutdown. Preserve LGPL requirements. Add architectures only when a consuming project needs them. Close the revival if existing diagnostics cover the use case more reliably. Scope: medium-to-large because allocator interception and CRT behavior can change.

- [ ] **WR-004 — P2: Maintain a focused Windows fork of [Funchook](https://github.com/kubo/funchook) if its API or cross-platform support fills a real gap.**  
  Benefit: a small C-facing interception layer usable in our own diagnostic programs. Evidence: upstream is archived and README explicitly says it is unmaintained; GitHub reports last push 2025-09-28. First inspect the upstream fork network, full license text and transitive disassembler licenses; compare with [MinHook](https://github.com/TsudaKageyu/minhook), [Detours](https://github.com/microsoft/Detours) and PolyHook. For a justified fork, update one disassembler backend and restore MSVC x64 CMake builds; exercise install/remove cycles only against test functions we control. Done when tests verify relocated instructions, return values, repeated installation/removal, supported optimization settings and documented concurrency limits. Treat Windows ARM64 as a separate experiment rather than promising support inherited from an old release note. Scope: medium-to-large due to instruction relocation and execution-state correctness.

- [ ] **WR-005 — P2: Consolidate useful [CrashRpt2](https://github.com/CrashRpt/crashrpt2) fixes into a tested Windows crash-reporting component.**  
  Benefit: preserve useful Windows exception-handler behavior and report compatibility without rebuilding an entire crash-reporting service. Evidence: CrashRpt2 last push 2021-08-11; [CrashRpt3](https://github.com/crashrpt3/crashrpt3) is an existing community continuation, last push 2025-12-28. Start by comparing both lineages and maintained forks; prefer extending CrashRpt3 if appropriate instead of creating another competing fork. Review BSD license notices and test claims independently. Done when a minimal current-toolchain example produces valid symbolizable dumps for a documented matrix of access violations, unhandled C++ exceptions, stack overflow, worker-thread failures and fail-fast behavior, with unsupported cases explicitly recorded. Assess out-of-process capture, consent and data handling if uploading is ever added to a product. Compare with our existing Crashpad reference before selecting the component. Scope: medium-to-large; success means measured crash coverage, not a marketing comparison.

## Further revival candidates and development

- [x] **WR-007 — P1 / COMPLETE — 0.2.0 PUBLISHED: Stabilize [goodtrailer/win-pipe](https://github.com/goodtrailer/win-pipe).**
  Published revival: https://github.com/SeanShaffer88/win-pipe-revival/releases/tag/v0.2.0 at commit 2e9523e28dee527b03773327338ee2519c5c38c9. ISC license and upstream provenance preserved.
  Completed: MSVC discovery; bounded overlapped IPC, concurrent senders/reconnects, callback/lifetime handling; five deterministic resource-failure cases; real PipeLog JSONL consumer with correlated application acknowledgements; agent-performed review and fixes; packaging and publishing scripts.
  Validation: 24 transport cases across five local MSVC/Clang configurations, 336 passing executions, PipeLog/example integration in every configuration and packaged x86/x64 binaries; MSVC /analyze /W4 /WX; all four exact-release MSVC GitHub jobs passed: https://github.com/SeanShaffer88/win-pipe-revival/actions/runs/39704893002. All four uploaded asset SHA-256 digests verified.
  Compatibility: both peers must upgrade. No durable/exactly-once guarantee; blocked callbacks/disk operations can delay shutdown. Scope: local Windows desktop x86/x64; ARM64 and authenticated cross-account services require separate work. Review was agent-performed, not independent human audit.
  Work checkout: (local research archive) Report and artifacts: (local research archive)
- [ ] **WR-008 — P2 / candidate: Modernize [Krzmbrzl/NamedPipe](https://github.com/Krzmbrzl/NamedPipe) when portable pipe semantics are needed.**  
  Benefit: a small CMake-based Windows/POSIX abstraction with BSD-3-Clause licensing. Evidence: not archived; last push 2023-06-27, so dormant rather than confirmed abandoned. Start with Windows build and paired-process fixtures and compare current forks, reproc and WR-007; identify whether the API supplies a useful portable behavior beyond existing components. Scope a revival to connection/shutdown behavior and modern CMake packaging. Done when required platforms pass connection, disconnect, EOF and binary-payload fixtures and the sample/package can be consumed without modifying upstream sources. Defer if there is no cross-platform consumer or the existing package already meets the need.

- [ ] **WR-009 — P2 / candidate: Restore [protobuf-pbop-plugin](https://github.com/end2endzone/protobuf-pbop-plugin) as a focused Windows local-RPC generator.**  
  Benefit: generated protobuf client/server interfaces over named pipes, distinct from maintaining a raw transport. MIT license; GitHub reports not archived and last push 2020-07-25. Begin by checking forks and compatibility with the selected current protoc/C++ runtime, then build one unary service and compare alternatives. Its README's historical Windows socket/performance claims are not assumed valid; benchmark modern transports on the actual workload. Done when code generation is reproducible, errors/disconnects propagate, malformed and oversized input is bounded, and a paired-process service sample passes repeated requests and shutdown. Keep streaming and async RPC outside the first milestone; the README says they are unsupported.

- [ ] **WR-010 — P3 / conditional: Revive a narrow [Mhook](https://github.com/martona/mhook) diagnostic use case.**  
  Benefit: preserve an existing small Windows interception API when that specifically reduces integration work. Not archived; GitHub reports last push 2021-04-28. Before coding, inspect full license and transitive decoder source, check forks, and compare Detours/MinHook/Funchook against a concrete API gap. Done only when that gap is demonstrated and a minimum x64 build passes controlled function relocation/install/remove tests; document concurrency and optimization limits. Prefer an existing maintained implementation when it satisfies the consumer. This is a conditional feasibility task, not a commitment to duplicate every hooking library.



## Conditional backlog

- [ ] **WR-006 — P3 / requires a consuming application: Apply a narrow [SharpDX](https://github.com/sharpdx/SharpDX) compatibility revival.**  
  Benefit: keep an existing SharpDX-dependent application working when a full graphics migration costs more than a limited fix. Evidence: archived; README says development and maintenance ended in 2019. First identify the actual application's required assemblies and failure, then compare migration to [Vortice.Windows](https://github.com/amerkoleci/Vortice.Windows). If a fork is justified, retain only the required bindings and repair the reproducible failure with MIT attribution. Done when the application's representative rendering/audio/input scenario works on its required Windows versions and architectures, COM ownership is tested, and the patch scope and maintenance owner are documented. Do not start a general DirectX binding rewrite without an application need. Scope: depends on the specific defect.

## Selection decisions

- [TestStack.White](https://github.com/TestStack/White): not queued. Its README recommends [FlaUI](https://github.com/FlaUI/FlaUI), explaining that the old architecture prevented desired UIA3 support. Prefer improving an adapter or migrating existing tests.
- [Snoop](https://github.com/snoopwpf/snoopwpf): not a revival candidate; the current upstream describes active maintenance. Consider it as an existing tool.
- Microsoft PDB, Bond and C++ REST SDK remain in the reference. Do not queue broad revivals without a demonstrated format/protocol/API compatibility need.
- ChakraCore remains a possible specialized runtime, but a general engine revival has a substantially larger maintenance and security burden than these bounded tasks.
- [Deviare2](https://github.com/nektra/Deviare2) was reviewed but not queued: broad COM/PDB-aware interception and license/dependency obligations need a specific consumer to justify maintaining it over existing instrumentation tools.

## How to maintain this backlog

Keep task IDs stable. Record the selected upstream/fork commit, consumer, concrete defect, validation and disposition as work starts. A task can finish by adopting an existing maintained solution when the evidence favors it; record why. Update this file and its persistent reference copy together.

Persistent copy: (local research archive)
Repository catalog: (local research archive)


## Repository and publishing preference

Sean authorized creating project repositories whenever appropriate and publishing finished products as they are completed. Preserve upstream provenance and licenses, validate release criteria and publish scoped finished products when the available account/tooling permits. Mark prototypes and milestones honestly. This preference does not mean a remote repository or release already exists.
