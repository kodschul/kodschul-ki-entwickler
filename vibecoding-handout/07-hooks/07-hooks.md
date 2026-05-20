# Hooks

**Block:** 10:45 - 12:15 Uhr (Tag 2, zusammen mit Specs)

---

## Wie funktioniert das unter der Haube?

```
Event tritt ein (z.B. Angebot erzeugt)
	-> Hook-Bedingung greift
	-> definierte Folgeaktion wird automatisch gestartet
	-> Team spart manuelle Zwischenschritte
```

Hooks sind **Automatisierungsregeln fuer Folgeprozesse**.

**Pfad:** `.claude/hooks/<name>.md`

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
