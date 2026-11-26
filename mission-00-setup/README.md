# Mission 00 — Create Your GitHub Workspace

## 1. Mission Title & Objectives
**Title:** Repository Setup and Local Workspace Configuration  
**Objective:** Initialize a clean, structured local repository for the Digital Detective assignment and link it to a public GitHub repository following the designated naming convention (`digital-detective-XXXX` using USN digits `8436`).

## 2. Environment & Tools Verified
Before scaffolding the folders, I checked the local command-line environment on macOS:
- **Python:** `Python 3.9.6` (Apple Clang / macOS system framework)
- **Git:** `git version 2.54.0 (Apple Git-157)`
- **Shell:** `zsh 5.9 (x86_64-apple-darwin26.0)`
- **Remote Host:** GitHub (`https://github.com/ayushechoglitch/digital-detective--8436`)

## 3. Work Completed
- Initialized local Git repository tracking on branch `main`.
- Structured the workspace with modular mission directories (`mission-00-setup` through `mission-08-final-report`) to prevent clutter.
- Created an `evidence/` directory for storing sanitized outputs and logs.
- Configured a `.gitignore` to prevent OS cache files (like `.DS_Store`) from polluting the repository history.
- Verified remote connectivity to GitHub via HTTPS.

Detailed verification records are archived in [Mission 00 Setup Evidence](../evidence/mission-00-setup.md).

## 4. Concept Reflection: What is a Repository?
A Git repository is far more than a simple folder of files. It is an append-only directed acyclic graph (DAG) of snapshots that records the entire evolutionary history of a project. Each commit records exactly who made a change, when it occurred, and what changed. 

Separating work into dedicated mission folders from day one ensures that each milestone is focused, independently verifiable, and easy to review without cross-contamination.

## 5. Practical Difficulties & Solutions
- **Challenge:** Making sure the GitHub remote URL correctly matched the repository name on GitHub without credential mismatch errors.
- **Resolution:** Verified the remote configuration using `git remote -v` and confirmed HTTPS authentication through Git credentials helper before making the initial commit.

## 6. Commit & Verification Status
- **Commit Message:** `Set up Digital Detective mission structure`
- **Status:** Verified on GitHub `main` branch.
