# Übung: Skills & .instructions.md – TypeScript Angular

**Zeit:** 90 min | **Projekt:** Angular Todo App

---

## Aufgabe 1 – Angular Instructions erstellen (20 min)

```bash
mkdir -p .github/instructions
```

Erstelle `.github/instructions/angular.instructions.md`:

```markdown
---
applyTo: "**/*.ts"
description: "Angular TypeScript rules for this project"
---

# Angular Guidelines

- Angular 17+ standalone components, kein @NgModule
- inject() für Dependency Injection
- Signals: signal(), computed(), effect() bevorzugen
- Typ-Annotationen für alle Parameter und Rückgabewerte
- camelCase für alle Variablen und Funktionen
- Alle Funktionen starten mit func\_
- Kein `any` – stattdessen generics oder union types
- RxJS: takeUntilDestroyed() statt manuellem unsubscribe
```

**Testen:**

```
Schreibe einen Angular Service der prüft ob eine todos.json Datei
über HTTP verfügbar ist und lesbar ist.
```

**Beobachten:** Nutzt Copilot `inject(HttpClient)` und Typ-Annotationen?

---

## Aufgabe 2 – Security Instructions erstellen (20 min)

Erstelle `.github/instructions/security.instructions.md`:

```markdown
---
applyTo: "**"
description: "Security rules - applies to all files"
---

# Security Guidelines

- Keine hardcodierten Passwörter, Tokens oder API-Keys im Code
- Nutzereingaben immer mit Angular-Validatoren validieren (Validators.required etc.)
- HTTP-Anfragen: nur relative URLs oder aus environment.ts
- Kein direktes DOM-Manipulation via innerHTML (XSS-Risiko)
- API-Schlüssel nur über environment.ts, nie hardcodiert
```

**Testen:**

```
Schreibe eine Angular-Komponente mit einem Passwort-Eingabefeld
das in localStorage gespeichert wird.
```

**Beobachten:** Warnt Copilot vor localStorage für Passwörter? Schlägt es Alternativen vor?

---

## Aufgabe 3 – Testing Instructions + settings.json (20 min)

Erstelle `.github/instructions/testing.instructions.md`:

```markdown
---
applyTo: "**/*.spec.ts"
description: "Karma/Jasmine testing rules for Angular"
---

# Testing Guidelines

- Immer: happy path + leere/null Eingabe + ungültiger Wert
- HttpClientTestingModule für alle Services die HTTP nutzen
- Test-Namen beschreiben das Szenario:
  it('should return error when title is empty')
- Kommentare auf Deutsch
- TestBed.configureTestingModule() vollständig konfigurieren
```

Verknüpfe in `.vscode/settings.json`:

```json
{
  "github.copilot.chat.testGeneration.instructions": [
    { "file": ".github/instructions/testing.instructions.md" }
  ]
}
```

**Testen:**

```
/tests Schreibe Tests für funcAddTodo in
#file:src/app/services/todo.service.ts
```

Nutzt Copilot `HttpClientTestingModule`? Schreibt es Kommentare auf Deutsch?

---

## Aufgabe 4 – applyTo Muster verstehen (15 min)

Erstelle `.github/instructions/html-templates.instructions.md`:

```markdown
---
applyTo: "**/*.component.html"
description: "Angular template rules"
---

# Template Guidelines

- Kein inline style=""
- Nutze @if / @for statt *ngIf / *ngFor (Angular 17+ Syntax)
- aria-label für alle interaktiven Elemente
- Tailwind CSS Klassen für Styling
```

**Testen:** Öffne eine `.component.html` und lass Copilot etwas generieren.  
Nutzt es `@if` und `@for`?

---

## Aufgabe 5 – Instructions stapeln (15 min)

Prüfe ob mehrere Instructions gleichzeitig wirken:

```
Schreibe eine Angular-Komponente todo-item die:
- Ein Todo anzeigt
- Einen Delete-Button hat
- Tests für beide Fälle enthält
```

**Beobachten:**

- Wirkt `angular.instructions.md` (inject, Signals)?
- Wirkt `testing.instructions.md` (happy path + edge case)?
- Wirkt `security.instructions.md` (kein innerHTML)?
