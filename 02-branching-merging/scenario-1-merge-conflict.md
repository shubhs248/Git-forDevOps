# Scenario 2.1 — Resolve a Merge Conflict

**Sandbox:** `sandbox/merge-conflict`
**You practise:** merging a branch and fixing a conflict by hand.

---

## 📖 The situation
There is one file, `greeting.txt`. Two branches changed the **same line** in different ways:

- `main` changed it to `Hello, Team!`
- `feature` changed it to `Hello, DevOps!`

You are on `main`. When you try to merge `feature`, Git cannot decide which line wins, so it stops and asks you to choose. This is a **merge conflict** — totally normal, and your job is to resolve it.

## 🎯 Your task
1. Merge `feature` into `main`.
2. Open `greeting.txt` and fix the conflict so the file has the final text you want (for example: `Hello, DevOps Team!`).
3. Mark it as resolved and finish the merge.

## ✅ How to check you succeeded
- `git status` shows a clean working tree (nothing to commit).
- `git log --oneline --graph` shows a **merge commit** joining the two branches.
- `greeting.txt` has your final line and **no** `<<<<<<<`, `=======`, or `>>>>>>>` markers left in it.

## 💡 Hints
- Start the merge with `git merge feature`. Git will tell you there is a conflict.
- Open `greeting.txt`. A conflict looks like this:
  ```
  <<<<<<< HEAD
  Hello, Team!
  =======
  Hello, DevOps!
  >>>>>>> feature
  ```
  Everything between `<<<<<<<` and `=======` is your side (main); everything between `=======` and `>>>>>>>` is the other side (feature). Delete the markers and keep the text you want.
- After editing, run `git add greeting.txt`, then `git commit` to complete the merge.
- Changed your mind mid-merge? `git merge --abort` puts everything back.

> Stuck? See [`solutions/scenario-1-merge-conflict.md`](solutions/scenario-1-merge-conflict.md).
> Want to start over? Run `python setup.py` from the lab root.
