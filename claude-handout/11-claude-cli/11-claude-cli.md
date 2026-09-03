# 11 – Claude Code CLI vollständig

**Block:** 90 min | **Tag 4**

---

## Interaktiv vs. Headless

```bash
claude                       # interaktiver REPL-Modus (Modul 02)
claude "Frage..."            # ein Prompt, danach REPL
claude --print "Frage..."    # nur Antwort ausgeben, kein UI – headless
```

**Headless Mode** ist der Claude-Code-Weg für Automatisierung, CI/CD und Skripte – vergleichbar mit `gh copilot suggest`/`explain` bei GitHub Copilot, aber deutlich mächtiger, da Claude Code dabei agentisch arbeiten kann (Dateien lesen/schreiben, Befehle ausführen).

---

## Output-Formate

```bash
# Standard (interaktiv)
claude

# Nur Antwort ausgeben, kein UI
claude --print "Was macht app.py?"

# JSON-Ausgabe (für Skripte)
claude --output-format json --print "Review app.py"

# Streaming JSON
claude --output-format stream-json --print "Review app.py"
```

---

## Headless Mode – für Automation

```bash
# Review als CI-Schritt
claude --print "Führe einen Code-Review von app.py durch. Ausgabe als Markdown." \
  > review-output.md
```

```bash
#!/bin/bash
# review.sh
claude --print \
  "Analysiere app.py auf Sicherheitsprobleme. Ausgabe als JSON-Array mit Feldern: problem, severity, line." \
  --output-format json \
  > review-output.json

echo "Review gespeichert: review-output.json"
```

---

## Wichtige Flags im Überblick

| Flag                     | Zweck                                                  |
| --------------------------- | --------------------------------------------------------- |
| `--print` / `-p`              | Headless: nur Antwort ausgeben, kein interaktives UI       |
| `--output-format`             | `text` (Standard), `json`, `stream-json`                   |
| `--model`                     | Modell für diesen Aufruf überschreiben                     |
| `--add-dir`                   | Zusätzliches Verzeichnis freigeben (wie `/add-dir`)         |
| `--resume` / `--continue`     | Frühere Session fortsetzen                                 |
| `--sandbox`                   | Claude darf nichts ausführen außer explizit Erlaubtem       |

---

## Sandbox Mode – für sensible Umgebungen

```bash
claude --sandbox
```

Nützlich für: Code-Review-Pipelines, öffentliche Umgebungen, Demos – Claude arbeitet dann strikt nach den konfigurierten `permissions` (Modul 05), ohne implizite Zusatzrechte.

---

## Permissions im Headless-Betrieb

Gerade in CI ist **Least Privilege** entscheidend, da niemand interaktiv Rückfragen bestätigen kann:

```json
{
  "permissions": {
    "allow": ["Bash(python -m pytest *)", "Read"],
    "deny": ["Bash(rm *)", "Bash(git push *)", "Write(/etc/*)"]
  }
}
```

---

## Typischer CI-Anwendungsfall

```yaml
# .github/workflows/claude-review.yml (Ausschnitt)
- name: Claude Code Review
  run: |
    claude --print "Review the diff for security and style issues. Output as markdown." \
      --output-format json > review.json
```

> Claude Code lässt sich so in CI/CD-Pipelines einbinden – vergleichbar mit dem Copilot Coding Agent (Modul 14), aber lokal steuerbar über die eigene Pipeline statt über GitHub-eigene Automatisierung.
