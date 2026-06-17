# Scenario 3.1 — Clean Up History with Interactive Rebase

**Sandbox:** `sandbox/interactive-rebase`
**You practise:** squashing several messy commits into one and rewording it.

---

## 📖 The situation
While building a login feature you committed in small messy steps. The history looks like this (newest first):

```
more wip
fix tpyo          <- note the typo in the message too!
wip
Add login feature
```

Before you share this, you want it to read as **one clean commit** with a clear message, instead of three "wip"-style commits.

## 🎯 Your task
Combine the **last 3 commits** (`wip`, `fix tpyo`, `more wip`) into the `Add login feature` commit — or into a single new commit — and give it one clear message, for example `Add login feature`.

## ✅ How to check you succeeded
- `git log --oneline` shows **one** commit for this work (not four), with a clean message.
- The file `login.py` still has its final content (nothing lost).

## 💡 Hints

There are two common ways. Pick whichever you like.

**Way A — interactive rebase (the classic):**
- Run `git rebase -i HEAD~3`.
- An editor opens listing the 3 commits with `pick` in front of each.
- Change the lines so the older ones are `pick` and the rest are `squash` (or `s`). To also change the message, use `reword` (`r`).
- Save and close. Git then lets you write the final commit message.
- 💡 No editor set up? Tell Git which one to use first, e.g. `git config core.editor "nano"` (or `notepad` on Windows).

**Way B — soft reset (no editor needed):**
- `git reset --soft HEAD~3` moves the last 3 commits' changes back into staging, keeping the files.
- Then make one fresh commit: `git commit -m "Add login feature"`.

> Stuck? See [`solutions/scenario-1-interactive-rebase.md`](solutions/scenario-1-interactive-rebase.md).
> Want to start over? Run `python setup.py` from the lab root.
