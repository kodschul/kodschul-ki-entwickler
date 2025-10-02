# Lab 4.1 – Requirements Engineering mit KI beschleunigen

In dieser Lab-Einheit lernst du, wie generative KI-Modelle wie GPT‑4 bei der Anforderungserhebung unterstützen können.  Generative Modelle erzeugen eigene Inhalte, indem sie aus großen Datenmengen Muster lernen【626807851092106†L51-L55】.  Sie zerteilen Eingaben in **Token** (Textstücke wie Wörter oder Subwörter)【626807851092106†L95-L105】 und projizieren diese in einen semantischen Vektorraum (Embeddings)【626807851092106†L114-L119】, damit das Modell inhaltliche Zusammenhänge erkennen kann.  Dank RLHF‑Feinabstimmung können Modelle hilfreicher und sicherer auf menschliche Anfragen reagieren【199146385693552†L90-L100】.

## Codebeispiele aus den Folien

### Use‑Case‑Generator (Node JS)
Das folgende Script aus den Slides zeigt, wie mit dem offiziellen OpenAI‑SDK Use‑Cases, User‑Stories und Akzeptanzkriterien für ein Online‑Banking‑System generiert werden.  Es erstellt einen Prompt und ruft das Chat‑Completion‑API von GPT‑4.1 auf.

```js
import OpenAI from "openai";
import * as dotenv from "dotenv";
dotenv.config();
const openai = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const prompt = `Du bist ein Requirements-Ingenieur. Erstelle 3 Use-Cases, 3 User-Stories und Akzeptanzkriterien für ein Online-Banking-System.`;
const response = await openai.chat.completions.create({
  model: "gpt-4.1",
  messages: [ { role: "user", content: prompt } ],
});
console.log(response.choices[0].message.content);
```

### User‑Story‑Review (Python)
In einem weiteren Beispiel wird eine vorhandene User‑Story analysiert und Verbesserungsvorschläge erzeugt.  Die `openai`‑Bibliothek liest den API‑Schlüssel aus der Umgebungsvariablen und sendet eine Chat‑Nachricht.

```python
from openai import OpenAI
import os
client = OpenAI()
story = "Als Kunde möchte ich eine Überweisung tätigen, um Rechnungen zu bezahlen."
prompt = f"Überprüfe diese User Story und schlage Verbesserungen vor:\n{story}"
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
)
print(completion.choices[0].message.content)
```

### WolframAlpha‑API nutzen
Die Slides enthielten auch ein Beispiel, wie externe APIs in den Anforderungsprozess integriert werden können.  Mit der [WolframAlpha‑API](https://api.wolframalpha.com) kann man z. B. Berechnungen durchführen.  Der API‑Schlüssel wird über `app_id` übergeben.  Danach wird das Ergebnis als JSON gedruckt.

```python
import requests
app_id = "DEIN_APP_ID"
query = "Arbeitszeit von 1. Januar 2025 bis 1. Februar 2025"
params = {"input": query, "appid": app_id, "output": "JSON"}
res = requests.get("https://api.wolframalpha.com/v2/query", params=params)
print(res.json())
```

Nutze diese Beispiele als Vorlage, um die folgenden Aufgaben zu lösen.
