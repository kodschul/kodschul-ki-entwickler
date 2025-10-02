# Lösungen – Lab 4.2 Konzept & Architektur

1. **E‑Commerce‑Architektur (Node):**

```js
import OpenAI from "openai";
import dotenv from "dotenv";
dotenv.config();
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const prompt = `Du bist Software‑Architekt. Entwirf eine 3‑Schichten‑Architektur für ein E‑Commerce‑System. Beschreibe die Präsentationsschicht (z.B. Web‑Shop UI), die Serviceschicht (z.B. Warenkorb‑Service, Payment‑Service, Bestellverwaltung) und die Datenhaltung (z.B. relationales DBMS).`;
async function main() {
  const res = await client.chat.completions.create({
    model: "gpt-4.1",
    messages: [ { role: "user", content: prompt } ],
    temperature: 0.5,
  });
  console.log(res.choices[0].message.content.trim());
}
main();
```

Die Antwort beschreibt typischerweise, dass die Präsentationsschicht Web‑ oder Mobile‑Frontends umfasst, die Serviceschicht REST‑APIs für Warenkorb‑ und Zahlungsprozesse bereitstellt, und die Datenebene Produkt‑ und Bestelldaten speichert.

2. **OpenAPI‑Spezifikation (Python):**

```python
from openai import OpenAI
client = OpenAI()
prompt = """Du bist API‑Designer. Schreibe eine OpenAPI‑3.0‑Spezifikation (YAML) für eine Bibliotheks‑API. Die API soll folgende Endpunkte haben:\n- GET /books: Liste aller Bücher mit Feldern id, title, author, available (boolean).\n- POST /books: Ein neues Buch anlegen.\n- POST /borrow: Ein Buch ausleihen (Parameter: book_id, user_id).\n- POST /return: Ein Buch zurückgeben.\nBeschreibe Schemas und Responses."""
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
)
print(completion.choices[0].message.content)
```

Das Modell erzeugt ein YAML‑Dokument mit Definitionen für `/books`, `/borrow` und `/return`, inklusive Parameter und Antwortstrukturen.

3. **Design‑Pattern Prompts:**

*Singleton (Python) Prompt*

> "Schreibe eine Python‑Klasse `DBConnection` nach dem Singleton‑Pattern. Verwende snake_case für Methoden und Docstrings zur Dokumentation. Die Klasse soll eine Methode `get_instance()` bereitstellen, die immer dieselbe Instanz zurückgibt, sowie eine Methode `connect()` zur Herstellung der Verbindung."

*Factory (TypeScript) Prompt*

> "Implementiere eine TypeScript‑Klasse `VehicleFactory` nach dem Factory‑Pattern. Nutze camelCase für Methoden und füge JSDoc‑Kommentare hinzu. Die Factory soll abhängig vom übergebenen Typ (`'car'`, `'truck'`) eine Instanz der Klassen `Car` bzw. `Truck` erzeugen."

Mit diesen Prompts erzeugt das Modell vollständige Klassen mit den gewünschten Namenskonventionen und Kommentaren.
