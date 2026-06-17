# Scenario 3.2 — Find the Bad Commit with `git bisect`

**Sandbox:** `sandbox/bisect`
**You practise:** letting Git binary-search your history to find the commit that broke things.

---

## 📖 The situation
This repo has a tiny calculator in `app.py`. Running it should print `OK`:

```bash
python app.py        # should print: OK
```

But somewhere in the last several commits, someone broke the maths and now it crashes with `AssertionError: math is broken!`. You do not know **which** commit did it. There are 7 commits — checking each by hand is slow.

`git bisect` finds it fast: you tell Git one **good** commit and one **bad** commit, and it checks the middle, then keeps halving the range until it pinpoints the exact commit that introduced the bug.

## 🎯 Your task
Find the first **bad** commit — the one where `python app.py` started failing.

## ✅ How to check you succeeded
- Git prints something like `<hash> is the first bad commit` with the message **`Refactor add()`**.
- After you finish, run `git bisect reset` to return to where you started.

## 💡 Hints

**The check:** a commit is "good" if `python app.py` prints `OK` (exit code 0) and "bad" if it crashes (non-zero exit code).

**Manual way:**
```bash
git bisect start
git bisect bad                 # the current commit (HEAD) is broken
git bisect good HEAD~6         # the oldest commit here still worked
# Git checks out a commit in the middle. Test it:
python app.py                  # then tell Git the result:
git bisect good                # if it printed OK
git bisect bad                 # if it crashed
# repeat until Git names the first bad commit
git bisect reset               # go back to normal when done
```

**Automatic way (let Git run the test for you):**
```bash
git bisect start HEAD HEAD~6   # bad first, then good
git bisect run python app.py   # Git tests each step on its own
git bisect reset
```

> Stuck? See [`solutions/scenario-2-bisect.md`](solutions/scenario-2-bisect.md).
> Want to start over? Run `python setup.py` from the lab root.
