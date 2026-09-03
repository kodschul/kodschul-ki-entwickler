# 14c – Plan Mode

**Seit wann:** Im Laufe von 2025 als eigener Modus in Claude Code eingeführt (umschaltbar während der Session, z. B. per Tastenkürzel/Modus-Wechsel je nach Version).

> Genauen Aktivierungsweg gegen `/help` bzw. die aktuelle Dokumentation der installierten Version prüfen.

---

## Was ist neu?

Im **Plan Mode** arbeitet Claude zunächst **rein lesend**: Es analysiert die Aufgabe und die Codebase und erstellt einen Plan, **ohne** Dateien zu verändern oder Befehle mit Seiteneffekten auszuführen. Erst nach Bestätigung des Plans wechselt Claude in den normalen, ausführenden Modus.

```
Plan Mode:  Aufgabe → Analyse (nur Read/Grep/Glob) → Plan zur Bestätigung
Normal Mode: Plan bestätigt → Claude implementiert, testet, ändert Dateien
```

## Warum wichtig?

- Ergänzt Spec-Driven Development (Modul 12): Plan Mode ist der informelle, schnelle Weg für kleinere Aufgaben, das Spec-Kit (`/spec plan`) der formalere Weg für größere Features
- Reduziert das Risiko unerwünschter Änderungen, weil der Plan **vor** jeder Datei-Änderung sichtbar ist

## Abgrenzung zu Spec-Kit

| Plan Mode                            | Spec-Kit (`/spec plan`, Modul 12)     |
| ----------------------------------------- | ------------------------------------------ |
| Informeller, schneller Plan-Schritt          | Formale `SPEC.md` mit Checkboxen             |
| Gut für spontane, mittelgroße Aufgaben        | Gut für Team-Workflows, nachvollziehbare Historie |
| Kein persistentes Artefakt im Repo            | Persistente Spec-Datei im Repo                |
