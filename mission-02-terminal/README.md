# Mission 02 — Become Comfortable with the Terminal

## 1. Mission Title & Objectives
**Title:** Command-Line Interface Navigation and File Manipulation  
**Objective:** Master essential shell commands, practice safe file operations (creation, copy, move, redirection), understand command-line options and pipes, and explain the function of package managers.

## 2. Work Completed
### Task 2.1 — Essential Terminal Command Reference

| Operation | Command (macOS / Linux) | Functional Behavior |
|---|---|---|
| **Working Directory** | `pwd` | Prints the absolute filesystem path of the current working directory. |
| **Basic Listing** | `ls` | Lists visible files and subdirectories in the target folder. |
| **Detailed Listing** | `ls -l` | Displays long listing with file permissions, link count, owner, file size, and timestamp. |
| **Change Directory** | `cd ..` | Navigates up one level to the parent directory (`cd -` returns to previous). |
| **Create Folder** | `mkdir -p terminal-practice` | Creates a new directory (the `-p` flag creates intermediate parents if needed). |
| **Create Empty File** | `touch practice/notes.txt` | Creates an empty file or updates the access timestamp of an existing file. |
| **Copy File** | `cp notes.txt notes-copy.txt` | Duplicates the file content into an independent new file. |
| **Move / Rename** | `mv notes-copy.txt backup.txt` | Relocates or renames a file without altering its contents. |
| **Display File** | `cat notes.txt` | Concatenates and prints file contents directly to standard output. |

---

### Task 2.2 — Safe Practice with Streams & Redirection
To test file operations safely, I worked inside an isolated `terminal-practice/` directory:

```bash
mkdir -p terminal-practice/task-2-1
cd terminal-practice
printf "First line of terminal practice notes\n" > notes.txt
printf "Second line appended safely\n" >> notes.txt
cat notes.txt
cp notes.txt backup.txt
mv backup.txt notes-backup.txt
```

- **Single Redirection (`>`):** Writes output to a target file. If the file exists, its previous contents are completely overwritten (clobbered).
- **Append Redirection (`>>`):** Appends new data to the end of the file without destroying existing lines.
- **Copy (`cp`) vs Move (`mv`):** Copy creates a completely new, detached copy of the bytes; move simply updates the directory pointer / path entry in the filesystem inode table.

---

### Task 2.3 — Flags and Pipeline Mechanics
Command flags modify how standard Unix utilities execute:
- `ls`: Default compact column listing.
- `ls -l`: Long format showing permissions, hard links, owner, group, size, and date.
- `ls -la`: Includes hidden dotfiles (files starting with `.`, like `.gitignore`).
- `ls -lah`: Displays file sizes in human-readable units (e.g. `4.0K`, `12M`).
- `ls -lah | head -n 5`: Uses the Unix pipe (`|`) to direct the standard output of `ls` directly into the standard input of `head`, restricting output to the first 5 lines.

---

### Task 2.4 — Package Managers on macOS
A package manager automates software discovery, dependency resolution, compilation, installation, and upgrades.
On macOS, **Homebrew** (`brew`) is the de-facto standard package manager. It downloads precompiled binary packages ("bottles") into `/opt/homebrew` and creates appropriate symbolic links into standard PATH directories, preventing manual dependency conflicts.

Verification details are recorded in [CLI Session Evidence](evidence/cli-session.md). Practice files are organized in [`terminal-practice/`](../terminal-practice/).

## 3. Personal Reflections
Working in the terminal felt intimidating at first, but practicing redirection and pipelines made me realize how powerful Unix tools are. Being able to chain small, single-purpose utilities together using pipes is much faster and cleaner than clicking through GUI menus.

## 4. Practical Difficulties & Solutions
- **Challenge:** Accidentally overwriting a practice file by typing `>` instead of `>>`.
- **Resolution:** I recreated the file and made it a habit to double-check my redirection operators before pressing enter.

## 5. Commit & Verification Status
- **Commit Message:** `Complete Terminal and file management mission`
- **Status:** Verified and pushed to `main`.
