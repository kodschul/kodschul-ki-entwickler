# Übung: Integrierte Commands – TypeScript Angular

**Zeit:** 90 min | **Projekt:** Angular Todo App

---

## Aufgabe 1 – /explain (15 min)

**Schritt 1:** Öffne `src/app/services/todo.service.ts` und markiere `funcLoadTodos`.

**Schritt 2:** Tippe in Copilot Chat:

```
/explain #sym:funcLoadTodos
```

**Schritt 3:** Frage nach Details:

```
Was passiert wenn der HTTP-Request fehlschlägt? Gibt es eine Fehlerbehandlung?
```

**Schritt 4:** Erkläre etwas Angular-spezifisches:

```
/explain Warum injizieren wir HttpClient via inject() statt über den Konstruktor?
```

---

## Aufgabe 2 – /fix (20 min)

**Schritt 1 – Absichtlichen Fehler einbauen:**

Ändere in `todo.service.ts` temporär:

```typescript
// Statt:
this.http.get<Todo[]>(this.apiUrl)
// Schreibe:
this.http.fetch<Todo[]>(this.apiUrl)  // falscher Methodenname
```

**Schritt 2:** Starte den Dev-Server oder führe Build aus:

```bash
ng build 2>&1 | tail -20
```

**Schritt 3:** In Copilot Chat:

```
/fix #terminalLastCommand
```

**Schritt 4:** Unterschied testen – mit vs. ohne Fehler-Output:

```
/fix Die App lädt keine Todos – warum?
```

vs.

```
/fix #terminalLastCommand
Fehler: Property 'fetch' does not exist on type 'HttpClient'
```

**Beobachten:** Welche Variante gibt den präziseren Fix?

---

## Aufgabe 3 – /tests (20 min)

**Schritt 1:** Generiere Tests für den TodoService:

```
/tests Schreibe Karma/Jasmine Unit-Tests für funcAddTodo in
#file:src/app/services/todo.service.ts.
Nutze HttpClientTestingModule. Happy path + leerer Titel.
```

**Schritt 2:** Füge in `.vscode/settings.json` Test-Instructions hinzu:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze Karma/Jasmine. Immer happy path + edge case. HttpClientTestingModule für Services. Kommentare auf Deutsch."
    }
  ]
}
```

**Schritt 3:** Generiere erneut – merkst du einen Unterschied?

```
/tests #file:src/app/services/todo.service.ts
```

**Schritt 4:** Tests ausführen:

```bash
ng test --watch=false --browsers=ChromeHeadless
```

---

## Aufgabe 4 – /doc (15 min)

**Schritt 1:**

```
/doc Erstelle JSDoc-Kommentare für alle public Methoden in
#file:src/app/services/todo.service.ts
```

**Schritt 2:** Spezifischen Stil anfordern:

```
/doc Schreibe einen vollständigen JSDoc für #sym:funcLoadTodos
mit @param, @returns und @throws
```

---

## Aufgabe 5 – /new (10 min)

Erstelle eine neue Komponente direkt aus dem Chat:

```
/new Erstelle eine Angular standalone Komponente "todo-filter"
mit drei Buttons: Alle / Offen / Erledigt.
Nutze ein Output-EventEmitter<'all'|'open'|'done'>.
Kein externes CSS-Framework.
```

**Prüfe:** Sind alle nötigen Dateien erstellt (`.ts`, `.html`, `.spec.ts`)?

---

## Aufgabe 6 – Copilot Code Review (10 min)

1. Markiere die gesamte `todo.service.ts`
2. Rechtsklick → **Copilot** → **Review and Comment**
3. Prüfe die Kommentare – sind sie sinnvoll?
4. Klicke auf einen Kommentar und wähle **Accept** oder **Discard**
