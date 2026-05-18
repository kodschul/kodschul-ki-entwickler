# 09 – Token-Management & Kontext sparen

**Block:** 60 min | **Tag 3**

---

## Was ist das Token-Limit?

Copilot hat ein **Kontextfenster** – die maximale Menge an Text die gleichzeitig verarbeitet werden kann:

```
Kontextfenster = System-Prompt + Chat-Verlauf + Dateikontexte + Antwort
```

Wenn das Limit erreicht ist:

- Ältere Chat-Nachrichten fallen raus
- Copilot "vergisst" frühere Anweisungen
- Antwortqualität sinkt

> **Ziel:** So wenig Tokens wie nötig – so viel Kontext wie sinnvoll.

---

## Token-Verbrauch visualisieren

| Was                          | Token-Verbrauch          |
| ---------------------------- | ------------------------ |
| Eine Zeile Code              | ~5–15 Tokens             |
| Eine Funktion (20 Zeilen)    | ~100–200 Tokens          |
| Eine Datei (200 Zeilen)      | ~1.000–2.000 Tokens      |
| `#codebase` (ganzes Projekt) | Sehr hoch – vorsicht     |
| Ein langer Chat-Verlauf      | Summiert sich schnell    |
| `copilot-instructions.md`    | Immer dabei (~500–1.000) |

---

## Strategie 1 – Gezielter Kontext statt alles

```
❌ Teuer:
@workspace Analysiere das gesamte Projekt und erkläre alle Funktionen.

✅ Günstig:
/explain #sym:func_load_todos

✅ Günstig:
Erkläre die /add Route in #file:app.py – nur diese Route.
```

**Regel:** Je präziser die Referenz, desto weniger Tokens.

| Zu viel Kontext             | Besser                     |
| --------------------------- | -------------------------- |
| `#codebase`                 | `#file:app.py`             |
| `#file:app.py` (200 Zeilen) | `#sym:func_add_todo`       |
| Ganzer Chat-Verlauf         | Neuer Chat für neues Thema |

---

## Strategie 2 – Chat regelmäßig leeren

Ein langer Chat-Verlauf kostet bei **jeder** Nachricht Tokens – auch für Themen die längst abgeschlossen sind.

```
🔄 Neue Aufgabe → Neuer Chat
```

**Wann neuen Chat starten:**

- Thema wechselt (von Bug-Fix zu neuem Feature)
- Chat-Verlauf > 20 Nachrichten
- Copilot antwortet zunehmend "off-topic"
- Nach erfolgreichem Feature-Abschluss

**Kurzform:**

- `+` Icon oben im Chat-Panel
- `⌘ Shift I` → Quick Chat → eigener kleiner Kontext

---

## Strategie 3 – copilot-instructions.md schlank halten

`copilot-instructions.md` wird bei **jeder** Antwort geladen. Jedes extra Wort kostet Tokens bei jeder Frage.

```markdown
❌ Zu lang (500+ Zeilen Projekt-Wiki):

# Projektgeschichte

...30 Absätze Hintergrund...

# Architektur-Entscheidungen

...20 ADRs...

✅ Kompakt (50–100 Zeilen):

## Projekt

Flask Todo-App, todos.json, Tailwind CDN.

## Start

FLASK_DEBUG=1 python app.py

## Regeln

- Kein JavaScript fetch
- Post/Redirect/Get Pattern
```

**Empfehlung:** Maximal 100 Zeilen in `copilot-instructions.md`.  
Details gehören in spezifische `.instructions.md`-Dateien (werden nur bei Match geladen).

---

## Strategie 4 – .instructions.md mit `applyTo` scharf eingrenzen

Eine Instruction mit `applyTo: "**"` wird bei **jeder** Datei geladen.  
Eingrenzen spart Tokens:

```yaml
# ❌ Immer geladen (auch bei HTML, YAML, etc.):
applyTo: "**"

# ✅ Nur bei Python-Dateien:
applyTo: "**/*.py"

# ✅ Nur bei Test-Dateien:
applyTo: "**/test_*.py"

# ✅ Nur bei einer konkreten Datei:
applyTo: "**/app.py"
```

---

## Strategie 5 – Kompakte Prompts schreiben

```
❌ Token-Verschwendung:
"Ich möchte, dass du dir bitte die aktuelle Datei app.py anschaust und
dann schaust ob du vielleicht eine Funktion findest die ich verbessern
könnte, wenn das möglich ist natürlich."

✅ Kompakt:
"Verbessere func_load_todos in #file:app.py – Fehlerbehandlung fehlt."
```

**Prompt-Muster:**

- **Was** soll gemacht werden (Verb + Objekt)
- **Wo** (Datei / Funktion / Zeile)
- **Wie** (Konstraints, Format)

---

## Strategie 6 – Inline Chat statt Vollchat

Inline Chat (`⌘ I`) hat **eigenen kleinen Kontext** – nur die aktuelle Datei + Selektion.  
Ideal für lokale Änderungen ohne Chat-Verlauf zu belasten.

```
Chat-Panel:     Großer Kontext, sammelt Verlauf → für übergreifende Aufgaben
Inline Chat:    Kleiner Kontext, kein Verlauf   → für lokale Code-Änderungen
Quick Chat:     Minimalkontext                  → für schnelle Fragen
```

---

## Strategie 7 – Spezifische Fragen statt Open-End

```
❌ Token-intensiv (Copilot muss viel explorieren):
"Was könnte ich an meiner App verbessern?"

✅ Token-effizient:
"Hat func_load_todos ein Race-Condition Problem? Ja/Nein + Begründung."
```

---

## Token-Sparplan auf einen Blick

| Situation                        | Token-effiziente Alternative                |
| -------------------------------- | ------------------------------------------- |
| Ganzes Projekt analysieren       | Eine Datei mit `#file` referenzieren        |
| Langer Chat läuft schon          | Neuen Chat starten (`+`)                    |
| `#codebase` für einfache Frage   | `#sym` oder `#file` mit Dateiname           |
| Lange `copilot-instructions.md`  | Aufteilen in spezifische `.instructions.md` |
| Code-Review der ganzen Datei     | Inline Chat für spezifische Funktion        |
| Allgemeine Verbesserungsideen    | Konkrete Frage mit Scope eingrenzen         |
| Instructions mit `applyTo: "**"` | `applyTo` auf tatsächlich relevante Dateien |

---

## gh copilot CLI – Token-frei für Terminal-Fragen

`gh copilot suggest` läuft vollständig **außerhalb des VS Code Chat-Kontexts** – kein Token-Verbrauch im Editor:

```bash
# Diese Fragen im Terminal stellen statt im Chat:
gh copilot suggest "alle Python-Dateien nach Änderungsdatum sortieren"
gh copilot explain "find . -name '*.py' -newer requirements.txt"
gh copilot suggest "pytest nur für geänderte Dateien ausführen" -t shell
```

→ Spart Tokens für komplexere Code-Aufgaben im Editor.
