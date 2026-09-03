# Spec-Kit mit Custom Prompt

**Block:** 13:15 – 15:00 Uhr

---

## Was ist das Spec-Kit?

Das Spec-Kit ist ein **Custom Prompt in GitHub Copilot** für strukturiertes, dreistufiges Entwickeln – ein direktes Äquivalent zum `/spec`-Workflow in Claude Code:

```
/spec-plan   → Copilot erstellt einen Plan aus deiner Anforderung
/spec-build  → Copilot implementiert nach dem Plan
/spec-test   → Copilot schreibt Tests gegen den Plan
```

> Kein freies Improvisieren. Copilot folgt dem Plan – nicht seiner eigenen Interpretation.

---

## Wie funktioniert das unter der Haube?

```
Nutzer: /spec-plan "Fälligkeitsdatum für Todos"
  → Copilot analysiert Codebase (#codebase)
  → Erstellt SPEC.md mit: Änderungen, Dateien, Schritte
  → Wartet auf Bestätigung

Nutzer: /spec-build
  → Copilot liest SPEC.md (#specs/...)
  → Implementiert Schritt für Schritt
  → Hakt Schritte in SPEC.md ab

Nutzer: /spec-test
  → Copilot liest SPEC.md (Akzeptanzkriterien)
  → Schreibt Tests nur für das was in der Spec steht
```

**Wichtig:** Copilot verändert während `/spec-build` nichts außerhalb der in der Spec definierten Dateien.

---

## Warum / Wann nicht?

| Warum nutzen                             | Wann nicht                                    |
| ---------------------------------------- | --------------------------------------------- |
| Reproduzierbarer Workflow im Team        | Schneller Bugfix → direkt tippen              |
| Copilot bleibt im Scope                  | Explorativer Prototyp → Spec zu früh          |
| Plan vor Code sichtbar + bestätigbar     | Feature ändert sich noch → Spec wird veraltet |
| Tests aus Akzeptanzkriterien generierbar | Einmalige Migration / Skript                  |

---

## Die drei Prompt-Dateien

### `/spec-plan` – Plan erstellen

**`.github/prompts/spec-plan.prompt.md`**

```markdown
---
mode: ask
description: "Feature analysieren und Implementierungsplan erstellen"
tools:
  - codebase
---

# Spec Plan

Feature: ${input:featureName}

Analysiere die bestehende Codebase und erstelle specs/${input:featureName}.md mit:

## Inhalt der Spec-Datei

- **Ziel:** Was soll das Feature können?
- **Betroffene Dateien:** Liste aller Dateien die geändert werden müssen
- **Implementierungsschritte:** Als Checkboxen `- [ ]`
- **Akzeptanzkriterien:** Mindestens 3 testbare Kriterien als Checkboxen

Erstelle NUR die Spec-Datei. Keinen Code. Warte auf mein OK.
```

---

### `/spec-build` – Implementieren

**`.github/prompts/spec-build.prompt.md`**

```markdown
---
mode: agent
description: "Feature nach vorhandener Spec implementieren"
tools:
  - codebase
  - terminal
---

# Spec Build

Welche Spec-Datei soll implementiert werden? ${input:specFile}

1. Lies #${input:specFile} komplett
2. Implementiere jeden Schritt aus den Implementierungsschritten
3. Hake jeden erledigten Schritt in der Spec-Datei ab (`- [x]`)
4. Ändere NUR die in der Spec genannten Dateien
5. Informiere mich wenn ein Schritt unklar ist

Nach Abschluss: Führe die Tests aus und berichte das Ergebnis.
```

---

### `/spec-test` – Tests generieren

**`.github/prompts/spec-test.prompt.md`**

```markdown
---
mode: agent
description: "Tests basierend auf Spec-Akzeptanzkriterien generieren"
tools:
  - codebase
  - terminal
---

# Spec Test

Welche Spec-Datei soll getestet werden? ${input:specFile}

1. Lies #${input:specFile} – fokussiere auf die Akzeptanzkriterien
2. Lies test_app.py – nutze das bestehende client-Fixture
3. Schreibe für jedes Akzeptanzkriterium mindestens einen Test
4. Schreibe nur in test_app.py
5. Führe die Tests aus: `python -m pytest test_app.py -v`
6. Berichte: Wie viele Tests grün, wie viele rot?
```

---

## SPEC.md – Aufbau

Copilot erzeugt beim `/spec-plan` automatisch eine Datei in diesem Format:

```markdown
# Spec: Fälligkeitsdatum für Todos

## Ziel

Todos können ein optionales Fälligkeitsdatum bekommen.
Überfällige Todos werden rot markiert.

## Betroffene Dateien

- `app.py` – Routen /add und / anpassen
- `templates/index.html` – Datum anzeigen, rot markieren
- `test_app.py` – neue Tests hinzufügen

## Implementierungsschritte

- [ ] Feld `due_date` in /add-Route entgegennehmen
- [ ] Feld `due_date` in todos.json speichern
- [ ] Template: Datum-Eingabe im Formular
- [ ] Template: Datum in der Liste anzeigen
- [ ] Template: Rote Markierung wenn Datum < heute

## Akzeptanzkriterien

- [ ] Todo mit Datum speicherbar
- [ ] Todo ohne Datum funktioniert weiterhin
- [ ] Überfälliges Todo visuell hervorgehoben
- [ ] Datum korrekt in todos.json gespeichert
```
