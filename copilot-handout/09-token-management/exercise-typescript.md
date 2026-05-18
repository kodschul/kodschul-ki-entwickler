# Übung: Token-Management – TypeScript Angular

**Zeit:** 60 min | **Projekt:** Angular Todo App

---

## Aufgabe 1 – Kontext vergleichen (20 min)

Stelle dieselbe Frage mit unterschiedlichem Kontext und beobachte Qualität + Geschwindigkeit:

**Runde 1 – Maximaler Kontext:**

```
@workspace Was macht diese App? Erkläre alle Services und Komponenten im Detail.
```

**Runde 2 – Mittlerer Kontext:**

```
Erkläre #file:src/app/services/todo.service.ts – Fokus auf die CRUD-Methoden.
```

**Runde 3 – Minimaler Kontext:**

```
Erkläre #sym:funcLoadTodos
```

**Protokolliere:**

| Variante   | Antwort-Qualität | Relevanz | Geschwindigkeit |
|------------|------------------|----------|-----------------|
| @workspace |                  |          |                 |
| #file      |                  |          |                 |
| #sym       |                  |          |                 |

**Fazit:** Wann ist mehr Kontext besser, wann schlechter?

---

## Aufgabe 2 – copilot-instructions.md schlank machen (15 min)

Öffne `.github/copilot-instructions.md`.

**Prüfe:**

- Gibt es redundante Informationen?
- Gibt es Regeln die nur für `.ts`-Dateien gelten? → In `angular.instructions.md` verschieben
- Gibt es Regeln die nur für Tests gelten? → In `testing.instructions.md` verschieben

**Ziel:** `copilot-instructions.md` auf unter 80 Zeilen reduzieren.

Vorher messen:

```bash
wc -l .github/copilot-instructions.md
```

Nachher erneut messen und Ersparnis berechnen.

---

## Aufgabe 3 – Chat-Verlauf vs. neuer Chat (15 min)

**Schritt 1:** Führe 10+ Nachrichten in einem Chat durch (z.B. Aufgabe 1 vollständig).

**Schritt 2:** Stelle die gleiche Frage in einem NEUEN Chat:

```
Erkläre funcLoadTodos in #file:src/app/services/todo.service.ts
```

**Beobachten:** Ist die Antwort im neuen Chat fokussierter?

**Schritt 3:** Wann ist es sinnvoll den Chat zu leeren?  
Schreibe 3 konkrete Situationen aus dem heutigen Tag auf:

- Situation 1: \_\_\_
- Situation 2: \_\_\_
- Situation 3: \_\_\_

---

## Aufgabe 4 – Inline Chat statt Panel-Chat (10 min)

Öffne `todo-list.component.ts`. Markiere eine einzelne Methode.

**Panel-Chat (mehr Token):**

```
Wie optimiere ich funcLoadTodos damit es nur beim ersten Laden aufruft?
```

**Inline-Chat (weniger Token, ⌘I):**

```
Nutze takeUntilDestroyed() um Memory Leaks zu vermeiden.
```

**Fazit:** Inline Chat für lokale Änderungen spart Context-Token.
