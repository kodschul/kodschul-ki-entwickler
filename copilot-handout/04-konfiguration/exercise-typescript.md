# Übung: Konfiguration – TypeScript Angular

**Zeit:** 60 min | **Projekt:** Angular Todo App

---

## Aufgabe 1 – copilot-instructions.md erstellen (20 min)

```bash
mkdir -p .github
```

Erstelle `.github/copilot-instructions.md`:

```
Erstelle eine .github/copilot-instructions.md für diese Angular Todo App.
Halte sie unter 80 Zeilen. Enthalte:
- Project Goal (1 Satz)
- Stack (Angular 17+, standalone components, Signals, RxJS, Karma/Jasmine)
- Commands (Start: ng serve, Test: ng test, Build: ng build)
- Architecture (3 Sätze: Component → Service → HttpClient → REST API)
- Do (5 Regeln – z.B. camelCase, inject(), Signals statt ngModel)
- Don't (5 Regeln – z.B. kein any, keine deprecated @NgModule, kein jQuery)
```

Prüfe: Unter 80 Zeilen?

```bash
wc -l .github/copilot-instructions.md
```

---

## Aufgabe 2 – .vscode/settings.json konfigurieren (20 min)

Erstelle `.vscode/settings.json`:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    { "file": ".github/instructions/angular.instructions.md" }
  ],
  "github.copilot.chat.testGeneration.instructions": [
    {
      "text": "Nutze Karma/Jasmine. HttpClientTestingModule für Services. Immer happy path + edge case. Kommentare auf Deutsch."
    }
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": ".github/instructions/security.instructions.md" }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    {
      "text": "Englisch. Format: type(scope): message. Typen: feat/fix/docs/refactor/test/chore."
    }
  ],
  "github.copilot.enable": {
    "*": true,
    "markdown": false
  },
  "github.copilot.chat.localeOverride": "de"
}
```

**Testen:** Öffne Copilot Chat → frage etwas zu Angular.
Antwortet Copilot auf Deutsch und nutzt es moderne Angular-Patterns?

---

## Aufgabe 3 – Angular Instructions erstellen (10 min)

Erstelle `.github/instructions/angular.instructions.md`:

```markdown
---
applyTo: "**/*.ts"
description: "Angular TypeScript code generation rules"
---

# Angular Guidelines

- Angular 17+ standalone components, kein @NgModule
- inject() statt Konstruktor-Injection
- Signals (signal(), computed(), effect()) bevorzugen
- Typ-Annotationen für alle Parameter und Rückgabewerte
- camelCase für alle Variablen und Funktionen
- Alle Funktionen starten mit func_
- Kein `any`-Typ – stattdessen generics oder union types
- RxJS: takeUntilDestroyed() statt manuellem unsubscribe
```

---

## Aufgabe 4 – Commit-Message Generator (10 min)

1. Ändere etwas in `todo.service.ts` (z.B. Kommentar hinzufügen)
2. Öffne Source Control Panel (`⌃ ⇧ G` / `Ctrl Shift G`)
3. Klicke auf das **Zauberstab-Icon** neben dem Commit-Eingabefeld
4. Prüfe: Folgt die generierte Message dem Format `type(scope): message`?

---

## Aufgabe 5 – Reflektion: Was gehört wo? (10 min)

Entscheide für jede Regel wo sie hingehört:

| Regel                                      | copilot-instructions.md | .instructions.md | .vscode/settings.json |
|--------------------------------------------|-------------------------|------------------|-----------------------|
| "Nutze standalone components"              |                         |                  |                       |
| "Typ-Annotationen für alle Parameter"      |                         |                  |                       |
| "Tests mit Karma/Jasmine"                  |                         |                  |                       |
| "Commit-Messages auf Englisch"             |                         |                  |                       |
| "ng serve startet auf Port 4200"           |                         |                  |                       |
| "Antworten auf Deutsch"                    |                         |                  |                       |
