# Scenario 2.3 — Stash Your Work to Switch Branches

**Sandbox:** `sandbox/stash-and-switch`
**You practise:** parking unfinished changes with `git stash`.

---

## 📖 The situation
You are on `main` in the middle of editing `notes.txt` — the changes are **not committed yet**. Suddenly you need to jump over to the `release` branch to check something. You do not want to commit half-finished work, and you do not want to lose it either.

`git stash` is the answer: it tucks your changes away safely so your working tree is clean, lets you switch branches, and then gives the changes back when you return.

## 🎯 Your task
1. Stash your uncommitted changes on `main`.
2. Switch to the `release` branch (your working tree should now be clean).
3. Switch back to `main`.
4. Bring your stashed changes back so you can keep working.

## ✅ How to check you succeeded
- After stashing, `git status` on `main` is clean and `git stash list` shows one entry.
- You can switch to `release` and back without errors.
- After restoring, `git status` shows `notes.txt` modified again, and `git stash list` is empty.

## 💡 Hints
- Save your work: `git stash` (or `git stash push -m "wip notes"` to give it a name).
- See what is stashed: `git stash list`.
- Switch branches: `git switch release`, then `git switch main`.
- Bring changes back and remove them from the stash: `git stash pop`.
  (`git stash apply` brings them back but **keeps** the stash entry.)

> Stuck? See [`solutions/scenario-3-stash-and-switch.md`](solutions/scenario-3-stash-and-switch.md).
> Want to start over? Run `python setup.py` from the lab root.
