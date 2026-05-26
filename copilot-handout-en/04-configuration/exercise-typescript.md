# Exercise: Configuration – TypeScript Angular

**Time:** 60 min | **Project:** Angular Todo App

---

## Task 1 – Create copilot-instructions.md (20 min)

```
Create a .github/copilot-instructions.md for our Angular Todo App.

Project:
- Angular 17+ with Standalone Components
- TypeScript strict mode
- Angular Signals for state management
- LocalStorage for persistence (no backend for now)
- Jasmine/Karma for unit tests
- CSS without any UI library (vanilla CSS)

Include:
1. Project goal (1 sentence)
2. Start command: ng serve
3. Test command: ng test --watch=false
4. DOs: Standalone Components, Signals, typed everything
5. DON'Ts: no NgModules, no jQuery, no eval()

Important: Maximum 80 lines!
```

---

## Task 2 – Create angular.instructions.md (15 min)

```
Create .github/instructions/angular.instructions.md for our Angular app.

applyTo: **/*.ts

Rules for all TypeScript files:
- Strict TypeScript: no "any" (use "unknown" or specific types)
- Prefer Angular Signals over BehaviorSubjects
- All Observables unsubscribed with takeUntilDestroyed()
- All public methods with explicit return types
- Interfaces for all data models (no classes for pure data)
```

---

## Task 3 – Configure .vscode/settings.json (15 min)

```
Create .vscode/settings.json for our Angular Todo App.

Configure:
1. codeGeneration: load angular.instructions.md
2. testGeneration: use Jasmine/TestBed, always 3 test cases
   (happy path, invalid input, edge case), describe/it format
3. commitMessageGeneration: Conventional Commits, max 72 chars
4. localeOverride: "en"
```

---

## Task 4 – Test Commit Message Generator (5 min)

1. Make a small change in `todo.service.ts`
2. Stage the file
3. Click ✨ in the commit message field
4. Observe: `feat:` or `fix:`?

---

## Task 5 – Reflection (5 min)

| Rule                                    | Where does it belong?                       |
| --------------------------------------- | ------------------------------------------- |
| "Use Jasmine for tests"                 | settings.json / testGeneration              |
| "No backend – only LocalStorage"        | copilot-instructions.md                     |
| "No 'any' in TypeScript"                | angular.instructions.md (applyTo: \*_/_.ts) |
| "No eval()"                             | security.instructions.md                    |
| "Commit in Conventional Commits format" | settings.json / commitMessageGeneration     |
| "All Observables unsubscribed"          | angular.instructions.md                     |
