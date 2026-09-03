# 06 – Skills & CLAUDE.md-Vertiefung

**Block:** 90 min | **Tag 3**

---

## Zwei Wege, Claude Wissen mitzugeben

| Mechanismus                | Für was                                                      |
| ----------------------------- | ----------------------------------------------------------------- |
| **`CLAUDE.md` (verschachtelt)** | Kontext/Regeln, die **immer** gelten – ggf. nur für einen Unterordner |
| **`SKILL.md`**                 | Eine **Fähigkeit für eine bestimmte Aufgabe**, die situativ aktiviert wird |

---

## Verschachtelte CLAUDE.md-Dateien (Scoping)

Claude Code liest nicht nur die `CLAUDE.md` im Projektroot, sondern auch `CLAUDE.md`-Dateien in Unterordnern, sobald in diesem Bereich gearbeitet wird – das Äquivalent zu pfadgebundenen `.instructions.md`-Dateien bei GitHub Copilot.

```
mein-projekt/
├── CLAUDE.md                    ← gilt projektweit
├── backend/
│   └── CLAUDE.md                ← gilt zusätzlich nur für backend/
└── frontend/
    └── CLAUDE.md                ← gilt zusätzlich nur für frontend/
```

**Beispiel `backend/CLAUDE.md`:**

```markdown
# Backend-Konventionen

## Do

- Alle Routen in app.py, keine Blueprints (Projektgröße rechtfertigt das nicht)
- Fehler als JSON mit `{"error": "..."}` zurückgeben

## Don't

- Keine synchronen DB-Calls in Request-Handlern über 200ms
```

> Root-`CLAUDE.md` bleibt kurz und allgemein, Details wandern in die jeweiligen Unterordner – das hält den Kontext klein (Modul 10).

---

## SKILL.md – wiederverwendbare Skills

Ein Skill ist eine **Anleitung für eine bestimmte Aufgabe**, die Claude über die `description` automatisch erkennt und aktiviert – das Konzept der Agent Skills wurde ursprünglich für Claude Code entwickelt und mittlerweile auch von anderen Tools übernommen (siehe Modul 14).

**Datei:** `.claude/skills/<name>/SKILL.md`

```markdown
---
name: feature-builder
description: Use when building a new feature in the app
---

- Denke an 3 mögliche Umsetzungsstrategien und frage den Nutzer,
  welche er bevorzugt, bevor du anfängst
- Nach der Implementierung schreibe Tests, um das Feature zu prüfen
```

```markdown
---
name: api-designer
description: Use when designing a new API for the app
---

- Nutze REST-API Prinzipien
- Swagger für Dokumentation und Tests einbinden
- Statisches Bearer-Token für Authentifizierung
```

**Skill aufrufen:** Einfach in der Konversation beschreiben, was getan werden soll – Claude erkennt den passenden Skill über die `description`.

---

## Warum / Wann nicht?

| Warum nutzen                                   | Wann nicht                                        |
| -------------------------------------------------- | ------------------------------------------------------ |
| Wiederkehrende Aufgabe soll immer gleich ablaufen    | Einmalige Aufgabe → direkt beschreiben                 |
| Unterordner braucht eigene Konventionen              | Ganzes Projekt hat einheitliche Regeln → reicht Root-`CLAUDE.md` |
| Team-Wissen versionierbar im Repo ablegen            | Sensible Daten → gehören nie in Skills/CLAUDE.md        |
| Zu viele/lange Instructions im Root                  | Zu viele Skills (>10) → Claude wird ungenau, Auswahl wird unklar |

---

## Vergleich: CLAUDE.md vs. SKILL.md

|                     | `CLAUDE.md`                        | `SKILL.md`                              |
| --------------------- | ------------------------------------- | ------------------------------------------ |
| **Aktivierung**        | Immer (root) bzw. bei Arbeit im Ordner | Situativ, wenn `description` passt         |
| **Inhalt**             | Projekt-/Bereichskontext, Regeln       | Konkreter Workflow für eine Aufgabenart     |
| **Umfang**             | Kurz, grundsätzlich                    | Kann detaillierter/länger sein              |
| **Ort**                | Projektroot + Unterordner              | `.claude/skills/<name>/SKILL.md`            |
