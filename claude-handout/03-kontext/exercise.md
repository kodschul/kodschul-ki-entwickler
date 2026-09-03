# Übung: Kontext bereitstellen

**Zeit:** ca. 30 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – CLAUDE.md schreiben (15 min)

Lege im Projektroot eine `CLAUDE.md` an (falls nicht vorhanden) mit:

- Project Goal (2–3 Sätze)
- Commands (Start, Test)
- Architecture (Datenfluss)
- Mind. 3 Do- und 3 Don't-Regeln

**Prompt zum Ausprobieren:**

```
Erstelle eine CLAUDE.md für dieses Projekt mit den Abschnitten
Project Goal, Commands, Architecture, Do und Don't.
```

## Aufgabe 2 – Kontext-Verhalten beobachten (10 min)

Stelle die gleiche Frage einmal **mit** und einmal **ohne** `CLAUDE.md` (temporär umbenennen):

```
Wie starte ich die Tests für dieses Projekt?
```

Vergleiche die Antworten – wie stark hilft der automatische Kontext?

## Aufgabe 3 – Verzeichnis erweitern (5 min)

```
/add-dir ../../ai-rules
```

```
Welche Style-Konventionen aus ai-rules/styles-guide.md sollte ich hier anwenden?
```

---

## Zusammenfassung

- [ ] `CLAUDE.md` mit allen vier Abschnitten angelegt
- [ ] Unterschied mit/ohne `CLAUDE.md` beobachtet
- [ ] Zusätzliches Verzeichnis per `/add-dir` eingebunden
