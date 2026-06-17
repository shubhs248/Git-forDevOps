# Solution — Scenario 2.3 Stash Your Work to Switch Branches

```bash
cd sandbox/stash-and-switch

# See the unfinished change first
git status                       # notes.txt modified

# 1. Park the changes safely
git stash                        # or: git stash push -m "wip notes"
git status                       # clean now
git stash list                   # stash@{0}: WIP on main: ...

# 2. Switch to release (works because the tree is clean)
git switch release

# 3. ...do whatever you needed to do, then come back
git switch main

# 4. Bring your changes back and drop them from the stash
git stash pop
git status                       # notes.txt modified again
git stash list                   # empty
```

### What happened
`git stash` saved your uncommitted changes and reset your working tree to the last commit, so you were free to switch branches. `git stash pop` re-applied them when you returned and removed the saved copy.

### Good to know
- `git stash apply` also restores the changes but **keeps** the stash entry (handy if you want to apply the same changes to more than one branch).
- `git stash` ignores untracked files by default. Use `git stash -u` to include new, untracked files too.
- See everything stashed with `git stash list`; inspect one with `git stash show -p stash@{0}`.
