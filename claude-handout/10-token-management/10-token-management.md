# 10 – Token-Management & Kontext sparen

**Block:** 60 min | **Tag 4**

---

## Was ist das Token-Limit?

Claude hat ein **Kontextfenster** – die maximale Menge an Text, die gleichzeitig verarbeitet werden kann:

```
Kontextfenster = CLAUDE.md + Tool-Ausgaben (gelesene Dateien) + Konversationsverlauf + Antwort
```

Wenn das Limit erreicht ist bzw. sich nähert:

- Claude Code kann automatisch komprimieren (Auto-Compact) oder du musst manuell eingreifen (`/compact`, Modul 04)
- Ältere Teile des Verlaufs gehen als Detail verloren
- Antwortqualität sinkt, wenn zu viel irrelevanter Kontext mitgeschleppt wird

> **Ziel:** So wenig Tokens wie nötig – so viel Kontext wie sinnvoll.

---

## Token-Verbrauch visualisieren

| Was                              | Token-Verbrauch            |
| ----------------------------------- | ----------------------------- |
| Eine Zeile Code                       | ~5–15 Tokens                  |
| Eine Funktion (20 Zeilen)             | ~100–200 Tokens               |
| Eine Datei (200 Zeilen)               | ~1.000–2.000 Tokens           |
| Claude durchsucht die ganze Codebase   | Sehr hoch – Vorsicht           |
| Ein langer Konversationsverlauf       | Summiert sich schnell          |
| `CLAUDE.md`                           | Immer dabei (~500–1.000)      |

---

## Strategie 1 – Gezielter Kontext statt alles

```
❌ Teuer:
Analysiere das gesamte Projekt und erkläre alle Funktionen.

✅ Günstig:
Erkläre die Funktion add_todo() in app.py.

✅ Günstig:
Erkläre die /add Route in app.py – nur diese Route.
```

**Regel:** Je präziser die Aufgabe, desto weniger Dateien muss Claude lesen und desto weniger Tokens werden verbraucht.

| Zu viel Kontext                     | Besser                            |
| --------------------------------------- | ------------------------------------ |
| "Durchsuche das ganze Repo"               | Konkreten Ordner/Datei nennen         |
| Ganze Datei lesen lassen (200 Zeilen)     | Nach konkreter Funktion/Route fragen  |
| Ganzer Konversationsverlauf                | `/clear` für neues Thema (Modul 04)  |

---

## Strategie 2 – Session-Hygiene: `/clear` und `/compact`

Ein langer Verlauf kostet bei **jeder** weiteren Nachricht Tokens – auch für Themen, die längst abgeschlossen sind.

```
🔄 Neue Aufgabe/Thema → /clear
🔄 Gleiche Aufgabe, aber Kontext wird groß → /compact
```

**Wann `/clear`:**

- Thema wechselt komplett (von Bug-Fix zu neuem Feature)
- Nach erfolgreichem Feature-Abschluss

**Wann `/compact`:**

- Gleiche Aufgabe läuft weiter, aber Verlauf ist schon sehr lang
- Vor einer neuen, größeren Teilaufgabe innerhalb derselben Session

---

## Strategie 3 – CLAUDE.md schlank halten

`CLAUDE.md` wird bei **jedem Start** vollständig geladen. Jedes extra Wort kostet Tokens bei jeder Session.

```
❌ Zu lang (500+ Zeilen Projekt-Wiki):
# Projektgeschichte
...30 Absätze Hintergrund...
# Architektur-Entscheidungen
...20 ADRs...

✅ Kompakt (50–100 Zeilen):
## Project Goal
Flask Todo-App, todos.json, Tailwind CDN.
## Commands
FLASK_DEBUG=1 python app.py
## Do / Don't
- Post/Redirect/Get Pattern
- Kein JavaScript fetch
```

**Empfehlung:** Maximal 100 Zeilen in der Root-`CLAUDE.md`. Details gehören in verschachtelte `CLAUDE.md`-Dateien pro Unterordner (Modul 06) – die werden nur geladen, wenn tatsächlich in diesem Bereich gearbeitet wird.

---

## Strategie 4 – Verschachtelte CLAUDE.md statt einer riesigen Datei

Genau wie `.instructions.md` mit `applyTo` bei GitHub Copilot lässt sich mit **`CLAUDE.md` pro Unterordner** (Modul 06) der Kontext gezielt eingrenzen, statt alles in eine einzige Root-Datei zu packen.

```
CLAUDE.md               ← 30 Zeilen, projektweit gültig
backend/CLAUDE.md       ← 20 Zeilen, nur bei Arbeit im Backend geladen
frontend/CLAUDE.md      ← 20 Zeilen, nur bei Arbeit im Frontend geladen
```

---

## Strategie 5 – Subagenten für Recherche nutzen

Ein Subagent (Modul 08, vertieft in Modul 15) kann eine aufwändige Recherche isoliert durchführen und liefert dem Hauptkontext nur das **Endergebnis** zurück – der Zwischenweg (viele gelesene Dateien) belastet den Hauptkontext nicht.

---

## Faustregeln

1. Gezielt fragen statt "durchsuche alles"
2. `/clear` bei Themenwechsel, `/compact` bei langer, aber laufender Aufgabe
3. `CLAUDE.md` kurz halten, Details in Unterordner-`CLAUDE.md` auslagern
4. Recherche-lastige Teilaufgaben an Subagenten delegieren
