# Lösungen – Lab 4.3 Coding‑Stile & Design‑Patterns

1. **Code‑Refactoring mit AI:**

*Prompt*

> "Formatiere den folgenden Python‑Code gemäß PEP 8, verwende snake_case für Funktionsnamen und füge einen Docstring hinzu, der den Zweck und die Parameter erklärt:\n\n`def makemilkshake(flavor,size):return "{}-{}".format(size,flavor)`"

*Antwort des Modells*

```python
def make_milkshake(flavor: str, size: str) -> str:
    """Erzeugt den Namen eines Milchshakes.

    Args:
        flavor: Geschmack, z. B. "Vanille" oder "Schokolade".
        size: Größe wie "klein", "mittel" oder "groß".

    Returns:
        Kombinierter Name aus Größe und Geschmack.
    """
    return f"{size}-{flavor}"
```

2. **TypeScript‑Factory:**

*Prompt*

> "Schreibe eine TypeScript‑Klasse `ProductService` nach dem Factory‑Pattern.  Verwende camelCase für Methoden und füge JSDoc‑Kommentare hinzu.  Die Factory‑Methode `createProduct` soll abhängig vom Typ eine Instanz der Klassen `Book` oder `Toy` erzeugen."

*Node‑Script*

```js
import OpenAI from "openai";
import dotenv from "dotenv";
dotenv.config();
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const prompt = `Schreibe eine TypeScript-Klasse ProductService nach dem Factory-Pattern. Verwende camelCase für Methoden und füge JSDoc-Kommentare hinzu. Die Factory-Methode createProduct soll abhängig vom Typ eine Instanz der Klassen Book oder Toy erzeugen.`;
(async () => {
  const res = await client.chat.completions.create({
    model: "gpt-4.1",
    messages: [ { role: "user", content: prompt } ],
  });
  console.log(res.choices[0].message.content);
})();
```

Die KI erzeugt eine Klasse mit `createProduct(type: string): Book | Toy` und JSDoc‑Kommentaren für Klasse und Methoden.

3. **Singleton korrigieren:**

Das ursprüngliche Beispiel ist problematisch, weil der Konstruktor öffentlich ist und weitere Instanzen erstellt werden können; außerdem ist die Instanz nicht thread‑sicher.  Eine korrekte Singleton‑Implementierung verbirgt den Konstruktor und stellt eine statische Zugriffsmethode bereit:

```java
/**
 * Konfigurations‑Singleton: stellt eine einzige Instanz zur Verfügung und lädt Einstellungen nur einmal.
 */
public class Config {
    private static Config instance;
    private Config() {
        // z. B. Laden von Konfigurationsdateien
    }
    public static synchronized Config getInstance() {
        if (instance == null) {
            instance = new Config();
        }
        return instance;
    }
    // weitere Methoden ...
}
```

Diese Version versteckt den Konstruktor (private) und gibt die Instanz über die statische Methode `getInstance()` zurück【977489249547423†L52-L59】.
