# Aufgaben – Lab 4.3 Coding‑Stile & Design‑Patterns

1. **Code‑Refactoring mit AI:** Die Datei `fabrik.py` enthält den folgenden unformatierten Python‑Code:

```python
def makemilkshake(flavor,size):return "{}-{}".format(size,flavor)
```

Erstelle einen Prompt für ein Sprachmodell, der diesen Code gemäß PEP 8 formatiert, Methoden in snake_case benennt und einen Docstring mit Beschreibung und Parametern hinzufügt.  Führe das Modell mit deinem Prompt aus und zeige den verbesserten Code.

2. **TypeScript‑Factory:** Schreibe eine Aufforderung an ein LLM, das eine TypeScript‑Klasse `ProductService` nach dem Factory‑Pattern generiert.  Die Klasse soll Methoden in camelCase verwenden und JSDoc‑Kommentare enthalten.  Implementiere anschließend ein Node‑Script, das mit dem OpenAI‑SDK diesen Prompt an `gpt-4.1` sendet und die Antwort ausgibt.

3. **Singleton korrigieren:** Das folgende Java‑Snippet implementiert kein echtes Singleton:

```java
public class Config {
    public static Config instance = new Config();
    public Config() {}
}
```

Erläutere, warum dies problematisch ist, und schreibe mithilfe des Singleton‑Patterns eine korrekte Version der Klasse.  Verwende außerdem Doc‑Kommentare, um den Zweck der Klasse zu beschreiben.
