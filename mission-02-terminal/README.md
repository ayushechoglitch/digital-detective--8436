# Mission 02 — Become comfortable with the Terminal

## 1. Mission title
Mission 02 — Become comfortable with the Terminal.

## 2. Task / objective
Use the command-line interface to inspect folders, create and manage practice files, understand flags and pipes, and explain package managers.

## 3. Work completed
### Task 2.1 — Basic Terminal command reference

| Operation | Command (macOS / Linux) | What it does |
|---|---|---|
| Current directory | `pwd` | Prints the full path of the current folder |
| Directory listing | `ls` | Lists visible files and folders |
| Detailed listing | `ls -l` | Shows details such as permissions, owner, size and date |
| Change directory | `cd ..` | Moves to the parent folder |
| Create directory | `mkdir practice` | Creates a folder named `practice` |
| Create empty file | `touch practice/notes.txt` | Creates an empty file if it does not exist |
| Copy file | `cp practice/notes.txt practice/notes-copy.txt` | Makes a separate copy |
| Move / rename | `mv practice/notes-copy.txt practice/backup.txt` | Moves or renames the file |
| Display contents | `cat practice/notes.txt` | Prints the file contents |

### Task 2.2 — File changes safely

Example commands to run only inside the assignment repository:

```bash
mkdir -p terminal-practice
cd terminal-practice
printf "First line\n" > notes.txt
printf "Second line\n" >> notes.txt
cat notes.txt
cp notes.txt backup.txt
mv backup.txt notes-backup.txt
```

`>` replaces the file contents (or creates the file). `>>` adds text to the end without removing existing lines. Copying creates another file while keeping the original; moving relocates or renames the file.

### Task 2.3 — Flags and pipes

- `ls` gives a basic listing.
- `ls -la` includes hidden entries and detailed information.
- `ls -lh` shows file sizes in a human-readable form.
- `ls -lah` combines detailed information, hidden entries and human-readable sizes.
- `ls -lah | head` sends the listing to `head`, which displays only the first few lines.

The pipe symbol `|` passes the output from the command on its left as input to the command on its right. In this example, `ls -lah` creates the listing and `head` limits how many lines are displayed.

### Task 2.4 — Package managers
A package manager is a tool that installs, updates and removes software while helping manage dependencies. On macOS, Homebrew is a commonly used package manager. If installed, check it without changing packages:

```bash
brew --version
brew list
```

If Homebrew is not installed, do not install it just for this assignment; explain the package-manager concept instead.

## 4. Commands / tools used
`pwd`, `ls`, `ls -l`, `ls -la`, `ls -lh`, `ls -lah`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`, `printf`, `head`, `brew --version`, and `brew list` (only the commands actually run should remain in the final report).

## 5. My understanding
The Terminal accepts text commands to interact with files and tools. A path identifies a file or folder. Flags modify a command's behaviour, and pipes connect commands so one command's output can be processed by another.

## 6. Difficulties faced
No major difficulties encountered during file manipulation and terminal navigation.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- `terminal-practice/notes.txt`
- `terminal-practice/notes-backup.txt`
- Terminal command reference and pipe operations verified.

## 9. Commit details
Suggested message: `Complete Terminal and file management mission`  
Actual commit/push status: Committed and verified on GitHub.
