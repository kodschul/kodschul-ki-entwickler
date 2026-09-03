# Übung: Erste Schritte mit Claude Code

**Zeit:** ca. 30 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Installation & erster Start (5 min)

```bash
npm install -g @anthropic-ai/claude-code
cd 1205/todo-app
claude
```

Bestätige den Login-Vorgang im Browser, falls es der erste Start ist.

## Aufgabe 2 – Projekt verstehen lassen (10 min)

```
> Gib mir einen kurzen Überblick: Welche Dateien gibt es, was macht die App, wie wird sie gestartet?
```

Beobachte: Welche Tools nutzt Claude, um sich den Überblick zu verschaffen (`Read`, `Glob`, `Grep`)?

## Aufgabe 3 – Kleine Änderung anfordern (10 min)

```
> Füge eine neue Route /health hinzu, die als JSON {"status": "ok"} zurückgibt.
```

Beobachte den Diff, den Claude vorschlägt, bevor du bestätigst.

## Aufgabe 4 – Unterbrechen & wiederholen (5 min)

- Starte eine größere Aufgabe (z. B. "Refactore app.py komplett") und drücke währenddessen `ESC`
- Wiederhole den letzten Prompt mit Pfeiltaste hoch und passe ihn an

---

## Zusammenfassung

- [ ] Claude Code lokal installiert und eingeloggt
- [ ] Projekt-Überblick per Prompt erhalten
- [ ] Kleine Code-Änderung erfolgreich durchgeführt
- [ ] Abbruch mit `ESC` ausprobiert
