# Solution — Scenario 3.2 Find the Bad Commit with `git bisect`

## Automatic way (recommended)

```bash
cd sandbox/bisect

# Tell Git: HEAD is bad, the commit 6 back is good
git bisect start HEAD HEAD~6

# Let Git run the test at each step. python app.py exits 0 when good, non-zero when bad.
git bisect run python app.py
#   ...
#   <hash> is the first bad commit
#       Refactor add()

# Always finish by returning to where you started
git bisect reset
```

## Manual way (to feel how it works)

```bash
cd sandbox/bisect

git bisect start
git bisect bad                 # current commit is broken
git bisect good HEAD~6         # the oldest commit here worked

# Git checks out a commit in the middle. Test it:
python app.py
#   - if it prints OK:           git bisect good
#   - if it crashes (AssertionError):  git bisect bad

# Repeat the test + good/bad until Git announces:
#   <hash> is the first bad commit  ->  "Refactor add()"

git bisect reset               # back to normal
```

### What happened
`git bisect` does a binary search through history. With 7 commits it only needs about 3 tests instead of checking all of them. The culprit here is the **`Refactor add()`** commit, where `return a + b` was changed to `return a - b`, which makes the built-in check in `app.py` fail.

### Tip
`git bisect run <command>` works with any command that returns 0 for "good" and non-zero for "bad" — a test suite, a script, a linter, anything. That makes finding regressions almost automatic.
