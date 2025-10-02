# Aufgaben – Lab 4.2 Konzept & Architektur

1. **E‑Commerce‑Architektur:** Erstelle ein Node‑Script, das mit dem OpenAI‑SDK eine dreischichtige Architektur für ein E‑Commerce‑System entwirft.  Dein Prompt soll die Schichten (Präsentation, Service, Daten) benennen und typische Komponenten (z. B. Warenkorb, Zahlungsmodule) verlangen.  Gib die Antwort der KI aus.

2. **OpenAPI‑Spezifikation:** Schreibe ein Python‑Programm, das über das OpenAI‑API eine OpenAPI‑3.0‑Spezifikation für ein Bibliotheks‑Verwaltungssystem generiert.  Die API soll Endpunkte zum Auflisten aller Bücher (`GET /books`), Hinzufügen eines Buches (`POST /books`), Ausleihen (`POST /borrow`) und Zurückgeben (`POST /return`) enthalten.  Fordere das Modell auf, Titel, Autor und Verfügbarkeit zu dokumentieren.

3. **Design‑Patterns per Prompt:** Formuliere zwei Prompts, mit denen du einen LLM anweist, eine Klasse in Python nach dem Singleton‑Pattern und eine Klasse in TypeScript nach dem Factory‑Pattern zu implementieren.  Definiere für Python, dass `snake_case` und Docstrings verwendet werden sollen; für TypeScript `camelCase` und JSDoc‑Kommentare.  Überlege, welche Informationen (z. B. Klassenname, Funktionen) der Prompt enthalten muss.
