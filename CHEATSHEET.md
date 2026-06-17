# 📋 Git Quick-Revision Cheatsheet

A one-page reminder of the Git commands you use most. Use it alongside the scenarios.

## Start & save work
```bash
git init                     # start tracking a folder
git status                   # what has changed?
git add <file>               # stage a file for the next commit (git add -A = everything)
git commit -m "message"      # save a snapshot
git log --oneline --graph    # see history, one line per commit, with branches
git diff                     # changes not yet staged
git diff --staged            # changes that ARE staged
```

## Branches
```bash
git branch                   # list branches
git switch <name>            # move to a branch         (old: git checkout <name>)
git switch -c <name>         # create and move to it    (old: git checkout -b <name>)
git branch -d <name>         # delete a merged branch
```

## Combining branches
```bash
git merge <branch>           # join <branch> into the current one (may conflict)
git merge --abort            # cancel an in-progress merge
git rebase <branch>          # replay current branch's commits on top of <branch>
git rebase --continue        # after fixing a conflict during a rebase
git rebase --abort           # cancel an in-progress rebase
```

## Fixing a merge/rebase conflict
```bash
# 1. open the file, find the markers, keep the text you want:
#    <<<<<<< HEAD   (your side)   ======= (their side)   >>>>>>> branch
# 2. then:
git add <file>
git commit                   # (merge)   or   git rebase --continue   (rebase)
```

## Undo things (in order of "force")
```bash
git restore <file>           # throw away unstaged changes to a file
git restore --staged <file>  # unstage a file, keep the changes  (old: git reset HEAD <file>)
git commit --amend           # change the LAST commit (message or contents)
git reset --soft HEAD~1      # undo last commit, KEEP changes staged
git reset --mixed HEAD~1     # undo last commit, keep changes unstaged (default)
git reset --hard HEAD~1      # undo last commit AND discard changes (careful!)
git revert <hash>            # make a NEW commit that undoes an old one (safe to share)
```

## Stash (park unfinished work)
```bash
git stash                    # save changes, clean the working tree
git stash -u                 # include untracked files too
git stash list               # see saved stashes
git stash pop                # restore latest stash and remove it
git stash apply              # restore latest stash but keep it
```

## Rewrite recent history
```bash
git rebase -i HEAD~3         # pick / squash / reword / reorder / drop the last 3 commits
git reset --soft HEAD~3 && git commit -m "msg"   # quick way to squash last 3 into one
git cherry-pick <hash>       # copy one specific commit onto the current branch
```

## Find a bad commit
```bash
git bisect start <bad> <good>   # e.g. git bisect start HEAD HEAD~6
git bisect run <test-cmd>       # auto-test each step (exit 0 = good, non-0 = bad)
git bisect reset                # finish and go back to where you were
```

## Rescue lost work
```bash
git reflog                   # everywhere HEAD has been (your safety net)
git reset --hard <hash>      # move the branch back onto a lost commit
git branch rescue <hash>     # or save the lost commit on a new branch
```

## Remotes (working with GitHub)
```bash
git clone <url>              # copy a repo
git remote -v               # list remotes
git pull                    # fetch + merge the latest from the remote
git push                    # send your commits to the remote
git push -u origin <branch> # push a new branch and track it
git fetch                   # download remote changes without merging
```

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to improve it? See [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
