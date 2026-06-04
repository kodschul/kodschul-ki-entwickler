# Übung: Chat & Kontext-Variablen – TypeScript Angular

**Zeit:** 90 min | **Projekt:** Angular Todo App

---

## Aufgabe 1 – Kontext-Variablen erkunden (20 min)

Öffne Copilot Chat. Probiere folgende Prompts aus und beobachte die Antwortqualität:

**Ohne Kontext:**

```
Erkläre wie die Todos gespeichert werden.
```

**Mit #file:**

```
Erkläre wie die Todos gespeichert werden. #file:src/app/services/todo.service.ts
```

**Mit #sym:**

```
Erkläre #sym:funcLoadTodos und #sym:funcSaveTodo
```

**Vergleich:** Wie unterscheiden sich die Antworten?

---

## Aufgabe 2 – @workspace nutzen (20 min)

```
@workspace Wo werden Todos geladen und wo werden sie gespeichert?
```

```
@workspace Welche Angular-Routen existieren und welche haben Unit-Tests?
```

```
@workspace Gibt es Code-Duplikate zwischen todo.service.ts und den Komponenten?
```

**Beobachten:** Was findet `@workspace` dass ein normaler Prompt nicht findet?

---

## Aufgabe 3 – Inline Chat (20 min)

1. Öffne `src/app/components/todo-form/todo-form.component.ts`
2. Markiere die `funcSubmit()`-Methode
3. Drücke `⌘ I` / `Ctrl I`
4. Gib ein:

```
Füge Reactive-Forms-Validierung hinzu: Titel darf nicht leer sein
und nicht länger als 200 Zeichen. Zeige eine Fehlermeldung unter
dem Input-Feld wenn die Validierung fehlschlägt.
```

5. Prüfe den Diff – sind alle Änderungen in `.ts` und `.html` korrekt?
6. `⌘ Enter` zum Annehmen oder `Esc` zum Ablehnen

---

## Aufgabe 4 – #terminalLastCommand (15 min)

```bash
# Im Terminal ausführen:
ng test --watch=false --browsers=ChromeHeadless
```

Falls Tests fehlschlagen → in Copilot Chat:

```
#terminalLastCommand
Warum schlägt dieser Test fehl? Wie behebe ich es?
```

Falls alle Tests grün → einen Test absichtlich kaputt machen:

```typescript
// todo.service.spec.ts – temporär ändern:
it("should load todos", () => {
  expect(true).toBe(false); // Absichtlicher Fehler
});
```

---

## Aufgabe 5 – #changes für Code-Review (15 min)

Ergänze in `src/app/models/todo.model.ts` ein neues Feld:

```typescript
export interface Todo {
  id: number;
  title: string;
  completed: boolean;
  dueDate: string | null;
  tags?: string[]; // ← NEU
}
```

Dann in Copilot Chat:

```
Mache einen kurzen Code-Review meiner Änderungen. #changes
Sind alle Stellen aktualisiert die Todo nutzen?
```

---

## Aufgabe 6 – Edit-Modus vs. Ask-Modus (15 min)

**Ask-Modus:**

```
Wie implementiere ich einen DarkMode-Toggle in Angular ohne externe Bibliothek?
```

**Edit-Modus** (öffne todo-list.component.ts, dann Edit-Modus auswählen):

```
Füge einen Toggle-Button hinzu der abgeschlossene Todos ein- und ausblendet.
Nutze ein lokales boolean-Signal: showCompleted.
```

**Beobachten:**

- Ask-Modus: erklärt, schreibt keinen Code direkt in die Datei
- Edit-Modus: ändert direkt die ausgewählten Dateien
