# Bug Finder Skill

## Trigger

Use this skill when the user asks about bugs, errors, or problems in the code — e.g. "Gibt es Fehler im Code?", "Check for bugs", "Was könnte schiefgehen?", "Analysiere den Code auf Probleme".

## Instructions

Analyze the Python code (primarily `app.py`) for the following four categories of issues. For each finding, report the file, line number, category, and a short explanation.

### 1. Unhandled Exceptions

Look for code paths that could raise exceptions without a try/except:

- File I/O (`open`, `json.load`, `json.dump`) without error handling
- Dictionary access with `[]` instead of `.get()` where the key may be absent
- Type conversions (`int()`, `float()`) on user-supplied input without catching `ValueError`
- Any external call that can fail (network, subprocess) without a handler

### 2. Missing Input Validation in Flask Routes

For every `@app.route` that accepts POST data or URL parameters, check:

- Is `request.form.get(...)` used safely, or does missing data cause a crash?
- Are integer/float conversions from form fields wrapped in try/except?
- Are required fields checked for empty strings before use?
- Is the length or content of user input bounded to prevent abuse?

### 3. Hardcoded Values

Search for secrets or environment-specific values baked into the source:

- Passwords, API keys, tokens, or secrets as string literals
- Hardcoded hostnames, IP addresses, or port numbers (e.g. `port=5000` passed to `app.run`)
- Debug flags forced to `True` in production paths (`debug=True`)
- File paths that only work on one machine

### 4. Missing Tests for New Functions

Identify functions or Flask routes that have no corresponding test:

- List all functions/routes defined in the code
- Check whether a `tests/` directory or `test_*.py` file exists and covers them
- Flag any function added without a matching test case

## Output Format

Present findings as a structured list grouped by category. Use this format:

```
### 1. Unbehandelte Exceptions
- app.py:42 — `json.load()` ohne try/except; eine beschädigte todos.json wirft einen ValueError

### 2. Fehlende Input-Validierung
- app.py:27 — POST /add: kein Check ob `title` leer ist, leere Todos werden gespeichert

### 3. Hardcodierte Werte
- app.py:91 — `app.run(debug=True, port=5000)` — Port und Debug-Flag sind hardcodiert

### 4. Fehlende Tests
- Funktion `delete_todo` (app.py:55) hat keinen Test in tests/
```

If a category has no findings, write "Keine Probleme gefunden."

End with a short summary: total number of findings and a recommended priority order for fixing them.
