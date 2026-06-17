# 🤝 Contributing

Thanks for thinking about helping out! This is a learning project, so contributions of every size are welcome — even fixing a typo.

If this repo helped you, the easiest way to support it is to **star** ⭐ it, **fork** 🍴 it, and **share** 🔗 it on LinkedIn so others can find it too.

## Ways you can help

- **Fix something** — a typo, a broken link, or a scenario that does not build.
- **Add a new scenario** — more practice on tags, submodules, `worktree`, `revert`, partial staging, etc.
- **Improve the wording** — make an explanation clearer or simpler.
- **Improve `setup.py`** — make the practice repos even more realistic.

## How to contribute (step by step)

1. **Fork** this repo to your own GitHub account (use the "Fork" button at the top).
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/git-scenarios-lab.git
   cd git-scenarios-lab
   ```
3. **Create a branch** for your change:
   ```bash
   git switch -c add-revert-scenario
   ```
4. **Make your change** and test it (see the checklist below).
5. **Commit** with a short, clear message:
   ```bash
   git add .
   git commit -m "Add a scenario on git revert"
   ```
6. **Push** your branch and open a **Pull Request**:
   ```bash
   git push -u origin add-revert-scenario
   ```

## Adding a new scenario

Keep the same simple style so the lab stays easy to follow:

1. **Build the starting state** in `setup.py`: add a `build_<name>()` function that creates
   `sandbox/<name>` in the state your scenario needs, and add it to the `SCENARIOS` list.
2. **Write the brief**: add `scenario-N-<name>.md` in the right part folder with these sections:
   - **The situation** — what state the repo is in and why.
   - **Your task** — what the learner must achieve.
   - **How to check you succeeded** — clear, testable success signs.
   - **Hints** — a few nudges, not the full answer.
3. **Write the answer**: add the same file name under that part's `solutions/` folder with the exact commands.
4. Use plain, simple English throughout.

## Checklist before you open a PR

- [ ] `python setup.py` runs cleanly and builds your new sandbox.
- [ ] You followed your own solution end-to-end and it works.
- [ ] The success checks in the scenario actually pass after the solution.
- [ ] Instructions use plain, simple English.
- [ ] If you added a new part, you linked it from the main `README.md`.

## Code of conduct

Be kind and helpful. This is a place for people to learn, so assume good intent and keep feedback friendly.

---

Made by **Shubham Sharma** · [GitHub](https://github.com/shubhs248) · [LinkedIn](https://www.linkedin.com/in/shubhs248)
