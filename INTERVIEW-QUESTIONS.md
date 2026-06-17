# 🎤 Git — Interview Questions

> The Git questions interviewers love (and the "what would you do if..." scenarios), in plain English with short answers you can say out loud. Run the scenarios in this lab first, then use this to **explain** what happened.

**How to use this file:** cover the answers, read a question, answer out loud, then check. The best answers describe *what the command does to your history*, not just the command.

---

## 🟢 Warm-up

**1. What's the difference between Git and GitHub?**
Git is the version-control tool that runs on your machine. GitHub (or GitLab/Bitbucket) is a hosting service for Git repositories that adds collaboration features (PRs, issues, CI). You can use Git with no GitHub at all.

**2. What's the difference between the working directory, staging area, and repository?**
- **Working directory** — your actual files.
- **Staging area (index)** — what you've marked with `git add` to go into the next commit.
- **Repository** — the committed history (`.git`).
So the flow is: edit → `git add` (stage) → `git commit` (save).

**3. What does `git add` actually do?**
It moves your changes into the staging area — a snapshot of what the next commit will contain. It does *not* save to history yet.

**4. Difference between `git fetch` and `git pull`?**
`fetch` downloads new commits from the remote but doesn't change your branch. `pull` = `fetch` + `merge` (it downloads *and* integrates). `pull` is convenient; `fetch` is safer when you want to look before merging.

**5. What is `.gitignore` for?**
It lists files/patterns Git should not track — build output, secrets, `node_modules`, `.env`. Note: it only ignores files that aren't *already* tracked.

---

## 🔵 Branching & merging

**6. Difference between merge and rebase?**
- **Merge** keeps both histories and adds a "merge commit" that ties them together — history is true but can look tangled.
- **Rebase** replays your commits on top of another branch — history stays linear and clean, but you're rewriting commits.
Common rule: **merge** shared/public branches, **rebase** your own local work before sharing.

**7. The golden rule of rebase?**
Never rebase commits that other people have already pulled (i.e. anything pushed to a shared branch). Rebasing rewrites commit hashes; rewriting shared history forces everyone else into a mess.

**8. How do you resolve a merge conflict?**
Git marks the conflicting file with `<<<<<<<`, `=======`, `>>>>>>>`. You open the file, pick the correct combination, remove the markers, then `git add` the file and `git commit` (or `git rebase --continue`). (That's scenario 1 in this lab.)

**9. What's a fast-forward merge?**
When the target branch hasn't moved since you branched, Git can just move the pointer forward — no merge commit needed. `--no-ff` forces a merge commit even when a fast-forward is possible (some teams want that for traceability).

**10. How do you delete a branch (local and remote)?**
```bash
git branch -d feature           # local (safe; -D to force)
git push origin --delete feature # remote
```

---

## 🟣 Undoing things (very common!)

**11. Difference between `git reset` and `git revert`?**
- **`reset`** moves the branch pointer back, *rewriting* history. Good for local commits not yet shared.
- **`revert`** creates a *new* commit that undoes a previous one, keeping history intact. Safe for shared branches.
Use `revert` on anything already pushed.

**12. Explain `reset --soft` vs `--mixed` vs `--hard`.**
- `--soft` — moves HEAD back, keeps changes **staged**.
- `--mixed` (default) — moves HEAD back, keeps changes in the **working directory** (unstaged).
- `--hard` — moves HEAD back and **throws away** the changes. Dangerous.

**13. You committed to the wrong branch. How do you fix it?**
Most simply: undo the commit but keep changes (`git reset --soft HEAD~1`), switch to the right branch, then commit. Or use `git cherry-pick` to copy the commit onto the right branch, then remove it from the wrong one.

**14. You `git reset --hard`'d and lost a commit. Can you get it back?**
Usually yes, with `git reflog`. It records where HEAD has been, so you find the lost commit's hash and `git reset --hard <hash>` (or `git cherry-pick` it). (That's scenario 3 in the history-recovery part.)

**15. How do you undo `git add` (unstage a file)?**
`git restore --staged file` (modern) or `git reset HEAD file` (older). The file keeps your changes; it's just no longer staged.

---

## 🟠 Stash, history, and detective work

**16. What is `git stash` and when do you use it?**
It temporarily shelves your uncommitted changes so you can switch branches or pull cleanly, then `git stash pop` brings them back. Great for "I'm half-done but need to jump to an urgent fix". (Scenario 3 in branching.)

**17. What is interactive rebase used for?**
`git rebase -i` lets you clean up history before sharing: **squash** several commits into one, **reword** messages, **reorder** or **drop** commits. Common before opening a PR. (Scenario 1 in history-recovery.)

**18. How do you find which commit introduced a bug?**
`git bisect`. You mark a known-good and known-bad commit; Git does a binary search through history, you test each step, and it pinpoints the exact breaking commit. `git bisect run <test>` automates it. (Scenario 2 in history-recovery.)

**19. How do you see who changed a specific line and why?**
`git blame file` shows the commit/author for each line. Then `git show <commit>` gives the full context of that change.

**20. Difference between `git cherry-pick` and `git merge`?**
`merge` brings in *all* the changes from another branch. `cherry-pick` copies *one specific commit* onto your current branch. Use cherry-pick for "I just need that one fix".

---

## 🔴 "Senior" / workflow & real-world

**21. Describe a branching strategy you've used.**
Common answers: **GitHub Flow** (main + short-lived feature branches + PRs, deploy from main) or **Git Flow** (main/develop/feature/release/hotfix). Mention short-lived branches, PR review, and CI gating before merge.

**22. What's the difference between HEAD, a branch, and a tag?**
- **HEAD** — a pointer to where you currently are (usually the tip of your current branch).
- **branch** — a movable pointer that advances with each commit.
- **tag** — a fixed pointer to a specific commit, usually a release (`v1.2.0`).

**23. What is a detached HEAD state?**
When HEAD points directly at a commit instead of a branch (e.g. after `git checkout <hash>`). Commits you make there aren't on any branch and can be lost — create a branch (`git switch -c name`) if you want to keep them.

**24. How do you keep a long-running feature branch up to date with main?**
Regularly bring main's changes in — `git rebase main` (clean linear history) or `git merge main` (preserves history). Doing it often means small, manageable conflicts instead of one huge one at the end.

**25. Someone pushed a secret/password. What do you do?**
Rotate the secret immediately (assume it's compromised). Then remove it from history with `git filter-repo` (or BFG), force-push, and tell the team to re-clone. Just deleting it in a new commit isn't enough — it stays in history.

**26. What's a merge conflict you can't auto-resolve, and how do you communicate it?**
When two people changed the same lines with incompatible intent. You can't just "pick one" — you talk to the other author to understand intent, then combine correctly. The technical fix is easy; the communication is the senior part.

---

## 🧠 Hands-on scenarios to rehearse

All of these are built as runnable sandboxes by `setup.py` in this lab.

1. **Resolve a merge conflict** end to end.
2. **Rebase a feature branch** onto an updated main.
3. **Stash work**, switch branches, come back, pop.
4. **Squash 3 messy commits** into 1 with interactive rebase.
5. **Find a bug commit** with `git bisect`.
6. **Recover a "lost" commit** with `git reflog`.

---

## ⭐ Found this useful?
If this helped your prep, please **star** ⭐, **fork** 🍴, and **share** 🔗 the repo on LinkedIn. Got a Git curveball from a real interview? Add it via [CONTRIBUTING.md](CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
