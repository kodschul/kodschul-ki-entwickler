# Übung: Token-Management

**Zeit:** 60 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – Kontext vergleichen (20 min)

Stelle dieselbe Frage mit unterschiedlichem Kontext und beobachte Qualität + Geschwindigkeit:

**Runde 1 – Maximaler Kontext:**

```
@workspace Was macht diese App? Erkläre alle Funktionen im Detail.
```

**Runde 2 – Mittlerer Kontext:**

```
Erkläre #file:app.py – Fokus auf die CRUD-Operationen.
```

**Runde 3 – Minimaler Kontext:**

```
Erkläre #sym:func_load_todos
```

**Protokolliere:**
| Variante | Antwort-Qualität | Relevanz | Geschwindigkeit |
|---------------|------------------|----------|-----------------|
| @workspace | | | |
| #file | | | |
| #sym | | | |

**Fazit:** Wann ist mehr Kontext besser, wann schlechter?

---

## Aufgabe 2 – copilot-instructions.md schlank machen (15 min)

Öffne `.github/copilot-instructions.md`.

**Prüfe:**

- Gibt es redundante Informationen?
- Gibt es Regeln die nur für Python-Dateien gelten? → In `python.instructions.md` verschieben
- Gibt es Regeln die nur für Tests gelten? → In `testing.instructions.md` verschieben

**Ziel:** `copilot-instructions.md` auf unter 80 Zeilen reduzieren.

Vorher: Zeilenzahl messen:

```bash
wc -l .github/copilot-instructions.md
```

Nachher: Erneut messen und Ersparnis berechnen.

---

## Aufgabe 3 – Chat-Verlauf vs. neuer Chat (15 min)

**Schritt 1:** Führe 10+ Nachrichten in einem Chat durch (z.B. Aufgabe 1 vollständig).

**Schritt 2:** Stelle die gleiche Frage in einem NEUEN Chat:

```
Erkläre func_load_todos in #file:app.py
```

**Beobachten:** Ist die Antwort im neuen Chat fokussierter?

**Schritt 3:** Wann ist es sinnvoll den Chat zu leeren?  
Schreibe 3 konkrete Situationen aus dem heutigen Tag auf:

- Situation 1: \_\_\_
- Situation 2: \_\_\_
- Situation 3: \_\_\_

---

## Aufgabe 4 – CLI statt Chat für Terminal-Fragen (10 min)

Diese Fragen im Terminal statt im Editor-Chat stellen:

```bash
# Frage 1: Wie führe ich nur geänderte Tests aus?
gh copilot suggest "nur geänderte pytest-Tests ausführen" -t shell

# Frage 2: Wie finde ich alle Python-Dateien über 100 Zeilen?
gh copilot suggest "Python-Dateien finden die über 100 Zeilen haben" -t shell

# Frage 3: Erkläre den letzten git-Befehl
gh copilot explain "git log --oneline --graph --decorate"
```

**Reflexion:** Welche Fragen gehören besser in den CLI, welche in den Editor-Chat?
