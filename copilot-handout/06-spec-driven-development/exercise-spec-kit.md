# Übung: Spec-Kit Prompts

**Zeit:** 13:15 – 15:00 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Die drei Spec-Kit Prompts erstellen (20 min)

**Ziel:** Dreistufigen Spec-Workflow als Custom Prompts umsetzen.

**Erstelle alle drei Prompt-Dateien:**

```bash
mkdir -p .github/prompts
```

**Datei 1:** `.github/prompts/spec-plan.prompt.md`

```markdown
---
mode: ask
description: "Feature analysieren und Implementierungsplan als Spec erstellen"
tools:
  - codebase
---

# Spec Plan

Feature: ${input:featureName}

Analysiere die bestehende Codebase und erstelle specs/${input:featureName}.md mit:

- Ziel (1-2 Sätze)
- Betroffene Dateien (Liste)
- Implementierungsschritte als Checkboxen (- [ ])
- Mindestens 3 Akzeptanzkriterien als Checkboxen

Erstelle NUR die Spec. Keinen Code. Warte auf mein OK.
```

**Datei 2:** `.github/prompts/spec-build.prompt.md`

```markdown
---
mode: agent
description: "Feature nach vorhandener Spec implementieren"
tools:
  - codebase
  - terminal
---

# Spec Build

Spec-Datei: ${input:specFile}

1. Lies #${input:specFile} komplett
2. Implementiere jeden Schritt aus den Implementierungsschritten
3. Hake erledigte Schritte in der Spec ab (- [x])
4. Ändere NUR die in der Spec genannten Dateien
5. Führe danach die Tests aus
```

**Datei 3:** `.github/prompts/spec-test.prompt.md`

```markdown
---
mode: agent
description: "Tests basierend auf Spec-Akzeptanzkriterien generieren"
tools:
  - codebase
  - terminal
---

# Spec Test

Spec-Datei: ${input:specFile}

1. Lies #${input:specFile} – fokussiere auf Akzeptanzkriterien
2. Schreibe für jedes Kriterium mindestens einen Test in test_app.py
3. Nutze das bestehende client-Fixture
4. Führe aus: python -m pytest test_app.py -v
5. Berichte: Grün / Rot
```

---

## Aufgabe 2 – Plan erstellen mit `/spec-plan` (15 min)

**Ziel:** Copilot analysiert die Codebase und erstellt einen Implementierungsplan.

```
/spec-plan
```

Copilot fragt → eingeben: `Notizen für Todos hinzufügen`

Copilot sollte automatisch:

- `app.py` und `templates/` analysieren
- Eine Spec-Datei unter `specs/` erstellen
- Betroffene Dateien, Schritte und Akzeptanzkriterien auflisten

**Prüfen bevor du weitermachst:**

- [ ] Sind alle betroffenen Dateien richtig erkannt?
- [ ] Sind die Implementierungsschritte logisch sortiert?
- [ ] Gibt es mindestens 3 Akzeptanzkriterien?

Falls etwas fehlt – **korrigiere die Spec manuell** bevor du implementierst.

---

## Aufgabe 3 – Implementieren mit `/spec-build` (20 min)

```
/spec-build
```

Copilot fragt nach der Spec-Datei → eingeben: `specs/Notizen für Todos hinzufügen.md`

Beobachte:

- Hakt Copilot Schritte in der Spec-Datei ab?
- Bleibt Copilot im Scope (nur die in der Spec genannten Dateien)?
- Was passiert wenn ein Schritt unklar ist?

**App testen:**

```bash
FLASK_DEBUG=1 python app.py
```

Öffne `http://localhost:5000` – ist das Notiz-Feld sichtbar?

---

## Aufgabe 4 – Tests generieren mit `/spec-test` (15 min)

```
/spec-test
```

Copilot fragt nach der Spec-Datei → eingeben: `specs/Notizen für Todos hinzufügen.md`

Ausführen:

```bash
python -m pytest test_app.py -v --tb=short
```

**Erwartung:** Tests für alle Akzeptanzkriterien aus der Spec. Alle grün.

Falls Tests rot:

```
Ein Test schlägt fehl: [Fehlermeldung hier einfügen].
Liegt der Fehler in der Implementierung oder im Test?
Korrigiere nur was falsch ist.
```

---

## Aufgabe 5 – Vergleich: Spec-Kit vs. manuell (10 min)

Du hast heute beide Wege gemacht:

| Aspekt               | Manuell (Aufgabe 1-4 in exercise.md) | Spec-Kit Prompts (diese Übung)    |
| -------------------- | ------------------------------------ | --------------------------------- |
| **Kontrolle**        | Du schreibst jeden Prompt selbst     | Standardisierter Workflow         |
| **Wiederholbarkeit** | Variiert je nach Formulierung        | Gleicher Ablauf bei jedem Feature |
| **Teamnutzung**      | Jeder formuliert anders              | Geteilte Prompts im Repo          |
| **Flexibilität**     | Beliebig anpassbar                   | Anpassung in `.prompt.md`-Dateien |
| **Einstiegshürde**   | Höher (muss Prompt kennen)           | Niedriger (einfach `/spec-plan`)  |
