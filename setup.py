#!/usr/bin/env python3
"""
setup.py - builds the Git practice repos for this lab.

It creates a fresh repo for each scenario inside the sandbox/ folder, each one
already in the state the scenario needs. Run it any time to reset everything:

    python setup.py

Nothing here touches your real projects - every repo lives under sandbox/,
which is ignored by git and rebuilt from scratch on each run.

Requirements: Git and Python 3.8+.
"""
from __future__ import annotations

import shutil
import stat
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SANDBOX = ROOT / "sandbox"


# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------
def git(repo: Path, *args: str) -> str:
    """Run a git command inside `repo` and return its output."""
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"git {' '.join(args)} failed in {repo}:\n{result.stderr.strip()}"
        )
    return result.stdout.strip()


def new_repo(name: str) -> Path:
    """Create an empty git repo at sandbox/<name> with a local identity."""
    repo = SANDBOX / name
    repo.mkdir(parents=True, exist_ok=True)
    # Use 'main' as the default branch on every git version.
    subprocess.run(["git", "init", "-q"], cwd=repo, check=True)
    git(repo, "symbolic-ref", "HEAD", "refs/heads/main")
    # Local settings so commits work even without a global git config.
    git(repo, "config", "user.name", "Practice Learner")
    git(repo, "config", "user.email", "learner@example.com")
    git(repo, "config", "commit.gpgsign", "false")
    git(repo, "config", "core.autocrlf", "false")
    return repo


def write(repo: Path, filename: str, content: str) -> None:
    (repo / filename).write_text(content, encoding="utf-8")


def commit_all(repo: Path, message: str) -> None:
    git(repo, "add", "-A")
    git(repo, "commit", "-q", "-m", message)


def _force_remove(func, path, _exc):
    """Helper so shutil.rmtree can delete read-only .git files on Windows."""
    import os
    os.chmod(path, stat.S_IWRITE)
    func(path)


def reset_sandbox() -> None:
    if SANDBOX.exists():
        shutil.rmtree(SANDBOX, onerror=_force_remove)
    SANDBOX.mkdir(parents=True, exist_ok=True)


# ---------------------------------------------------------------------------
# Part 2 - branching & merging
# ---------------------------------------------------------------------------
def build_merge_conflict() -> None:
    repo = new_repo("merge-conflict")
    write(repo, "greeting.txt", "Hello, world!\n")
    commit_all(repo, "Add greeting")

    # A feature branch changes the greeting line.
    git(repo, "switch", "-c", "feature")
    write(repo, "greeting.txt", "Hello, DevOps!\n")
    commit_all(repo, "Make greeting say DevOps")

    # Meanwhile main changes the SAME line a different way.
    git(repo, "switch", "main")
    write(repo, "greeting.txt", "Hello, Team!\n")
    commit_all(repo, "Make greeting say Team")
    # Learner is left on main; merging 'feature' will conflict on greeting.txt.


def build_rebase_feature() -> None:
    repo = new_repo("rebase-feature")
    write(repo, "app.txt", "version 1\n")
    commit_all(repo, "Initial app")

    # feature branches off here and adds its own file.
    git(repo, "switch", "-c", "feature")
    write(repo, "feature.txt", "shiny new feature\n")
    commit_all(repo, "Add shiny feature")

    # main moves ahead with an unrelated change.
    git(repo, "switch", "main")
    write(repo, "app.txt", "version 2\n")
    commit_all(repo, "Update app to version 2")

    # Leave the learner on feature, one commit behind main.
    git(repo, "switch", "feature")


def build_stash_and_switch() -> None:
    repo = new_repo("stash-and-switch")
    write(repo, "notes.txt", "Project notes\n")
    commit_all(repo, "Add notes")

    # Another branch exists for the learner to switch to later.
    git(repo, "branch", "release")

    # Leave UNCOMMITTED changes in the working tree on main.
    write(repo, "notes.txt", "Project notes\nWIP: still editing this...\n")
    # (no commit on purpose - the working tree is dirty)


# ---------------------------------------------------------------------------
# Part 3 - history & recovery
# ---------------------------------------------------------------------------
def build_interactive_rebase() -> None:
    repo = new_repo("interactive-rebase")
    write(repo, "login.py", "def login():\n    return True\n")
    commit_all(repo, "Add login feature")

    write(repo, "login.py", "def login():\n    return True  # noqa\n")
    commit_all(repo, "wip")

    write(repo, "login.py", "def login():\n    return True  # fixed\n")
    commit_all(repo, "fix tpyo")

    write(repo, "login.py", "def login():\n    return True  # final\n")
    commit_all(repo, "more wip")
    # Learner squashes the last 3 messy commits into one clean commit.


def build_bisect() -> None:
    repo = new_repo("bisect")

    good_app = (
        "def add(a, b):\n"
        "    return a + b\n\n"
        'if __name__ == "__main__":\n'
        '    assert add(2, 3) == 5, "math is broken!"\n'
        '    print("OK")\n'
    )
    bad_app = good_app.replace("return a + b", "return a - b")

    # A run of healthy commits.
    write(repo, "app.py", good_app)
    commit_all(repo, "Add calculator")
    write(repo, "README.md", "# Calculator\n")
    commit_all(repo, "Add README")
    write(repo, "README.md", "# Calculator\n\nA tiny adder.\n")
    commit_all(repo, "Describe the project")

    # The commit that introduces the bug.
    write(repo, "app.py", bad_app)
    commit_all(repo, "Refactor add()")

    # More commits on top, so the bug is buried in history.
    write(repo, "README.md", "# Calculator\n\nA tiny adder.\n\n## Usage\n")
    commit_all(repo, "Add usage section")
    write(repo, "app.py", bad_app + "# end of file\n")
    commit_all(repo, "Tidy file end")
    write(repo, "VERSION", "1.0.0\n")
    commit_all(repo, "Bump version")
    # Learner uses bisect to find "Refactor add()" as the bad commit.


def build_reflog_recover() -> None:
    repo = new_repo("reflog-recover")
    write(repo, "work.txt", "Starting the project.\n")
    commit_all(repo, "Add project")

    # An important commit...
    write(repo, "work.txt", "Starting the project.\nIMPORTANT: the secret sauce.\n")
    commit_all(repo, "Add the important feature")

    # ...that gets "lost" by an accidental hard reset.
    git(repo, "reset", "--hard", "HEAD~1")
    # The commit is gone from the branch but still findable via the reflog.


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
SCENARIOS = [
    ("merge-conflict", build_merge_conflict),
    ("rebase-feature", build_rebase_feature),
    ("stash-and-switch", build_stash_and_switch),
    ("interactive-rebase", build_interactive_rebase),
    ("bisect", build_bisect),
    ("reflog-recover", build_reflog_recover),
]


def main() -> None:
    # Make sure git exists before we start.
    try:
        subprocess.run(["git", "--version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("ERROR: Git is not installed or not on your PATH.")
        sys.exit(1)

    print("==> Git Scenarios Lab - building practice repos")
    reset_sandbox()

    for name, builder in SCENARIOS:
        builder()
        print(f"    built sandbox/{name}")

    print()
    print(f"Done. {len(SCENARIOS)} practice repos are ready under sandbox/.")
    print("Start with:")
    print("    cat 02-branching-merging/scenario-1-merge-conflict.md")
    print("    cd sandbox/merge-conflict")


if __name__ == "__main__":
    main()
