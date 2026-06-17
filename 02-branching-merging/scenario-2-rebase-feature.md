# Scenario 2.2 — Rebase a Feature Branch

**Sandbox:** `sandbox/rebase-feature`
**You practise:** rebasing to keep a clean, straight history.

---

## 📖 The situation
You started a `feature` branch and added a commit (`Add shiny feature`). While you were working, `main` moved ahead with another commit (`Update app to version 2`). Now `feature` is **based on an old version of main**.

You could merge, but that creates an extra merge commit. Instead you want a **clean, straight line**: take your feature commit and replay it on top of the latest `main`. That is what `git rebase` does.

## 🎯 Your task
1. Make sure you are on the `feature` branch.
2. Rebase `feature` on top of `main`.
3. End up with a straight history where `Add shiny feature` sits on top of `Update app to version 2`.

## ✅ How to check you succeeded
- `git log --oneline --graph` shows a **single straight line** (no fork), with your feature commit newest.
- `git log --oneline main..feature` shows just your one feature commit (it is now ahead of main).

## 💡 Hints
- First check where you are: `git branch --show-current` (switch with `git switch feature` if needed).
- Run `git rebase main`.
- In this scenario the two branches changed **different files**, so the rebase is clean — no conflict.
- If a rebase ever does hit a conflict: fix the files, `git add` them, then `git rebase --continue`. To bail out, `git rebase --abort`.
- ⚠️ Real-world rule of thumb: rebase your **own** local branches freely, but avoid rebasing commits you have already shared/pushed with others.

> Stuck? See [`solutions/scenario-2-rebase-feature.md`](solutions/scenario-2-rebase-feature.md).
> Want to start over? Run `python setup.py` from the lab root.
