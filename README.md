# ChatGPT Codex: AI-Powered Coding, sample lesson + course outline

A sample from a proposed hands-on course on ChatGPT Codex. Everything here is real: the starter code was committed with a bug, Codex fixed it and wrote the tests, and the commit history shows each step.

## Sample lesson: "Debug, fix and test with Codex" (Module 3, Lesson 2)

**The setup.** `invoices.py` totals unpaid invoices from a CSV. Run it on the sample data and it crashes:

```
ValueError: invalid literal for int() with base 10: '1200.50'
```

**The prompt we give Codex** (from the terminal, `codex exec`, sandboxed to this folder):

> Running invoices.py crashes. Find the root cause and fix it. Requirements: amounts can have cents (use Decimal, not float), status matching must be case-insensitive, a row with a blank amount must be skipped with a warning instead of crashing. Then add pytest tests in test_invoices.py covering each of those cases, run them, and make sure they pass. Keep the code minimal.

**What the lesson teaches with it**
1. Write the prompt like a ticket: the symptom, the requirements, and how you'll know it's done (tests pass).
2. Name the hidden traps yourself. "Use Decimal, not float" is there because float money math is a classic silent bug that an AI fix can introduce.
3. Read the diff before you trust it: 8 lines added, 3 removed, in `invoices.py`.
4. Run the tests yourself. Don't take "6 tests passed" on faith: `pytest -q` → `6 passed`.
5. Check the result against the data by hand: 1200.50 + 450.25 = **1650.75**. Globex is paid and Umbrella has a blank amount, so neither counts.

**Try it**
```bash
git log --oneline          # starter commit, then the Codex fix
git show $(git rev-list --max-parents=0 HEAD):invoices.py  # the buggy starter
python invoices.py         # 1650.75
pytest -q                  # 6 passed
```

## Proposed course outline

1. **Introduction to Codex and AI-powered coding:** what Codex is (CLI, IDE extension, cloud tasks), where it fits next to your editor, and what it should never do unsupervised.
2. **Setup and workflow:** install, sign in, sandbox and approval modes, `AGENTS.md` project instructions, choosing a model.
3. **Generate, explain, debug, refactor:** prompting like a ticket, reading diffs, the sample lesson above, refactoring safely behind tests.
4. **Real codebases:** exploring an unfamiliar multi-file repo, making a scoped change across files, working on branches, keeping Codex inside the task.
5. **Tests, reviews and docs:** test-first prompts, Codex as a code reviewer on a pull request, generating and checking documentation.
6. **Project 1, a full-stack app:** a small Next.js + API app built end to end with Codex, deployed.
7. **Project 2, a Python automation:** a data pipeline with tests and CI, built and maintained with Codex.
8. **Productivity, limits and security:** secrets, dependency risk, prompt injection in repos, when to stop and write it yourself, a review checklist for AI-written code.

Every module ships with starter code, a solution branch and exercises.
