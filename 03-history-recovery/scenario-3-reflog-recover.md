# Scenario 3.3 — Rescue a Lost Commit with `git reflog`

**Sandbox:** `sandbox/reflog-recover`
**You practise:** getting back a commit that seems to have vanished.

---

## 📖 The situation
You had two commits:

```
Add the important feature     <- had the "secret sauce" in work.txt
Add project
```

Then someone ran `git reset --hard HEAD~1` and the `Add the important feature` commit disappeared from the history. `git log` now only shows `Add project`, and `work.txt` no longer has the important line. 😱

Good news: Git almost never throws anything away immediately. The **reflog** records every place `HEAD` has been, so you can find the lost commit and bring it back.

## 🎯 Your task
1. Find the lost commit `Add the important feature` using the reflog.
2. Restore it so it is back in your branch history and `work.txt` has the important line again.

## ✅ How to check you succeeded
- `git log --oneline` shows **both** commits again.
- `work.txt` contains the line `IMPORTANT: the secret sauce.`

## 💡 Hints
- See everywhere HEAD has been: `git reflog`. Look for the line mentioning `Add the important feature` — note its short hash (or its `HEAD@{1}` name).
- Easiest fix (move your branch back to it):
  ```bash
  git reset --hard <hash>        # e.g. the one labelled "commit: Add the important feature"
  ```
- Prefer not to move the branch? You can instead bring just that commit back on top:
  ```bash
  git cherry-pick <hash>
  ```
- Or point a brand-new branch at it so you do not lose it: `git branch rescue <hash>`.

> Stuck? See [`solutions/scenario-3-reflog-recover.md`](solutions/scenario-3-reflog-recover.md).
> Want to start over? Run `python setup.py` from the lab root.
