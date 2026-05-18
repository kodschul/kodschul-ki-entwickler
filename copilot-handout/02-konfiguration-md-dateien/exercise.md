# Übung: Konfiguration & .md-Dateien

**Zeit:** 09:15 – 10:30 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – copilot-instructions.md erstellen (15 min)

Erstelle die Datei `.github/copilot-instructions.md` im Projektroot der Todo-App.  
Sie soll Copilot beim Start jeder Chat-Session vollständigen Kontext geben.

**Ziel:** Copilot soll nach dem Lesen wissen:

- Was diese App tut
- Wie sie gestartet und getestet wird
- Welche Patterns verwendet werden
- Was sie NICHT tun soll

**Prompt zum Ausprobieren (in Copilot Chat):**

```
Erstelle eine .github/copilot-instructions.md Datei für diese Todo-App, sodass:
- Der Projektkontext in 2-3 Sätzen klar ist
- Alle wichtigen Befehle (start, test) eingetragen sind
- Mindestens 5 Do-Regeln und 5 Don't-Regeln vorhanden sind
- Ein Abschnitt "Architecture" erklärt wie Daten fließen (Request → app.py → todos.json → Template)
```

**Erwartetes Ergebnis:** `.github/copilot-instructions.md` mit vollständigen Abschnitten

---

## Aufgabe 2 – Eigene Instruction-Datei schreiben (20 min)

Wir brauchen eine neue Instruction: **`security.instructions.md`**  
Sie soll Copilot anweisen, Code auf typische Python-Sicherheitsprobleme zu prüfen.

**Ziel:** Datei `.github/instructions/security.instructions.md` erstellen

**Manuell erstellen – Vorlage:**

```markdown
---
applyTo: "**/*.py"
description: "Security review guidelines for Python code"
---

# Security Guidelines

Prüfe den Code auf folgende Probleme:

- [HIER EINTRAGEN: Regel 1]
- [HIER EINTRAGEN: Regel 2]
- [HIER EINTRAGEN: Regel 3]
```

**Oder per Prompt:**

```
Erstelle eine neue Instruction-Datei unter .github/instructions/security.instructions.md.
Die Instruction soll Copilot anweisen, Python-Code zu analysieren und auf folgende Probleme zu prüfen:
- Unbehandelte Exceptions
- Fehlende Input-Validierung bei Flask-Routen
- Hardcodierte Werte (Passwörter, Tokens, Ports)
- Fehlende Tests für neue Funktionen
Setze applyTo auf alle Python-Dateien.
```

**Erwartetes Ergebnis:** `.github/instructions/security.instructions.md`

---

## Aufgabe 3 – .vscode/settings.json konfigurieren (15 min)

Verbinde die Instruction-Dateien mit den richtigen Copilot-Einstellungen.

**Erstelle oder erweitere** `.vscode/settings.json`:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "file": ".github/instructions/python.instructions.md"
    }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze pytest. Schreibe immer happy path und edge case Tests."
    }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    {
      "file": ".github/instructions/security.instructions.md"
    }
  ]
}
```

**Oder per Prompt:**

```
Erstelle eine .vscode/settings.json Datei, die folgende Copilot-Einstellungen enthält:
- Für Code-Generierung: die python.instructions.md laden
- Für Test-Generierung: pytest verwenden, immer happy path und edge case
- Für Code-Review: die security.instructions.md laden
```

**Testen:**  
Öffne eine Python-Datei, starte Copilot Chat und schreibe: `Erstelle einen Test für die /add-Route`  
Beobachte: Nutzt Copilot die eingetragenen Einstellungen?

---

## Aufgabe 4 – gh copilot CLI ausprobieren (10 min)

```bash
# Copilot CLI installieren (falls noch nicht vorhanden)
gh extension install github/gh-copilot

# Einen Befehl für das Starten der App vorschlagen lassen
gh copilot suggest "Flask Development-Server mit Debug-Modus starten"

# Den pytest-Befehl erklären lassen
gh copilot explain "python -m pytest test_app.py -v --tb=short"
```

**Fragen zum Nachdenken:**

- Was schlägt Copilot CLI vor?
- Ist der Vorschlag korrekt für unsere App?
- Wo unterscheidet sich `gh copilot suggest` von Copilot Chat im Editor?
