# Solution — Scenario 3.1 Clean Up History with Interactive Rebase

You can do this two ways. Way B is the easiest if you are not comfortable with the editor yet.

## Way A — interactive rebase

```bash
cd sandbox/interactive-rebase

git rebase -i HEAD~3
```

An editor opens showing the 3 newest commits (oldest at the top):

```
pick a23b480 wip
pick 98f5597 fix tpyo
pick 1460b1f more wip
```

Change it so the first stays `pick` and the others are `squash` (combine into the one above):

```
pick a23b480 wip
squash 98f5597 fix tpyo
squash 1460b1f more wip
```

Save and close. Git opens a second editor for the final message — delete the messy lines and write one clean message, e.g.:

```
Add login feature
```

Save and close. Done.

> 💡 If `git rebase -i` shows an error about no editor, set one first:
> `git config core.editor "nano"`  (Windows: `git config core.editor "notepad"`).

## Way B — soft reset (no editor needed)

```bash
cd sandbox/interactive-rebase

# Move the last 3 commits' changes back into staging (files are kept)
git reset --soft HEAD~3

# Make one clean commit
git commit -m "Add login feature"
```

## Confirm (either way)

```bash
git log --oneline
#   <hash> Add login feature      <- a single, clean commit
cat login.py                      # final content is still here
```

### What happened
Both approaches replace several small commits with one. Interactive rebase is the flexible tool (you can squash, reword, reorder, or drop commits); the soft reset is a quick shortcut when you just want to mash the latest commits into one.
