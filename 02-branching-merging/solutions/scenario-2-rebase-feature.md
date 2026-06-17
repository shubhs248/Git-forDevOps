# Solution — Scenario 2.2 Rebase a Feature Branch

```bash
cd sandbox/rebase-feature

# 1. Make sure you are on feature
git switch feature
git branch --show-current     # -> feature

# 2. See the fork before you start (optional)
git log --oneline --graph --all

# 3. Replay feature's commits on top of the latest main
git rebase main
#   Successfully rebased and updated refs/heads/feature.

# 4. Confirm the history is now a straight line
git log --oneline --graph
#   * Add shiny feature
#   * Update app to version 2
#   * Initial app
```

### What happened
`git rebase main` took your `Add shiny feature` commit, set it aside, fast-forwarded `feature` to match `main`, then re-applied your commit on top. The result is a clean straight history instead of a fork plus a merge commit.

### If a rebase hits a conflict (not in this scenario, but good to know)
```bash
# fix the conflicted files, then:
git add <file>
git rebase --continue
# or give up and go back to how things were:
git rebase --abort
```

### Remember
Rebasing rewrites commits (they get new IDs). Do it freely on your own local branches, but avoid rebasing commits you have already pushed and shared.
