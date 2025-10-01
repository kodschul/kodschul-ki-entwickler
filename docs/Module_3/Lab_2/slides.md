# Lab 2 – Zusammenfassung der Slides

Die Folien zum zweiten Lab veranschaulichen, wie LLMs Edge Cases und
Fehlerpfade identifizieren können:

* **Einfacher Code als Beispiel** – Eine Divisionsfunktion zeigt,
  dass Division durch Null zu einer Ausnahme führt. LLMs sollen
  entsprechende Testfälle vorschlagen.

* **Fehlerpfade in API‑Funktionen** – Eine `getUser`‑Funktion
  demonstriert unterschiedliche Rückgabewerte (Fehler, null, Objekt).
  LLMs können anhand der Bedingungszweige passende Tests generieren.

* **Sicherheitskritische Bereiche** – Bei Login‑Funktionen wird
  vorgeschlagen, Tests für leere Eingaben, ungewöhnlich lange
  Eingaben und Injection‑ähnliche Strings zu generieren. Die Folien
  betonen, dass LLMs oft kreative Vorschläge machen, diese aber
  immer fachlich geprüft werden müssen.
