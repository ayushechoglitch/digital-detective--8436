# Mission 04 — How Programs Run: Compilers vs. Interpreters

## 1. Mission Title & Objectives
**Title:** Program Execution Paradigms: Compilers vs Interpreters  
**Objective:** Write and execute a Python program, evaluate the architectural differences between compiled and interpreted execution models, and examine hybrid translation approaches.

## 2. Work Completed
### Task 4.1 — Program Execution
I authored [`hello.py`](hello.py) containing a single clean print statement:

```python
print("Hello from Python")
```

I executed the script directly from the repository root:

```bash
python3 mission-04-programs/hello.py
```

**Observed Terminal Output:**
```text
Hello from Python
```

---

### Task 4.2 — Compilers vs Interpreters: Detailed Comparison

| Attribute | Compiler (e.g. GCC, Clang, Rustc) | Interpreter (e.g. CPython, Node.js, Ruby) |
|---|---|---|
| **Translation Timing** | Ahead-of-Time (AOT): Translates entire source code into machine code prior to execution. | Just-in-Time / At Runtime: Interprets and executes instructions line by line or block by block. |
| **Output Produced** | Standalone native machine code binary (ELF on Linux, Mach-O on macOS, PE on Windows). | Executes directly in memory; typically produces no independent standalone native binary. |
| **Execution Performance** | Highly optimized: Runs directly on bare-metal CPU hardware with minimal runtime overhead. | Slower: Each operation passes through the interpreter's virtual evaluation loop. |
| **Debugging & Feedback** | Requires full rebuild/relink on changes; errors caught at compile time before execution. | Rapid feedback loop: Easy to test snippets interactively in a REPL; errors surface at runtime. |
| **Platform Portability** | Compiled binary is architecture-specific (e.g. x86_64 vs arm64); must recompile for each OS. | Source code runs on any machine with a compatible interpreter installed. |

---

### Task 4.3 — Hybrid Models in Modern Computing
In practice, the boundary between pure compilers and pure interpreters is often blurred:
- **Python (CPython):** When a Python script runs, CPython first compiles the source text into intermediate **bytecode** (stored in `.pyc` files under `__pycache__/`). The CPython Virtual Machine then interprets this bytecode.
- **Java (JVM):** `javac` compiles Java source code into platform-independent `.class` bytecode. At runtime, the JVM uses a **Just-In-Time (JIT) compiler** to dynamically convert frequently executed bytecode ("hot spots") into native machine code on the fly.

Sanitized execution logs are available in [Run Output Evidence](evidence/run-output.md).

## 3. Personal Reflections
Learning about hybrid execution changed my perspective. I used to think of Python as simply "reading lines like text", but knowing that it compiles to bytecode first explains why `__pycache__` folders appear and how modern runtimes balance development speed with execution efficiency.

## 4. Practical Difficulties & Solutions
- **Challenge:** Understanding why Python doesn't produce a `.exe` or native app binary directly.
- **Resolution:** Realized that Python relies on the CPython runtime binary to evaluate bytecode, which trades native executable convenience for cross-platform portability.

## 5. Commit & Verification Status
- **Commits:**
  1. `Add hello.py program` (Program file creation)
  2. `Compare compilers and interpreters` (Report and evidence)
- **Status:** Verified and pushed to `main`.
