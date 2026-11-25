# Mission 04 — How programs run

## 1. Mission title
Mission 04 — How programs run.

## 2. Task / objective
Run a simple Python program and compare compilers with interpreters.

## 3. Work completed
Create `hello.py` in this folder with:

```python
print("Hello from Python")
```

Run it from the repository root using:

```bash
python3 mission-04-programs/hello.py
```

Expected output:

```text
Hello from Python
```

### Task 4.2 — Compiler and interpreter comparison

| Point | Compiler | Interpreter |
|---|---|---|
| When translation / execution happens | Translates source code before the resulting program is run. | Executes instructions at runtime, often as it processes the program. |
| Typical output | Often produces a separate executable or object code. | Often produces program behaviour directly without a separate native executable. |
| One example | A C compiler such as GCC | A Python interpreter |
| One advantage | Compiled programs can run efficiently after compilation. | Convenient for testing and interactive execution. |

A compiler generally translates a program before it is executed, often producing machine code or another target form. An interpreter carries out program instructions at runtime. This makes interpreted workflows convenient for testing and learning. Real language implementations can combine compilation and interpretation techniques.

## 4. Commands / tools used
- Text editor / VS Code — creates `hello.py`.
- `python3` — runs the Python program from Terminal.

## 5. My understanding
A Python source file contains instructions. Running it with Python 3 starts the Python implementation, which processes the code and produces the printed output. Compiler and interpreter describe ways language implementations translate or execute programs; some modern implementations combine both approaches.

## 6. Difficulties faced
No major difficulties encountered executing Python scripts.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `hello.py`
- Terminal output showing `Hello from Python`

## 9. Commit details
Suggested message: `Compare compilers and interpreters`  
Actual commit/push status: Committed and verified on GitHub.
