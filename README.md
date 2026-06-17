# 🌿 Git Scenarios — Practice Lab

> A **clone-and-go** lab where you fix real Git situations: merge conflicts, rebases, lost commits, finding a bad commit with `bisect`, and more. Every scenario sets up a small broken/ready repo for you to work in safely.

[![Made with Git](https://img.shields.io/badge/Made%20with-Git-F05032.svg?logo=git&logoColor=white)](https://git-scm.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🎯 Why this repo?

You can read about `git rebase` a hundred times, but you only really learn it the first time you do it on a repo that is in a tricky state. This lab gives you those tricky states on demand — and a way to reset them whenever you want to try again.

A small script builds **throwaway practice repos** inside a `sandbox/` folder. You do the task in there. If you mess it up, just rebuild and start fresh. Nothing you do can affect this lab or your real projects.

## 🗂️ What's inside

```
git-scenarios-lab/
├── README.md                 ← you are here
├── CHEATSHEET.md             ← 1-page Git command reminder
├── CONTRIBUTING.md           ← how to add your own scenarios
├── setup.py                  ← builds (or rebuilds) all the practice repos
├── 01-git-fundamentals/      ← warm-up: init, add, commit, branch, undo
│   └── README.md
├── 02-branching-merging/     ← merge conflicts, rebase, stash
│   ├── README.md
│   ├── scenario-1-merge-conflict.md
│   ├── scenario-2-rebase-feature.md
│   ├── scenario-3-stash-and-switch.md
│   └── solutions/
├── 03-history-recovery/      ← rewrite history, find & rescue commits
│   ├── README.md
│   ├── scenario-1-interactive-rebase.md
│   ├── scenario-2-bisect.md
│   ├── scenario-3-reflog-recover.md
│   └── solutions/
└── sandbox/                  ← created by setup.py (ignored by git)
```

## ✅ Requirements

- **Git** installed (`git --version`)
- **Python 3.8+** (only used to build the practice repos — `python --version`)

## 🚀 Quick start

```bash
# 1. Get the code
git clone https://github.com/shubhs248/git-scenarios-lab.git
cd git-scenarios-lab

# 2. Build the practice repos (safe to run any time — it rebuilds them fresh)
python setup.py

# 3. Read a scenario, then go into its sandbox repo and try it
cat 02-branching-merging/scenario-1-merge-conflict.md
cd sandbox/merge-conflict
git status
```

> 💡 Made a mess in a sandbox? Just run `python setup.py` again from the lab root to reset everything.

## 🧭 Suggested path (about 90 minutes)

| # | Part | What you practise | Time |
|---|------|-------------------|------|
| 1 | [Git Fundamentals](01-git-fundamentals/README.md) | `init` `add` `commit` `status` `log` `branch` `switch` `undo` | 25 min |
| 2 | [Branching & Merging](02-branching-merging/README.md) | merge conflicts, `rebase`, `stash` | 35 min |
| 3 | [History & Recovery](03-history-recovery/README.md) | interactive `rebase`, `bisect`, `reflog` | 35 min |

## 📝 How each scenario works

1. Read the scenario's `.md` file. It explains **the situation**, **your task**, and **how to check you succeeded**.
2. Go into the matching repo under `sandbox/` and do the work with real Git commands.
3. Stuck? Open the same file name inside that part's `solutions/` folder for the step-by-step commands.
4. Want to try again from scratch? Run `python setup.py` from the lab root.

---

## ⭐ Found this useful?

If this lab helped you, here is how you can support it and help others find it:

- **Star** ⭐ the repo so more people discover it.
- **Fork** 🍴 it and practise on your own copy.
- **Share** 🔗 it on LinkedIn and tag me — I would love to see your progress.
- **Contribute** 🤝 a new scenario or fix. See [CONTRIBUTING.md](CONTRIBUTING.md).

## 👋 About the author

Made with care by **Shubham Sharma**.

- GitHub: [github.com/shubhs248](https://github.com/shubhs248)
- LinkedIn: [linkedin.com/in/shubhs248](https://www.linkedin.com/in/shubhs248)

## 📜 License

MIT — free to use, fork, teach with, and share. A star ⭐ or a tag on LinkedIn is always appreciated!
