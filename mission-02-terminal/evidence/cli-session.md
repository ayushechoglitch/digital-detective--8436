# Mission 02 — CLI Practice Evidence

Sanitized terminal transcript from the command-line exercises conducted on macOS.

## Task 2.1 & 2.2 Transcript
```text
$ pwd
/Users/[redacted]/digital-detective--8436

$ ls
README.md                    mission-02-terminal
evidence                     mission-03-operating-system
mission-00-setup             terminal-practice
mission-01-computer-basics

$ mkdir -p terminal-practice/task-2-1
$ touch terminal-practice/task-2-1/empty.txt
$ ls -l terminal-practice/task-2-1/
-rw-r--r--  1 [redacted]  staff  0 Nov 25 23:38 empty.txt

$ printf "First line\n" > terminal-practice/notes.txt
$ printf "Second line\n" >> terminal-practice/notes.txt
$ cat terminal-practice/notes.txt
First line
Second line

$ cp terminal-practice/notes.txt terminal-practice/backup.txt
$ mv terminal-practice/backup.txt terminal-practice/notes-backup.txt
$ ls -l terminal-practice/
-rw-r--r--  1 [redacted]  staff  23 Nov 25 23:38 notes-backup.txt
-rw-r--r--  1 [redacted]  staff  23 Nov 25 23:38 notes.txt
drwxr-xr-x  3 [redacted]  staff  96 Nov 25 23:38 task-2-1
```

All commands executed cleanly with expected return codes (exit code 0).
