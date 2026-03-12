# Lab 4.1 – Software Testing mit Generativer KI

## Szenario

Du bist neu in einem Team, das eine **Aufgabenverwaltungs-API** (Task Management)
entwickelt hat. Die Anwendung ist funktionsfähig – aber die Testabdeckung ist
praktisch nicht vorhanden. Der Tech Lead hat klargemacht: Bevor neue Features
entwickelt werden dürfen, müssen die kritischen Kernfunktionen durch Unit Tests
abgesichert sein.

Deine Aufgabe: Schreibe umfassende Tests für die bestehende Logik – mithilfe
des KI-Assistenten.

---

## Projekt-Überblick

Eine Task-Management-Anwendung mit Aufgaben, Projekten und Benutzern.

```
Project/
├── src/
│   ├── TaskService.ts        ← Kernlogik – soll getestet werden
│   ├── ProjectService.ts     ← Projekt-Logik – soll getestet werden
│   ├── UserService.ts        ← Nutzer-Verwaltung – soll getestet werden
│   ├── models/
│   │   ├── Task.ts
│   │   ├── Project.ts
│   │   └── User.ts
│   └── utils/
│       └── dateUtils.ts      ← Hilfsfunktionen – einfach zu testen
├── tests/
│   └── example.test.ts       ← Nur ein Beispiel-Test zum Orientieren
├── jest.config.js
├── package.json
└── tsconfig.json
```

---

## Lernziele

- Unit Tests mit Jest schreiben
- KI zur Testgenerierung einsetzen
- Edge Cases und Fehlerfälle identifizieren
- Testabdeckung erhöhen und interpretieren
- Mocks und Test-Doubles nutzen

---

## Aufgaben

### Aufgabe 1 – Bestehenden Code verstehen (10 Min.)

Lies zunächst alle Dateien unter `src/` durch.

Nutze den **KI-Chat**, um folgende Fragen zu klären:

1. *„Erkläre mir die Methoden in TaskService und welche Randfälle es geben könnte."*
2. *„Welche Methoden in ProjectService sind am kritischsten und warum?"*
3. Erstelle eine kurze Liste, welche Methoden du testen willst (priorisiere!).

---

### Aufgabe 2 – Tests für `dateUtils.ts` generieren (15 Min.)

`dateUtils.ts` enthält reine Funktionen – ideal für den Einstieg ins Testen.

Nutze die KI (Edit-Modus oder Chat), um Tests zu generieren:

1. Erstelle `tests/dateUtils.test.ts`
2. Die Tests sollen abdecken:
   - Normalfälle (typische gültige Eingaben)
   - Randfälle (Jahreswechsel, 29. Februar, etc.)
   - Fehlerfälle (null, undefined, ungültige Daten)
3. Führe die Tests aus: `npm test`

> **Tipp:** Zeige der KI die Quelldatei und nutze den Prompt:  
> *„Generiere Jest Unit Tests für alle Funktionen in dieser Datei.
> Decke Normalfälle, Randfälle und Fehlerfälle ab."*

---

### Aufgabe 3 – Tests für `TaskService.ts` generieren (20 Min.)

`TaskService` ist die Kernkomponente. Erstelle `tests/TaskService.test.ts`.

Anforderungen:
- Teste `createTask`, `updateTask`, `deleteTask`, `getTasksByProject`
- Teste Fehlerszenarien (Task nicht gefunden, ungültige Daten)
- Teste den Statuswechsel-Workflow (OPEN → IN_PROGRESS → DONE)
- Verwende `beforeEach`, um einen frischen Service-State zu erstellen

> **Tipp:** Prompt:  
> *„Erstelle Jest Unit Tests für TaskService. Nutze beforeEach für den Setup.
> Decke Fehlerszenarien und Statusübergänge ab."*

---

### Aufgabe 4 – Edge Cases identifizieren (15 Min.)

Nachdem du erste Tests generiert hast: Lass die KI nach weiteren Edge Cases suchen.

Frage die KI:
1. *„Welche Edge Cases in TaskService könnten zu Fehlern führen, die ich noch nicht getestet habe?"*
2. *„Gibt es Szenarien mit leeren Listen, null-Werten oder gleichzeitigen Operationen?"*
3. Füge mindestens 5 neue Test-Cases hinzu, die du ohne KI nicht gefunden hättest.

---

### Aufgabe 5 – Tests für `ProjectService.ts` und Mocks (15 Min.)

`ProjectService` hängt von `TaskService` ab – teste ihn mit einem Mock.

Erstelle `tests/ProjectService.test.ts`:

1. Erstelle einen Mock für `TaskService` mit `jest.fn()`.
2. Teste, dass `deleteProject` auch alle zugehörigen Tasks löscht.
3. Teste, dass Statistik-Methoden korrekte Werte zurückgeben.

> **Tipp:** Prompt:  
> *„Erstelle einen Jest Mock für TaskService und nutze ihn in Tests für
> ProjectService. Die Abhängigkeit soll als Mock injiziert werden."*

---

### Aufgabe 6 – Testabdeckung messen und erhöhen (10 Min.)

Führe die Tests mit Coverage aus:

```bash
npm run test:coverage
```

1. Öffne den Coverage-Report (in `coverage/lcov-report/index.html`).
2. Identifiziere Methoden mit < 80% Coverage.
3. Nutze KI, um die fehlenden Tests zu generieren.

> **Tipp:** Prompt:  
> *„Folgende Zeilen in TaskService wurden noch nicht durch Tests abgedeckt:
> [Zeilen einfügen]. Generiere Tests, die diese Pfade abdecken."*

---

## Erwartetes Ergebnis

- ✅ `tests/dateUtils.test.ts` – mind. 8 Tests
- ✅ `tests/TaskService.test.ts` – mind. 12 Tests inkl. Edge Cases
- ✅ `tests/ProjectService.test.ts` – mind. 6 Tests mit Mocks
- ✅ Alle Tests laufen grün durch (`npm test`)
- ✅ Gesamt-Coverage ≥ 80% (`npm run test:coverage`)
- ✅ Mindestens einen Test, den du ohne KI nicht gefunden hättest (kommentiert)

---

## Hinweise zum KI-Einsatz

| Aufgabe                    | Empfohlener Modus | Beispiel-Prompt                                                                  |
|----------------------------|-------------------|----------------------------------------------------------------------------------|
| Edge Cases finden          | Ask / Chat        | „Welche Edge Cases könnte ich in dieser Methode testen?"                         |
| Tests generieren           | Edit / Chat       | „Generiere Jest Tests für diese Funktion mit Normalfall und Fehlerfällen"        |
| Mock erstellen             | Edit              | „Erstelle einen Jest Mock für diese Klasse"                                      |
| Coverage-Lücken schließen  | Edit mit Kontext  | „Diese Zeilen haben keine Testabdeckung – generiere Tests dafür"                 |
| Test-Qualität verbessern   | Ask               | „Sind meine Tests gut? Was fehlt? Prüfe auf fehlende Assertions"                 |

---

## Nützliche Befehle

```bash
npm install         # Abhängigkeiten installieren
npm test            # Alle Tests ausführen
npm run test:watch  # Tests im Watch-Modus
npm run test:coverage # Tests mit Coverage-Report
```
