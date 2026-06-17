# Part 1 — Git Fundamentals (Warm-up)

## 🎯 Goal
Refresh the everyday Git commands before you tackle the tricky scenarios in parts 2 and 3.

## 🧠 What you practise here
| Command | What it is for |
|---------|----------------|
| `git init` | Start tracking a folder with Git |
| `git status` | See what has changed |
| `git add` | Choose what goes into the next commit |
| `git commit` | Save a snapshot with a message |
| `git log` | See the history of commits |
| `git diff` | See exactly what changed |
| `git branch` / `git switch` | Make and move between branches |
| `.gitignore` | Tell Git to ignore certain files |
| undo commands | Take back a mistake before it spreads |

For this warm-up you make your **own** tiny repo (no sandbox needed). Run each command and watch what happens.

---

## 📝 Tasks
Try each one. The answers are at the bottom.

1. **Start a repo.** Make a new folder `playground`, go into it, and turn it into a Git repo.
2. **First commit.** Create a file `hello.txt` with some text, stage it, and commit it with the message `First commit`.
3. **See the state.** Change `hello.txt`, then check `git status` and `git diff` before committing.
4. **Commit the change.** Stage and commit it with a clear message.
5. **View history.** Show the history as a short one-line-per-commit list.
6. **Make a branch.** Create a branch called `feature` and switch to it.
7. **Commit on the branch.** Add a new file on `feature` and commit it. Then switch back to `main` and notice the file is gone (it lives on the branch).
8. **Ignore a file.** Create a `.gitignore` that ignores `secret.txt`, then create `secret.txt` and confirm Git does not want to track it.
9. **Unstage a file.** Stage a file by mistake, then take it back out of the staging area (without losing your changes).
10. **Undo the last commit but keep the changes.** Move the last commit's changes back into your working area.

---

## ✅ Answers

```bash
# 1. Start a repo
mkdir playground && cd playground
git init

# 2. First commit
echo "Hello Git" > hello.txt
git add hello.txt
git commit -m "First commit"

# 3. See the state
echo "another line" >> hello.txt
git status         # shows hello.txt as modified
git diff           # shows the exact lines added/removed

# 4. Commit the change
git add hello.txt
git commit -m "Add another line to hello.txt"

# 5. View history
git log --oneline

# 6. Make a branch
git switch -c feature      # older Git: git checkout -b feature

# 7. Commit on the branch, then switch back
echo "feature work" > feature.txt
git add feature.txt
git commit -m "Add feature file"
git switch main            # feature.txt is not here - it lives on 'feature'

# 8. Ignore a file
echo "secret.txt" > .gitignore
echo "do not track me" > secret.txt
git status                 # secret.txt does NOT appear as untracked

# 9. Unstage a file (keep the changes)
git add hello.txt
git restore --staged hello.txt    # older Git: git reset HEAD hello.txt

# 10. Undo the last commit but keep the changes
git reset --soft HEAD~1    # the commit is gone, its changes are staged again
```

➡️ When you are comfortable, move on to [Part 2 — Branching & Merging](../02-branching-merging/README.md).

---

## ⭐ Found this useful?
Please **star** ⭐, **fork** 🍴, and **share** 🔗 this repo on LinkedIn so others can use it too. Want to add a task or fix something? See [CONTRIBUTING.md](../CONTRIBUTING.md).

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
