# Mission 01 — Know Your Computer & The IPOS Cycle

## 1. Mission Title & Objectives
**Title:** Computer Fundamentals, Hardware/Software Roles, and Everyday Systems  
**Objective:** Investigate how a modern computer processes data through the Input-Processing-Output-Storage (IPOS) framework, classify common hardware and software components, and examine computer systems embedded in society.

## 2. Work Completed
### Task 1.1 — The IPOS Cycle in Action: Typing & Saving a Document
To understand the IPOS cycle in daily practice, I analyzed what occurs inside my Mac when I open Visual Studio Code, write lecture notes, and save the file:

| Stage | What Actually Happens | Key Hardware / Component |
|---|---|---|
| **Input** | I press letters on the keyboard. Each physical keystroke closes a switch, triggering a scan code that is sent as an interrupt to the OS. | Built-in Apple Magic Keyboard / Trackpad |
| **Processing** | The CPU decodes the keyboard interrupt, hands the input event to the editor's event loop, recalculates the active buffer in RAM, and prepares the render frame. | Apple Silicon CPU & Unified RAM |
| **Output** | The editor instructs the GPU to render text glyphs onto the screen. The updated document text appears instantly in front of me. | Retina Display (GPU Framebuffer) |
| **Storage** | When I press `Cmd + S`, the editor requests the operating system write the buffer permanently to the APFS file system on the flash drive. | Solid State Drive (NVMe SSD) |

**Key Takeaway:** Processing and storage are complementary but distinct. RAM is ultra-fast, temporary scratch space that vanishes when power is lost; the SSD is non-volatile persistent storage designed to retain files safely across reboots.

---

### Task 1.2 — Hardware & Software Classification

| Component / Tool | Classification | Software Category | Functional Purpose |
|---|---|---|---|
| **Magic Keyboard** | Hardware | N/A | Captures alphanumeric user input via key switches. |
| **Force Touch Trackpad** | Hardware | N/A | Translates finger gestures and taps into pointer coordinates. |
| **Retina Display** | Hardware | N/A | Emits visual pixels showing GUI windows and terminal text. |
| **PCIe NVMe SSD** | Hardware | N/A | Non-volatile flash storage for OS, applications, and documents. |
| **macOS (Darwin)** | Software | Operating System | Orchestrates hardware resources, schedules processes, and enforces permissions. |
| **Visual Studio Code** | Software | Application Software | Provides an interactive IDE for writing, debugging, and editing code. |
| **Google Chrome** | Software | Application Software | Client browser for navigating the web and rendering HTML/CSS/JS. |
| **Activity Monitor** | Software | System Utility | Diagnostic tool for monitoring CPU, memory, disk, and process metrics. |

---

### Task 1.3 — Computer Systems in Everyday Life

| Embedded System | Primary Purpose | Primary Input(s) | Primary Output(s) |
|---|---|---|---|
| **Bank ATM** | Enables secure self-service banking transactions | Chip card reader, numeric PIN pad, touch selections | Cash dispensing mechanism, paper receipt, on-screen balance |
| **Metro Transit Fare Gate** | Validates passenger tickets and controls platform access | RFID / NFC smartcard sensor, optical QR code scanner | Motorized gate barrier release, status chime, LED display |
| **Traffic Light Controller** | Regulates intersection vehicle and pedestrian flow | Inductive road loop sensors, pedestrian push-buttons, timer clocks | Red, yellow, green relay signals, pedestrian walk signs |

Detailed observations are compiled in [Mission 01 Completion Evidence](../evidence/mission-01-completion.md).

## 3. Personal Understanding & Reflection
Before this mission, I thought of computers mostly through the applications I run. Walking through the IPOS model made it clear that every high-level software action depends on a synchronized chain of physical hardware events. The operating system acts as the invisible bridge, ensuring user inputs are handled by the CPU and safely stored on disk without crashing the machine.

## 4. Practical Difficulties & Solutions
- **Challenge:** Distinguishing clearly between system software and utilities.
- **Resolution:** I researched macOS architecture and realized that while the OS kernel handles low-level process and memory management, utilities like Activity Monitor and Disk Utility are user-facing diagnostic tools that query OS counters.

## 5. Commit & Verification Status
- **Commit Message:** `Complete computer basics and IPOS mission`
- **Status:** Verified and pushed to `main`.
