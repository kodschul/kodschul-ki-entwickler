# Lab 3 – Zusammenfassung der Slides

Im dritten Lab des Moduls 3 erfahren Sie, wie LLMs Tests für
verschiedene Frameworks generieren können:

* **JUnit** – Die Folien demonstrieren, dass ein LLM korrekte
  JUnit‑Testmethoden schreiben kann, indem Parameterwerte und
  erwartete Ergebnisse vorgegeben werden. Import‑Anweisungen und
  `assertEquals` werden automatisch ergänzt.

* **Jest** – Für JavaScript‑Funktionen werden Jest‑Tests erstellt,
  die sowohl normale als auch Randfälle abdecken (zum Beispiel null,
  undefined, ungewöhnliche Zeichenfolgen).

* **Integrationstests** – Es wird gezeigt, wie man mit Python und
  `subprocess` ein CLI‑Programm aufruft und die Ausgabe verifiziert.
  Integrationstests betrachten das Gesamtsystem und ergänzen Unit‑Tests,
  die nur einzelne Funktionen prüfen.

Die Folien unterstreichen, dass LLMs unterschiedliche Sprachen und
Testframeworks kennen. Durch präzise Prompts lassen sich schnell
grundlegende Testgerüste erzeugen, die anschließend manuell
verfeinert werden sollten.
