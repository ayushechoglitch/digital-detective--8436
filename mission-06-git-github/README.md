# Mission 06 — Version Control & GitHub Collaboration

## 1. Mission Title & Objectives
**Title:** Git Version Control, Branching Models, and Pull Request Collaboration  
**Objective:** Master core version control workflows (status, staging, committing, log inspection), create an isolated feature branch (`update-about`), submit a Pull Request, and document team collaboration principles.

## 2. Work Completed
### Task 6.1 — Core Git Workflow: The Three Trees
Git manages changes across three distinct local environments:
1. **Working Directory:** The actual active files on the local filesystem.
2. **Staging Area (Index):** A curated snapshot of prepared changes staged via `git add`.
3. **Commit History (`.git` repository):** Permanent cryptographic snapshots committed via `git commit`.

| Operation | Command | Technical Function |
|---|---|---|
| **Check Status** | `git status` | Displays untracked, modified, and staged files. |
| **Stage Changes** | `git add <file>` | Moves changes from working directory to staging index. |
| **Record Commit** | `git commit -m "..."` | Captures staged changes into an immutable historical commit object. |
| **View History** | `git log --oneline` | Displays concise linear commit history with short SHAs. |

**Staging vs. Committing:** Staging lets you craft clean, atomic commits by selecting exactly which file modifications belong together, rather than dumping all work blindly into history.

---

### Task 6.2 — Branching & Isolated Development
To practice safe team workflows, I created an isolated feature branch named `update-about`:

```bash
git switch -c update-about
# Updated root README.md with the "My Learning" reflection
git add README.md
git commit -m "Add My Learning summary to root README"
git push -u origin update-about
```

Branching allows developers to experiment, build features, and fix bugs in total isolation without destabilizing the production `main` branch.

---

### Task 6.3 — Pull Requests & Team Collaboration
A **Pull Request (PR)** is a mechanism for proposing that changes from a feature branch be merged into the target branch (`main`).
- It provides a centralized space for code review, diff inspection, automated CI checks, and peer feedback before code enters the main project.
- **PR Activity:**
  - Opened PR on GitHub from branch `update-about` into `main`.
  - Reviewed the file diff (`README.md` additions).
  - Merged PR via GitHub merge commit, integrating the work cleanly into the `main` project line.

---

### Task 6.4 — Git Command Glossary

| Git Command | Plain-English Explanation |
|---|---|
| `git init` | Initializes a new, empty Git version control repository in the current folder. |
| `git status` | Inspects the current state of files across working directory and staging index. |
| `git add` | Stages selected file changes to be included in the next commit snapshot. |
| `git commit` | Permanently records the staged snapshot into the repository history with a message. |
| `git log` | Displays chronological commit history and author metadata. |
| `git branch` | Lists local branches or creates a new branch pointer. |
| `git switch` | Switches the working tree to a different branch context. |
| `git push` | Transmits local commits to a remote hosting platform like GitHub. |
| `git pull` | Fetches and integrates changes from the remote repository into the local branch. |

Evidence records are archived in [Git Workflow Evidence](evidence/git-workflow.md).

## 3. Practical Difficulties & Solutions
- **Challenge:** Understanding how switching branches changes files on disk.
- **Resolution:** Monitored the working directory with `ls` and `git status` while switching between `main` and `update-about`, confirming that Git automatically swaps the active file versions.

## 4. Commit & Verification Status
- **Commit Message:** `Complete Git and GitHub collaboration mission`
- **Branch Activity:** Branch `update-about` created, committed, and merged via PR.
