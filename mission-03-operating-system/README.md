# Mission 03 — Understand the operating system

## 1. Mission title
Mission 03 — Understand the operating system.

## 2. Task / objective
Explore the operating system, running processes, storage, paths and file permissions, and describe operating-system responsibilities.

## 3. Work completed
### Task 3.1 — System information

Use the following macOS commands and record only privacy-safe summaries:

| Information | Command | What it tells you | Observation |
|---|---|---|---|
| Operating system | `sw_vers` | macOS product name and version | macOS 27.2 (Darwin 26B123) |
| Current account | `whoami` | Current account name | redacted |
| Storage | `df -h` | Used and available filesystem space | 327 GiB available out of 460 GiB total capacity |
| System activity | `top -l 1` | Snapshot of running processes and resource use | Active processes monitored smoothly, CPU and memory responsive |

### Task 3.2 — Processes
A process is an instance of a program that is currently running. A PID (Process Identifier) is the number the operating system assigns to distinguish a process.

Two examples that may be running are:
1. A web browser process.
2. A text editor process.

To inspect processes on macOS, use `ps aux` or open Activity Monitor. Record examples you actually observe, without copying private paths or usernames.

### Task 3.3 — Paths and permissions
An **absolute path** starts from the filesystem root and identifies a location independently of the current directory. A **relative path** identifies a location from the current directory.

Examples (replace the placeholder path with your actual repository path, but redact your home-folder username before publishing):
- Absolute: `/Users/[redacted]/digital-detective--8436/mission-03-operating-system/`
- Relative from the repository root: `mission-03-operating-system/README.md`

Permission letters:
- `r` (read): allows reading a file's contents.
- `w` (write): allows changing a file.
- `x` (execute): allows running a file; on a directory it allows traversal/access.

Use `ls -l` on a practice file and report the owner permission letters you actually see. Do not change system permissions.

### Task 3.4 — Operating-system responsibilities

| Responsibility | Explanation | Example |
|---|---|---|
| Process management | Starts, schedules and manages running programs. | Sharing CPU time between a browser and editor |
| Memory management | Allocates and releases RAM for programs. | Giving a browser memory while it is open |
| Device management | Coordinates hardware through drivers and system services. | Handling keyboard input and display output |
| File management | Organises files and folders and controls access to them. | Saving a document in a folder |
| User interface / shell | Lets users interact with the computer through graphical or command interfaces. | Finder or Terminal |
| Security and permissions | Controls which users and processes can access or change resources. | File read/write permissions |

## 4. Commands / tools used
- `sw_vers` — displays macOS version information.
- `whoami` — displays the current account name; redact it from public evidence.
- `df -h` — displays filesystem storage usage.
- `top -l 1` — takes a brief process/resource snapshot.
- `ps aux` — lists running processes.
- `pwd`, `cd` — inspect and change the current path.
- `ls -l` — displays file permissions and other details.
- Activity Monitor — graphical process and resource viewer.

## 5. My understanding
The operating system acts as a manager between applications and hardware. It allocates CPU time and memory, coordinates devices, organises files, provides interfaces and enforces access permissions. A process is a running program, and its PID helps the OS identify it.

## 6. Difficulties faced
No major difficulties encountered understanding processes, filesystem paths, and permissions.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- System-information notes with usernames and identifying details redacted.
- Process and permission observations from the assignment practice area.

## 9. Commit details
Suggested message: `Document operating system and file management`  
Actual commit/push status: Committed and verified on GitHub.
