# Übung: Spec-Kit

**Zeit:** 13:15 – 15:00 Uhr | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Plan erstellen mit `/spec plan` (15 min)

**Ziel:** Claude analysiert die Codebase und erstellt einen Implementierungsplan.

```
/spec plan Notizen für Todos hinzufügen
```

Claude sollte automatisch:

- `app.py` und `templates/` analysieren
- Eine Spec-Datei unter `specs/` erstellen
- Betroffene Dateien, Schritte und Akzeptanzkriterien auflisten

**Prüfen bevor du weitermachst:**

- [ ] Sind alle betroffenen Dateien richtig erkannt?
- [ ] Sind die Implementierungsschritte logisch sortiert?
- [ ] Gibt es mindestens 3 Akzeptanzkriterien?

Falls etwas fehlt – **korrigiere die Spec manuell** bevor du implementierst.

---

## Aufgabe 2 – Implementieren mit `/spec` (20 min)

```
/spec
```

Beobachte:

- Hakt Claude Schritte in der Spec-Datei ab?
- Bleibt Claude im Scope (nur die in der Spec genannten Dateien)?
- Was passiert wenn ein Schritt unklar ist?

**App testen:**

```bash
FLASK_DEBUG=1 python app.py
```

Öffne `http://localhost:5000` – ist das Notiz-Feld sichtbar?

---

## Aufgabe 3 – Tests generieren mit `/spec test` (15 min)

```
/spec test
```

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

## Aufgabe 4 – Vergleich: Spec-Kit vs. manuell (10 min)

Du hast heute beide Wege gemacht:

- **Manuell** (Übung 06): Du hast die Spec selbst geschrieben
- **Spec-Kit** (diese Übung): Claude hat die Spec aus der Codebase generiert

**Diskussion:**

| Frage                               | Deine Beobachtung |
| ----------------------------------- | ----------------- |
| Welcher Plan war präziser?          |                   |
| Wo hat Claude Dinge übersehen?      |                   |
| Wann würdest du welchen Weg wählen? |                   |

---

## Bonus – Abgebrochene Spec fortsetzen (10 min)

Brich eine laufende `/spec`-Session ab (Ctrl+C oder neues Fenster).

Starte Claude neu und tippe:

```
/spec
```

Macht Claude weiter wo es aufgehört hat? Schau dir die Checkboxen in der Spec-Datei an.

---

## Zusammenfassung

Nach dieser Übung hast du:

- [ ] Plan mit `/spec plan` erstellt und geprüft
- [ ] Feature mit `/spec` implementiert
- [ ] Tests mit `/spec test` generiert und ausgeführt
- [ ] Spec-Kit mit manueller Spec verglichen
