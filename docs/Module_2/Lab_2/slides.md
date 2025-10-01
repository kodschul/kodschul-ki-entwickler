# Lab 2 – Zusammenfassung der Slides

Im zweiten Lab von Modul 2 wird gezeigt, wie LLMs bei der Analyse
und Verbesserung von Code unterstützen können.

* **Laufzeitverbesserung** – Ein Beispiel illustriert, dass eine
  doppelt geschachtelte Schleife zur Duplikaterkennung quadratische
  Laufzeit verursacht. Durch den Einsatz eines Sets lässt sich die
  Aufgabe in linearer Zeit lösen. Die Folien erklären, warum
  Datenstrukturen wie Sets und HashMaps effizienter sind als
  verschachtelte Schleifen.

* **Sicherheit** – Es wird gezeigt, wie einfach sich SQL‑Injection
  einschleichen kann, wenn Benutzer‑Eingaben direkt in SQL‑Strings
  eingebettet werden. Prepared Statements isolieren Parameter vom
  Abfragecode und schützen so vor solchen Angriffen.

* **Modularisierung und Lesbarkeit** – Lange Funktionen lassen sich in
  kleine, gut benannte Helferfunktionen zerlegen. Dies verbessert die
  Wartbarkeit und erleichtert automatisierte Tests. Beispiele zeigen,
  wie man `cleanData`, `splitData`, `toNumbers` und `filterEven`
  definiert und anschließend im Hauptworkflow verwendet.

Die Folien betonen, dass LLMs bei der Codeanalyse unterstützen
können, aber Entwicklerinnen und Entwickler sollten die Vorschläge
kritisch prüfen und bewährte Sicherheits‑ sowie Architekturprinzipien
anwenden.
