# Mission 06 — Git and GitHub

## 1. Mission title
Mission 06 — Git and GitHub.

## 2. Task / objective
Understand version control, stage and commit changes, create a branch, open a Pull Request and explain collaboration.

## 3. Work completed
### Task 6.1 — Basic Git workflow

| Git operation | Command | What it does |
|---|---|---|
| Check status | `git status` | Shows changed, staged and untracked files |
| Stage selected change | `git add path/to/README.md` | Adds the selected change to the staging area |
| Create commit | `git commit -m "Describe the change"` | Saves a snapshot of staged changes in local history |
| View history | `git log --oneline` | Shows concise recent commit history |

Staging selects the changes that will go into the next commit. Committing records the staged snapshot in the repository's local history.

### Task 6.2 — Branch activity

The assignment asks for a branch named `update-about` and a “My Learning” section in the root README. Example commands:

```bash
git switch -c update-about
# Edit README.md and add the "My Learning" section
git status
git add README.md
git commit -m "Add my learning summary"
git push -u origin update-about
```

Suggested “My Learning” text (edit it so it accurately reflects what you have completed):

> I learned how IPOS describes the flow of information through a computer. I practised using Terminal commands to inspect and manage files. I also learned how Git staging and commits help track project changes.

### Task 6.3 — Pull Request
A branch is a separate line of development that lets someone make changes without immediately changing the main branch. A Pull Request (PR) asks the repository team to review and discuss changes before they are merged into another branch. Branches and PRs make collaboration safer because changes can be checked before joining the main project.

PR description example:

> This Pull Request adds a “My Learning” section to the root README. It summarises the concepts covered so far and keeps the update isolated on the `update-about` branch for review.

**PR status:** Merged (PR #1 created from update-about branch and merged into main - https://github.com/ayushechoglitch/digital-detective--8436/pull/1)

### Task 6.4 — Git command glossary

| Operation | Command | Explanation |
|---|---|---|
| Initialise repository | `git init` | Starts Git tracking in the current folder |
| Check status | `git status` | Shows the state of files |
| Stage changes | `git add` | Selects changes for the next commit |
| Commit changes | `git commit` | Records staged changes |
| View history | `git log` | Displays previous commits |
| Create/list branches | `git branch` | Creates or lists branches |
| Switch branches | `git switch` | Changes the active branch |
| Publish changes | `git push` | Sends local commits to a remote repository |
| Retrieve remote changes | `git pull` | Fetches and integrates remote changes |

## 4. Commands / tools used
`git status`, `git add`, `git commit`, `git log`, `git init`, `git branch`, `git switch`, `git push`, and `git pull` (retain only the commands actually used). GitHub website — used to review branches and create a Pull Request.

## 5. My understanding
Git is a version-control tool that records project history. GitHub hosts Git repositories online and provides collaboration features. A branch isolates work, while a Pull Request makes proposed changes available for review.

## 6. Difficulties faced
No major difficulties encountered with Git branches, commits, and pull requests.

## 7. How I resolved them
Not applicable.

## 8. Evidence / files
- Git command notes
- Visible `update-about` branch
- Pull Request link and status: https://github.com/ayushechoglitch/digital-detective--8436/pull/1 (Merged)

## 9. Commit details
Suggested message: `Complete Git and GitHub collaboration mission`  
Actual commit/push status: Committed and verified on GitHub.
