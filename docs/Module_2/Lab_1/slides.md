# Lab 1 – Zusammenfassung der Slides

Die Folien zum ersten Lab von Modul 2 zeigen, wie LLMs beim
Programmieren unterstützen können. Es werden konkrete Beispiele
demonstriert:

* Eine **Python‑Funktion zur E‑Mail‑Validierung** nutzt einen regulären
  Ausdruck, um zu prüfen, ob ein `@` und ein Domain‑Teil vorhanden
  sind. Das Beispiel zeigt auch, wie man mit ChatGPT einen
  Docstring generiert.

* Mittels **Pytest** können automatisch Testfunktionen erstellt
  werden. Im Beispiel werden verschiedene Eingaben an die Funktion
  übergeben, und `assert`‑Anweisungen prüfen die erwarteten
  Rückgabewerte. Die Folien machen deutlich, dass Tests auch Randfälle
  abdecken sollten (fehlendes `@`, fehlender Domain‑Teil).

* Eine **TypeScript‑Funktion `groupBy`** gruppiert Elemente einer
  Liste nach einem durch eine Callback‑Funktion bestimmten Schlüssel.
  Der zugehörige JSDoc‑Kommentar erläutert den Zweck der Funktion,
  beschreibt Typparameter, Parameter und Rückgabewert und hilft so
  zukünftigen Nutzerinnen und Nutzern beim Verständnis.

Darüber hinaus werden allgemeine Empfehlungen zum Debugging gegeben,
zum Beispiel systematisch nach der Ursache eines Fehlers zu suchen und
Ausgaben des LLMs kritisch zu hinterfragen.
