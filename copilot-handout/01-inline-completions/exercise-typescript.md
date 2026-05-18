# Übung: Inline Completions – TypeScript Angular

**Zeit:** 90 min | **Projekt:** Angular Todo App

---

## Projekt-Setup

```bash
ng new todo-app-angular --standalone --routing --style=css
cd todo-app-angular
ng generate service services/todo
ng generate component components/todo-list
ng generate component components/todo-form
ng generate interface models/todo
```

---

## Aufgabe 1 – Shortcuts kennenlernen (20 min)

Öffne `src/app/services/todo.service.ts`. Schreibe ans Ende:

```typescript
// Returns all todos that are due today
funcGetDueToday(todos: Todo[]): Todo[] {
```

**Ausprobieren:**

1. Warte auf Ghost Text
2. `⌥ ]` / `Alt ]` – nächster Vorschlag
3. `⌥ [` / `Alt [` – vorheriger Vorschlag
4. `⌥ Enter` / `Alt Enter` – alle Vorschläge im Panel
5. `⌘ →` / `Ctrl →` – Wort für Wort annehmen

**Fragen:**

- Wie viele verschiedene Vorschläge bietet Copilot an?
- Nutzt Copilot `Date` korrekt für den Vergleich?

---

## Aufgabe 2 – Kontext mit Kommentar steuern (20 min)

Schreibe drei Varianten in `todo.service.ts` und beobachte wie der Kommentar den Vorschlag ändert:

**Variante A – kein Kommentar:**

```typescript
funcValidateTodo(title: string): boolean {
  |
}
```

**Variante B – kurzer Kommentar:**

```typescript
// Validates the todo title
funcValidateTodo(title: string): boolean {
  |
}
```

**Variante C – präziser Kommentar:**

```typescript
// Validates the todo title: not empty, max 200 characters.
// Returns { valid: true } on success or { valid: false, error: string } on failure.
funcValidateTodo(title: string): { valid: boolean; error?: string } {
  |
}
```

**Beobachten:** Wie unterscheiden sich die Rückgabetypen in den Vorschlägen?

---

## Aufgabe 3 – JSDoc-First (20 min)

Schreibe zuerst den JSDoc, dann lässt du Copilot die Implementierung generieren:

```typescript
/**
 * Formats an ISO date string (YYYY-MM-DD) for display in the UI.
 *
 * - Returns 'Kein Datum' if dueDateStr is empty or null
 * - Returns 'Überfällig' if the date is in the past
 * - Otherwise returns 'Fällig am DD.MM.YYYY'
 *
 * @param dueDateStr - ISO date string or null
 * @returns Formatted string for display
 */
funcFormatDueDate(dueDateStr: string | null): string {
  |
}
```

Akzeptiere den Vorschlag. Schreibe dann einen Test:

```typescript
describe('funcFormatDueDate', () => {
  it('should return |  // Copilot leitet aus dem JSDoc Tests ab
```

---

## Aufgabe 4 – Next Edit Suggestion (15 min)

1. Öffne `src/app/models/todo.model.ts`
2. Füge ein neues Pflichtfeld hinzu: `priority: 'low' | 'medium' | 'high'`
3. Beobachte: Schlägt Copilot vor alle Stellen zu aktualisieren wo `Todo` genutzt wird?
4. Drücke `Tab` um jeden Vorschlag anzunehmen

**Alternativ:**

```typescript
// todo.model.ts – vor der Änderung:
export interface Todo {
  id: number;
  title: string;
  completed: boolean;
  dueDate: string | null;
}

// Ändere zu:
export interface Todo {
  id: number;
  title: string;
  completed: boolean;
  dueDate: string | null;
  priority: 'low' | 'medium' | 'high';  // ← NEU
}
```

**Beobachte:** Schlägt Copilot in `todo.service.ts` und `todo-form.component.ts` Updates vor?

---

## Aufgabe 5 – Copilot vs. manuelle Implementierung (15 min)

Implementiere die Funktion manuell:

```typescript
funcFilterByStatus(todos: Todo[], showCompleted: boolean): Todo[] {
  // Manuell: gibt todos zurück gefiltert nach completed-Status
}
```

Lösche die Implementierung wieder. Schreibe nur den Kommentar und lass Copilot vorschlagen.

**Vergleich:**
- Ist Copilots Vorschlag idiomatischer (z.B. nutzt er `filter()`)?
- Nutzt er den `showCompleted`-Parameter sinnvoll?
