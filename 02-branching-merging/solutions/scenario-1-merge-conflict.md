# Solution — Scenario 2.1 Resolve a Merge Conflict

```bash
cd sandbox/merge-conflict

# 1. Start the merge — Git stops with a conflict in greeting.txt
git merge feature
#   ...
#   CONFLICT (content): Merge conflict in greeting.txt
#   Automatic merge failed; fix conflicts and then commit the result.

# 2. Look at the conflict
git status
cat greeting.txt
#   <<<<<<< HEAD
#   Hello, Team!
#   =======
#   Hello, DevOps!
#   >>>>>>> feature
```

Edit `greeting.txt` so it contains only the final text you want, with no markers:

```
Hello, DevOps Team!
```

```bash
# 3. Mark it resolved and finish the merge
git add greeting.txt
git commit --no-edit          # keeps the default merge message

# 4. Confirm
git status                     # clean
git log --oneline --graph     # shows a merge commit joining main + feature
```

### What happened
A conflict means two branches changed the same lines and Git will not guess which to keep. The `<<<<<<<` / `=======` / `>>>>>>>` markers show both versions; you decide the result, remove the markers, `add`, and `commit`.

### Handy escape hatch
If you want to cancel and try again: `git merge --abort` (then `python setup.py` to fully reset).
