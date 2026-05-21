# Hooks

**Block:** 10:45 - 12:15 Uhr (Tag 2)

---

## Was ist ein Hook?

Ein Hook ist eine **automatische Folgeaktion** - sie passiert ohne dein Zutun,
wenn ein bestimmtes Ereignis in der App eintritt.

Beispiel: Sobald ein Angebot erstellt wird, soll automatisch ein Pruefauftrag entstehen.
Du musst nichts mehr manuell anstoessen.

```
Ein Ereignis tritt ein (z.B. Angebot erstellt)
  -> Hook-Bedingung greift
  -> Folgeaktion startet automatisch
  -> Du musst nichts mehr daran denken
```

**Pfad:** `.claude/hooks/<name>.md`

---

## Warum / Wann nicht?

| Warum nutzen                           | Wann nicht                               |
| -------------------------------------- | ---------------------------------------- |
| Nie wieder etwas manuell vergessen     | Einmalige manuelle Sonderaufgabe         |
| Wiederkehrende Ablaeufe automatisieren | Wenn der Prozess noch nicht stabil ist   |
| Review-Prozess standardisieren         | Wenn das Team den Ablauf noch diskutiert |

---

## So beschreibst du einen Hook

Du erklaerst:

- Wann soll die Aktion passieren? (Ereignis)
- Was soll dann automatisch passieren? (Aktion)
- Was wenn etwas schiefgeht? (Fehlerfall)

Kein Code, nur Text.

---

## Vollstaendige Beispiele

**`.claude/hooks/notify-review.md`**

```markdown
# Hook: Pruefhinweis nach Erstellung

Wann: Sobald ein Angebot erstellt wurde.

Was dann passiert:

1. Status des Angebots auf "Wartet auf Pruefung" setzen.
2. Einen Pruefauftrag mit aktuellem Datum und Uhrzeit erstellen.
3. Hinweis in der App anzeigen: "Angebot bereit zur Pruefung".

Wenn etwas schiefgeht:

- Falls keine Angebots-ID vorhanden ist: Fehler protokollieren, nichts weiter tun.
```

**`.claude/hooks/auto-version.md`**

```markdown
# Hook: Automatische Versionierung

Wann: Sobald ein Angebot als geprueft markiert wurde.

Was dann passiert:

1. Versionsnummer erhoehen (v1 wird zu v2).
2. Kurze Zusammenfassung der Aenderungen speichern.
```

---

## So laesst du Claude den Hook anlegen

```text
Erstelle `.claude/hooks/notify-review.md`.
Dieser Hook soll automatisch passieren, sobald ein Angebot erstellt wurde.
Dann soll: Status auf 'Wartet auf Pruefung' gesetzt werden,
ein Pruefauftrag mit Zeitstempel erstellt werden,
und ein Hinweis in der App erscheinen.
Fehlerfall: Wenn keine ID vorhanden, Fehler protokollieren und stoppen.
```

---

## Muster-Prompts

```text
Erstelle `.claude/hooks/notify-review.md` fuer das Ereignis
'Angebot erstellt'. Setze Status, erstelle Aufgabe, zeige Hinweis.
```

```text
Erstelle `.claude/hooks/auto-version.md` fuer das Ereignis
'Angebot geprueft'. Erhoehe Versionsnummer und schreibe Aenderungslog.
```

```text
Simuliere den kompletten Ablauf: Angebot erstellen, Hook 1 triggert,
Pruefung abschliessen, Hook 2 triggert. Zeige jeden Zustandswechsel.
```

---

## Ergebnis

Deine App automatisiert wiederkehrende Schritte.
Kein manuelles Nachfassen mehr - Hooks erledigen das.

---

## Warum / Wann nicht?

| Warum nutzen                               | Wann nicht                             |
| ------------------------------------------ | -------------------------------------- |
| Wiederholbare Folgeaktionen automatisieren | Einmalige manuelle Sonderaufgabe       |
| Fehler reduzieren (nichts vergessen)       | Wenn Trigger noch instabil sind        |
| Review-Prozess standardisieren             | Wenn Teamfluss noch nicht geklaert ist |

---

## Aufbau - Vollstaendiges Beispiel

**`.claude/hooks/notify-review.md`**

```markdown
# Hook: notify-review

Trigger:

- Event: offer.generated

Aktion:

1. Setze Status auf "in review"
2. Erzeuge Review-Task mit Zeitstempel
3. Schreibe Hinweis in die UI-Meldungen

Fehlerfall:

- Wenn Angebots-ID fehlt, logge Fehler und stoppe Hook.
```

**`.claude/hooks/auto-version.md`**

```markdown
# Hook: auto-version

Trigger:

- Event: offer.review.completed

Aktion:

1. Erhoehe Angebotsversion (v1 -> v2)
2. Speichere kurze Aenderungszusammenfassung
```

---

## Muster-Prompts

```text
Erstelle `.claude/hooks/notify-review.md` fuer den Trigger offer.generated.
Lege Statuswechsel, Task-Erstellung und UI-Hinweis fest.
```

```text
Erstelle `.claude/hooks/auto-version.md` fuer den Trigger offer.review.completed.
```

```text
Simuliere beide Hooks fuer einen Testfall und gib die resultierenden
Statusaenderungen Schritt fuer Schritt aus.
```

---

## Ergebnis

Die App wird prozessorientiert: Generate fuehrt automatisch zu sauberem Review-Flow.
