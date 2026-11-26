# Mission 06 — Git Workflow Evidence

Sanitized command log of Git branch and pull request operations.

```text
$ git status --short
 M README.md

$ git switch -c update-about
Switched to a new branch 'update-about'

$ git add README.md
$ git commit -m "Add My Learning summary to root README"
[update-about 3d62389] Add My Learning summary to root README
 1 file changed, 3 insertions(+)

$ git push -u origin update-about
Branch 'update-about' set up to track remote branch 'update-about' from 'origin'.
```

Pull Request created and merged successfully into `main`.
