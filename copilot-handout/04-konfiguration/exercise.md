# Übung: Konfiguration

**Zeit:** 60 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – copilot-instructions.md erstellen (20 min)

```bash
mkdir -p .github
```

Erstelle `.github/copilot-instructions.md`:

```
Erstelle eine .github/copilot-instructions.md für diese Todo-App.
Halte sie unter 80 Zeilen. Enthalte:
- Project Goal (1 Satz)
- Stack (Flask, Jinja2, Tailwind CDN, pytest, todos.json)
- Commands (Start + Test)
- Architecture (Request → app.py → todos.json → Template, 3 Sätze)
- Do (5 Regeln)
- Don't (5 Regeln)
```

Prüfe: Unter 80 Zeilen?

```bash
wc -l .github/copilot-instructions.md
```

---

## Aufgabe 2 – .vscode/settings.json konfigurieren (20 min)

Erstelle `.vscode/settings.json`:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/instructions/python.instructions.md" }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze pytest. Immer happy path + edge case. Kommentare auf Deutsch."
    }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": ".github/instructions/security.instructions.md" }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    {
      "text": "Englisch. Format: type(scope): message. Typen: feat/fix/docs/test/chore."
    }
  ],
  "github.copilot.enable": {
    "*": true,
    "markdown": false
  },
  "github.copilot.chat.localeOverride": "de"
}
```

**Testen:** Öffne Copilot Chat → tippe eine einfache Code-Frage.  
Antwortet Copilot auf Deutsch?

---

## Aufgabe 3 – Commit-Message Generator (10 min)

1. Ändere eine Kleinigkeit in `app.py` (z.B. Kommentar)
2. Öffne Source Control Panel (`⌃ ⇧ G` / `Ctrl Shift G`)
3. Klicke auf das **Zauberstab-Icon** neben dem Commit-Eingabefeld
4. Prüfe: Folgt die generierte Message dem Format `type(scope): message`?

---

## Aufgabe 4 – Reflektion: Was gehört wo? (10 min)

Entscheide für jede Regel wo sie hin gehört:

| Regel                                  | copilot-instructions.md | .instructions.md | .vscode/settings.json |
| -------------------------------------- | ----------------------- | ---------------- | --------------------- |
| "Keine Datenbank nutzen"               |                         |                  |                       |
| "Typ-Annotationen für alle Funktionen" |                         |                  |                       |
| "Tests mit pytest schreiben"           |                         |                  |                       |
| "Commit-Messages auf Englisch"         |                         |                  |                       |
| "App mit FLASK_DEBUG=1 starten"        |                         |                  |                       |
| "Antworten auf Deutsch"                |                         |                  |                       |
