# Lab 4.2 – Konzept‑ und Architekturentwürfe mit KI denken

LLMs können mehr als nur Text generieren – sie lassen sich auch als *Sparringspartner* für Software‑Architekturen einsetzen.  Durch eine gezielte Beschreibung des gewünschten Systems lassen sich Komponenten, Schichten und Schnittstellen entwerfen.  Dabei hilft es, die Sprachmodelle mit **Prompt‑Engineering** anzuleiten.  Beim *Zero‑Shot‑Prompting* wird nur die Aufgabe gestellt, beim *Few‑Shot* werden Beispiele mitgegeben【626807851092106†L164-L175】.

## Codebeispiele aus den Folien

### Architektur‑Generator (Node JS)

```js
import OpenAI from "openai";
import dotenv from "dotenv";
dotenv.config();
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const prompt = `Entwirf eine dreischichtige Architektur (Präsentations‑, Geschäfts‑ und Datenebene) für ein E‑Learning‑Portal. Beschreibe pro Schicht die Hauptkomponenten und deren Aufgaben.`;
const result = await client.chat.completions.create({
  model: "gpt-4.1",
  messages: [ { role: "user", content: prompt } ],
});
console.log(result.choices[0].message.content);
```

Dieser Code generiert eine Beschreibung der Präsentationsschicht (z. B. Web‑Frontend), der Geschäftslogik (Kurse, Prüfungen, Benutzerverwaltung) und der Datenbankebene.

### OpenAPI‑Spezifikation generieren (Python)

```python
from openai import OpenAI
client = OpenAI()
prompt = """Du bist ein API‑Designer. Schreibe eine OpenAPI‑3.0‑Spezifikation für eine Blog‑API mit Endpunkten zum Anlegen, Lesen, Aktualisieren und Löschen von Beiträgen. Nutze YAML‑Format und beschreibe die Felder titel (String), inhalt (String) und autor (String)."""
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
)
print(completion.choices[0].message.content)
```

Die AI erstellt ein YAML‑Dokument mit `openapi: 3.0.0`, definiert `paths` für CRUD‑Operationen und beschreibt Datenstrukturen.

### Design‑Pattern und Stilvorgaben per Prompt
Um konsistente Code‑Vorschläge zu erhalten, kann man das Modell mit Style‑Guidelines füttern.  Ein Beispiel aus den Slides fordert z. B.:

> *"Schreibe eine TypeScript‑Klasse `UserService` mit camelCase‑Methoden, verwende das Factory‑Pattern und füge JSDoc‑Kommentare hinzu."*

Das Modell produziert daraufhin eine Klasse mit Konstruktor, Factory‑Methode und Dokumentation.  In einem anderen Beispiel wird das Singleton‑Pattern in Python mit snake_case und Docstrings umgesetzt.  Der Singleton stellt sicher, dass eine Klasse nur eine Instanz besitzt und einen globalen Zugriffspunkt bietet【977489249547423†L8-L12】; die Implementierung nutzt einen privaten Konstruktor und eine statische Methode zur Instanzierung【977489249547423†L52-L59】.
