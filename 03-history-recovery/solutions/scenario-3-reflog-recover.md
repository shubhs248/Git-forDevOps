# Solution — Scenario 3.3 Rescue a Lost Commit with `git reflog`

```bash
cd sandbox/reflog-recover

# The branch only shows one commit now
git log --oneline
#   <hash> Add project

# 1. Look at everywhere HEAD has been
git reflog
#   a610d8c HEAD@{0}: reset: moving to HEAD~1
#   754ee82 HEAD@{1}: commit: Add the important feature   <- the lost commit!
#   a610d8c HEAD@{2}: commit (initial): Add project
```

```bash
# 2a. Easiest: move the branch back onto the lost commit
git reset --hard 754ee82          # use the hash YOU see, or: git reset --hard HEAD@{1}

# Confirm
git log --oneline                 # both commits are back
cat work.txt                      # has "IMPORTANT: the secret sauce."
```

### Other ways to recover
```bash
# Bring just that commit back on top of the current branch:
git cherry-pick 754ee82

# Or park it safely on a new branch without moving your current one:
git branch rescue 754ee82
```

### What happened
A commit is not truly deleted right away — it just had nothing pointing to it after the `reset --hard`. The **reflog** is Git's private diary of where `HEAD` (and each branch) has been, so you can look up the commit's hash and point your branch back at it.

### Remember
- The reflog is **local only** — it is not pushed or cloned.
- Entries expire eventually (90 days by default for reachable history), so recover sooner rather than later.
- This is why `git reset --hard` is rarely a true disaster: check `git reflog` before you panic.
