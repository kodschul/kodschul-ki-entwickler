# Lab 3 – Zusammenfassung der Slides

Die Folien dieses Labs zeigen, wie man Code durch Refactoring und
Optimierung verbessert:

* **Rekursive Funktionen** können bei großen Argumenten zu
  Stacküberläufen führen. Eine iterative Variante vermeidet
  übermäßigen Speicherverbrauch und ist oft effizienter.

* **Duplizierten Code** gilt es zu vermeiden. Wiederverwendbare
  Funktionen kapseln gemeinsam genutzte Logik und erleichtern die
  Wartung.

* **Fehlerbehandlung** – Ressourcen wie Dateien sollten mit
  Kontextmanagern geöffnet werden, damit sie bei Ausnahmen
  garantiert geschlossen werden. Zudem sollten mögliche
  Fehlersituationen (Datei fehlt, Lesefehler) explizit behandelt
  werden.

Die Beispiele verdeutlichen, dass LLM‑Empfehlungen als Ausgangspunkt
für Refactoring dienen können, der finale Code aber einer
Qualitätssicherung durch Entwicklerinnen und Entwickler bedarf.
