# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Stack

- **Backend:** Flask (Python) + SQLite
- **Frontend:** Server-side rendered HTML via Jinja2 (`templates/index.html`)
- **AI tooling:** Anthropic SDK (`review_agent.py`)

## Run

```bash
pip install -r requirements.txt
python app.py
```

## Key files

| File              | Purpose                                 |
| ----------------- | --------------------------------------- |
| `app.py`          | Flask routes                            |
| `db.py`           | All DB queries via `DbManager` class    |
| `schema.sql`      | SQLite schema, applied once at startup  |
| `review_agent.py` | Standalone AI-powered code review agent |

## Architecture

`app.py` instantiates a single `DbManager` at module level and delegates all persistence to it. Routes return either rendered HTML (GET `/tasks`) or JSON (POST/DELETE). The DB is initialized lazily via `dbManager.func_init_db()` on first run, which executes `schema.sql`.

`review_agent.py` is independent of the Flask app — it uses the Anthropic SDK to review code and writes output to `review-output.json`.

## Known issues

`db.py` contains **intentional SQL injection vulnerabilities** (documented inline) for workshop/training purposes. All three `DbManager` methods use string interpolation instead of parameterized queries. Do not deploy this app.
lnerabilities.

## Custom slash commands

- `/db-review` — runs a security review of `db.py` (defined in `.claude/commands/db-review.md`)
