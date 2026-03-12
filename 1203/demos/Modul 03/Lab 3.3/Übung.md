# Lab 3.3 – Refactoring mit KI-Unterstützung

## Szenario

Du arbeitest als Senior-Entwickler in einem Fintech-Startup. Das Team hat in den
letzten Monaten schnell einen **Zahlungsverarbeitungs-Service** entwickelt,
um einen Marktdeadline zu treffen. Der Code funktioniert – aber jeder neue
Feature-Wunsch dauert immer länger, weil die Codebasis schwer verständlich und
kaum wartbar ist.

Deine Aufgabe ist es, den Code zu analysieren, Code-Smells zu identifizieren
und eine gezielte Refactoring-Kampagne durchzuführen – mit Hilfe des KI-Assistenten.

---

## Projekt-Überblick

Ein Zahlungsservice in TypeScript, der Zahlungen verarbeitet, Rabatte berechnet
und Rechnungen erstellt.

```
Project/
├── src/
│   ├── PaymentProcessor.ts   ← God Class, 400+ Zeilen, alles drin
│   ├── types.ts              ← Typdefinitionen
│   └── index.ts              ← Demo-Nutzung
├── package.json
└── tsconfig.json
```

---

## Lernziele

- Code-Smells mit KI erkennen und beschreiben
- Refactoring-Strategien ableiten
- Design Patterns anwenden (Strategy, Single Responsibility)
- Code sicherer, lesbarer und testbarer machen

---

## Code-Smells im Projekt (nicht verraten!)

Der Code enthält absichtlich folgende Probleme – finde sie selbst mithilfe der KI:

- God Class (eine Klasse macht alles)
- Zu lange Methoden (>50 Zeilen)
- Magic Numbers ohne Bezeichnung
- Copy-Paste-Duplikate in der Rabattlogik
- Kryptische Variablennamen
- Fehlende Abstraktion für Payment-Provider-spezifischen Code
- Switch-Statement das nach Open/Closed-Prinzip verletzt
- Primitive Obsession (rohe Strings/Numbers statt Typen)

---

## Aufgaben

### Aufgabe 1 – Code-Smells identifizieren (15 Min.)

Öffne `src/PaymentProcessor.ts`. Nutze den **KI-Chat (Ask-Modus)**:

1. Frage: *„Analysiere diese Datei und liste alle Code-Smells auf."*
2. Frage: *„Welche SOLID-Prinzipien werden hier verletzt?"*
3. Erstelle eine eigene Liste der gefundenen Probleme.

> **Tipp:** Lies den Code zunächst selbst durch, dann vergleiche deine
> Einschätzung mit der KI-Analyse.

---

### Aufgabe 2 – God Class aufteilen (25 Min.)

`PaymentProcessor` macht viel zu viel. Teile ihn auf:

Nutze KI (Edit-Modus), um folgende Klassen zu extrahieren:

1. **`DiscountCalculator`** – enthält nur Rabattlogik
2. **`InvoiceGenerator`** – enthält nur Rechnungserstellung
3. **`PaymentValidator`** – enthält nur Validierungslogik
4. **`PaymentProcessor`** (schlanker) – orchestriert die anderen Klassen

> **Tipp:** Markiere zusammengehörige Methoden und frage die KI:  
> *„Extrahiere diese Methoden in eine separate Klasse mit dem Namen DiscountCalculator."*

---

### Aufgabe 3 – Magic Numbers durch Konstanten ersetzen (10 Min.)

Im Code gibt es viele Zahlen wie `0.19`, `0.07`, `0.10`, `5000`, `0.15`.

1. Identifiziere alle Magic Numbers mithilfe der KI.
2. Erstelle eine Datei `constants.ts` mit aussagekräftigen Konstanten.
3. Ersetze alle Magic Numbers im Code.

> **Tipp:** Prompt: *„Identifiziere alle Magic Numbers in diesem Code und
> schlage Konstantennamen vor."*

---

### Aufgabe 4 – Switch-Statement durch Strategy-Pattern ersetzen (20 Min.)

In `processPayment` gibt es ein großes `switch`-Statement über den Provider-Typ.

Nutze KI, um ein **Strategy Pattern** zu implementieren:

1. Erstelle ein Interface `IPaymentStrategy` mit einer Methode `process`.
2. Implementiere `CreditCardStrategy`, `PayPalStrategy`, `BankTransferStrategy`.
3. Ersetze das switch-Statement durch eine Strategy-Factory.

> **Tipp:** Zeige der KI das switch-Statement und frage:  
> *„Refaktoriere diesen Code mit dem Strategy Pattern. Erstelle ein
> IPaymentStrategy-Interface und je eine Implementierung pro Case."*

---

### Aufgabe 5 – Lange Methode aufteilen (15 Min.)

Die Methode `processAndGenerateInvoice` ist über 60 Zeilen lang.

1. Identifiziere logische Abschnitte mit KI-Hilfe.
2. Extrahiere private Hilfsmethoden.
3. Die öffentliche Methode soll danach maximal 15 Zeilen haben.

> **Tipp:** Prompt: *„Diese Methode ist zu lang. Teile sie in kleinere,
> sprechend benannte Methoden auf. Jede Methode soll genau eine Aufgabe haben."*

---

### Aufgabe 6 – Umbenennung kryptischer Variablen (10 Min.)

Suche alle kurzen, nichtssagenden Variablennamen (`d`, `p`, `amt`, `tx`, `res`).

Nutze KI, um bessere Namen vorzuschlagen und alle Vorkommen umzubenennen.

> **Tipp:** Prompt: *„Schlage für jede Variable einen beschreibenden Namen vor,
> der den Zweck der Variable im Kontext dieser Methode erklärt."*

---

## Erwartetes Ergebnis

- ✅ `PaymentProcessor.ts` unter 80 Zeilen
- ✅ Mindestens 3 neue Klassen/Dateien aus der God Class extrahiert
- ✅ Alle Magic Numbers durch benannte Konstanten ersetzt
- ✅ Strategy Pattern für Payment-Provider implementiert
- ✅ Keine Methode mehr länger als 20 Zeilen
- ✅ Alle Variablennamen sind aussagekräftig

---

## Hinweise zum KI-Einsatz

| Aufgabe                     | Empfohlener Modus   | Beispiel-Prompt                                                             |
|-----------------------------|---------------------|-----------------------------------------------------------------------------|
| Code-Smells finden          | Ask / Chat          | „Analysiere diesen Code und liste alle Code-Smells auf"                     |
| SOLID-Verletzungen erkennen | Ask                 | „Welche SOLID-Prinzipien werden in dieser Klasse verletzt?"                 |
| Klasse extrahieren          | Edit / Inline-Chat  | „Extrahiere diese Methoden in eine separate Klasse"                         |
| Strategy Pattern            | Edit                | „Refaktoriere dieses switch mit Strategy Pattern"                           |
| Methode aufteilen           | Edit / Inline-Chat  | „Teile diese Methode in kleinere Methoden auf – eine Aufgabe pro Methode"   |
| Umbenennen                  | Edit / Rename       | „Schlage bessere Variablennamen für diesen Code vor"                        |
