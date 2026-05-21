# Exercise: Hooks - Automatische Folgeaktionen einrichten

## Ziel

Du richtest automatische Ablaeufe ein, die ohne dein Zutun starten.
Kein Code - nur Beschreibungen.

---

## Aufgabe 1: Review-Hook anlegen

```text
Erstelle `.claude/hooks/notify-review.md`.
Dieser Hook soll automatisch passieren, sobald ein Angebot erstellt wurde.
Dann soll:
1. Der Status auf 'Wartet auf Pruefung' gesetzt werden.
2. Ein Pruefauftrag mit aktuellem Datum erstellt werden.
3. Ein Hinweis in der App erscheinen: 'Angebot bereit zur Pruefung'.
Fehlerfall: Wenn keine Angebots-ID vorhanden, Fehler aufzeichnen und stoppen.
```

---

## Aufgabe 2: Versions-Hook anlegen

```text
Erstelle `.claude/hooks/auto-version.md`.
Dieser Hook soll passieren, sobald ein Angebot als geprueft markiert wurde.
Dann soll:
1. Die Versionsnummer um 1 erhoehen (v1 -> v2).
2. Eine kurze Zusammenfassung der Aenderungen gespeichert werden.
```

---

## Aufgabe 3: Eigenen Hook erfinden

Ueberlege: Was soll in deiner App automatisch passieren?

```text
Erstelle `.claude/hooks/[dein-name].md`.
Dieser Hook soll passieren wenn: [Ereignis beschreiben]
Dann soll: [Folgeaktion beschreiben]
```

Beispiele zur Inspiration:

- Angebot exportiert -> Export protokollieren
- Angebot abgelehnt -> Ablehnungsgrund speichern
- 7 Tage ohne Pruefung -> Erinnerungshinweis zeigen

---

## Aufgabe 4: Ablauf simulieren lassen

```text
Simuliere den kompletten Ablauf:
1. Angebot wird erstellt -> Hook notify-review triggert
2. Pruefung wird abgeschlossen -> Hook auto-version triggert
Zeige nach jedem Schritt, welcher Status aktiv ist.
```

Notiere:

```
Nach Schritt 1: _______________________________
Nach Schritt 2: _______________________________
```

---

## Done-Kriterien

- [ ] `notify-review.md` Hook vorhanden
- [ ] `auto-version.md` Hook vorhanden
- [ ] Eigener Hook erstellt
- [ ] Ablauf simuliert

## Naechstes Modul

`08-mcp`: Echte Daten in die App einbinden (optional).
