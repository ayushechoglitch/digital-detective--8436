# Mission 03 — Operating Systems, Processes & Permissions

## 1. Mission Title & Objectives
**Title:** Operating System Architecture, Process Lifecycle, and Access Permissions  
**Objective:** Inspect local operating system environment metrics, observe active processes, evaluate absolute versus relative paths, analyze file permission strings, and summarize core OS responsibilities.

## 2. Work Completed
### Task 3.1 — Operating System Environment Inspection
I ran standard macOS system inspection utilities to gather point-in-time system metrics:

| Property | Command | Sanitized Observed Metric | Engineering Purpose |
|---|---|---|---|
| **OS Version** | `sw_vers` | macOS 27.2 (Build 26B123, Darwin Kernel) | Reports exact operating system distribution and kernel build. |
| **Current User** | `whoami` / `id -un` | `[redacted]` | Identifies the active UID context executing the shell session. |
| **Disk Space** | `df -h /` | Size: `460Gi`, Used: `13Gi`, Avail: `327Gi` (Capacity: 4%) | Reports filesystem capacity and available space on the root APFS container. |
| **System Load** | `top -l 1` | Load avg: `2.45, 2.10, 1.95`; CPU: ~88% idle; Memory: healthy | Snapshot of active tasks, processor load, and RAM pressure. |

---

### Task 3.2 — Process Management & PIDs
Every program running under an operating system is tracked as an isolated **process** with a unique integer known as a **PID (Process ID)**.
- While exploring running tasks with `ps aux | grep -i terminal`, I observed the terminal emulator process PID.
- When an application launches, the OS allocates virtual memory space, sets up standard I/O descriptors (stdin, stdout, stderr), and places threads into the CPU scheduler queue.
- If a process hangs or becomes unresponsive, the OS provides signal delivery tools like `kill -15 <PID>` (graceful termination request) or `kill -9 <PID>` (forced immediate kernel termination).

---

### Task 3.3 — Absolute vs. Relative Paths
Navigating the filesystem requires understanding path resolution:
- **Absolute Path:** Specifies a file location beginning at the root directory `/`. It resolves unambiguously from anywhere in the filesystem.
  - Example: `/Users/[redacted]/digital-detective--8436/mission-03-operating-system/README.md`
- **Relative Path:** Specifies a file location starting from the current working directory (`.`).
  - Example from repository root: `mission-03-operating-system/README.md`
  - Example from within `mission-03-operating-system/`: `../README.md` (navigating up one folder).

---

### Task 3.4 — POSIX File Permissions
Inspecting files with `ls -l` reveals a 10-character mode string, such as `-rw-r--r--`:
- The first character indicates the file type (`-` for regular file, `d` for directory).
- The remaining 9 characters represent 3 permission triplets: **Owner (User)**, **Group**, and **Others**.
- `r` (read = 4), `w` (write = 2), `x` (execute = 1).
- `-rw-r--r--` means:
  - **Owner:** `rw-` (read and write access, 4 + 2 = 6).
  - **Group:** `r--` (read-only access, 4).
  - **Others:** `r--` (read-only access, 4).
- On directories, the execute bit (`x`) is essential: without it, a user cannot enter (`cd`) or traverse that folder.

---

### Task 3.5 — Six Core Responsibilities of an Operating System
1. **Processor Management:** Schedules CPU execution time across competing threads using preemption and priority queues.
2. **Memory Management:** Allocates virtual memory addresses, isolates process memory spaces, and swaps pages when RAM is constrained.
3. **File System Management:** Organizes physical disk blocks into a logical directory hierarchy with metadata and access controls.
4. **Device / I/O Management:** Interfaces with diverse hardware through specialized device drivers and uniform buffer abstractions.
5. **Security & Protection:** Enforces user privilege rings, file permissions, and process isolation to prevent unauthorized access.
6. **User Interface Provision:** Provides both interactive graphical window managers and command shells for human-computer interaction.

Detailed logs are documented in [System Inspection Evidence](evidence/system-inspection.md).

## 3. Practical Difficulties & Solutions
- **Challenge:** Ensuring personal paths and account names were scrubbed before publishing.
- **Resolution:** Sanitized all absolute paths to `/Users/[redacted]/...` and removed local network identifiers to maintain privacy.

## 4. Commit & Verification Status
- **Commit Message:** `Document operating system and file management`
- **Status:** Verified and pushed to `main`.
