# Lab 1 – Zusammenfassung der Slides

Die Folien zum ersten Lab in Modul 3 zeigen, wie man mit Hilfe von
Sprachmodellen Testfälle generiert:

* Für eine einfache Funktion wie `is_even` erstellt das Modell
  automatisch mehrere **pytest‑Tests**, die unterschiedliche Eingaben
  abdecken (positive Zahlen, Null, ungerade Zahlen). Das Beispiel
  verdeutlicht, wie ein präziser Prompt zu vollständigen Testfällen
  führt.

* Die Folien erwähnen zudem, dass LLMs andere Testframeworks wie
  **JUnit**, **pytest** oder **Jest** kennen und zielgerichtete Tests
  generieren können. In einem Beispiel werden mehrere Java‑Tests
  mittels JUnit und mehrere JavaScript‑Tests mittels Jest erzeugt.

* Es wird hervorgehoben, dass Prompts präzise formuliert werden
  sollten (zum Beispiel gewünschtes Framework, Anzahl der Tests,
  besondere Randfälle). LLMs dienen als nützlicher Ausgangspunkt, die
  generierten Tests müssen aber manuell überprüft und ergänzt
  werden.
