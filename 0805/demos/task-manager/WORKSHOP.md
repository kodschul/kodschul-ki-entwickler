# TaskFlow — Claude Code Workshop

Welcome! This project is a deliberately insecure task management web app.
Your job is to explore it, find the bugs, fix them, and automate the review.

---

## Block 1 — Explore the codebase with Claude Code (~20 min)

**Goal:** Understand the project structure before touching any code.

1. Open Claude Code in this directory.
2. Ask Claude: *"Give me a tour of this project. What does each file do?"*
3. Ask Claude: *"What HTTP routes does the app expose and what do they expect?"*
4. Ask Claude: *"What does the database layer look like?"*

**Deliverable:** You should be able to describe the request/response flow
from the browser to the database in one sentence.

---

## Block 2 — Security review with a custom command (~25 min)

**Goal:** Configure and run the `/db-review` slash command.

1. Open `.claude/commands/db-review.md`.
2. Fill in the three `<!-- TODO -->` sections:
   - What Claude should look for (SQL injection patterns).
   - The output format (JSON array of issues).
   - An example output block.
3. Back in Claude Code, run: `/db-review`
4. Claude should identify the **3 security issues** in `db.py`:
   - Line ~26 — f-string SQL injection in `func_get_tasks`
   - Line ~40 — string concatenation SQL injection in `func_create_task`
   - Line ~51 — missing parameterization in `func_delete_task`
5. Copy Claude's output into `review-output.json`.

**Checkpoint:** `review-output.json` contains a non-empty JSON array.

---

## Block 3 — Fix the issues and update CLAUDE.md (~25 min)

**Goal:** Fix all three bugs and add guard-rails to `CLAUDE.md`.

### 3a — Fix `db.py`

For each issue, replace the unsafe query with a parameterized version:

```python
# BEFORE (unsafe)
query = f"SELECT * FROM tasks WHERE status = '{status}'"
conn.execute(query)

# AFTER (safe)
conn.execute("SELECT * FROM tasks WHERE status = ? ORDER BY created_at DESC", (status,))
```

Fix all three methods the same way.

### 3b — Update `CLAUDE.md`

Fill in the `<!-- TODO -->` sections:

- **Stack:** Python 3, Flask, SQLite, TailwindCSS (CDN)
- **Rules:** Add *"Always use parameterized queries. Never build SQL strings with f-strings or concatenation."*
- **Imports / banned patterns:** Add `eval`, `exec`, and raw f-string SQL.

### 3c — Complete `CLAUDE.md` verification

Ask Claude: *"Does this project follow the rules in CLAUDE.md?"*
Claude should now answer "yes" for the fixed file.

---

## Block 4 — Build the review agent (~30 min)

**Goal:** Complete `review_agent.py` so it calls Claude via the SDK and
writes findings to `review-output.json`.

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Export your API key:
   ```bash
   export ANTHROPIC_API_KEY="sk-ant-..."
   ```

3. Open `review_agent.py` and implement each `# TODO` function in order:
   | Function | What to do |
   |---|---|
   | `func_read_file` | `open(filePath).read()` |
   | `func_review_file` | Create client, call `messages.create`, return text |
   | `func_parse_response` | `json.loads(rawResponse)` or extract JSON block |
   | `func_write_output` | `json.dump(findings, f, indent=2)` |
   | `func_main` | Wire `sys.argv[1]` through all four functions |

4. Run it against `db.py`:
   ```bash
   python review_agent.py db.py
   ```

5. Open `review-output.json` — it should list the 3 security issues.

### Bonus — hook

Open `.claude/hooks/post_tool.py` and implement `func_check_risky_patterns`
to detect f-string SQL. Register the hook in Claude Code settings and
observe entries appearing in `security-log.md` as you edit files.

### Bonus — CI

Uncomment the steps in `.github/workflows/ai-review.yml` and add
`ANTHROPIC_API_KEY` as a GitHub Actions secret. The workflow will run
`review_agent.py` on every pull request.

---

## Quick reference

| Command | Purpose |
|---|---|
| `python app.py` | Start the Flask dev server on http://127.0.0.1:5000 |
| `python review_agent.py db.py` | Run the AI review agent |
| `/db-review` (in Claude Code) | Run the custom slash command |

## Files at a glance

| File | Status |
|---|---|
| `app.py` | Complete — read-only for this workshop |
| `db.py` | **Contains 3 bugs — fix in Block 3** |
| `schema.sql` | Complete |
| `templates/index.html` | Complete |
| `CLAUDE.md` | **Skeleton — fill in Block 3b** |
| `.claude/commands/db-review.md` | **Skeleton — fill in Block 2** |
| `.claude/hooks/post_tool.py` | **Skeleton — bonus task** |
| `.github/workflows/ai-review.yml` | **Skeleton — bonus task** |
| `review_agent.py` | **Skeleton — implement in Block 4** |
| `review-output.json` | Written by `review_agent.py` |
| `security-log.md` | Written by the hook |
