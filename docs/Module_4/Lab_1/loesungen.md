# Lösungen – Lab 4.1 Requirements Engineering mit KI

1. **Use‑Cases generieren (Node):**

```js
// installiere mit: npm install openai dotenv
import OpenAI from "openai";
import * as dotenv from "dotenv";
dotenv.config();
const client = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const systemPrompt = `Du bist Requirements‑Ingenieur für ein Inventarverwaltungssystem. Generiere fünf Use‑Cases, fünf User‑Stories und passende Akzeptanzkriterien.`;
async function run() {
  const completion = await client.chat.completions.create({
    model: "gpt-4.1",
    messages: [ { role: "user", content: systemPrompt } ],
    temperature: 0.7,
  });
  console.log(completion.choices[0].message.content.trim());
}
run();
```

Die Ausgabe enthält stichpunktartige Use‑Cases (z. B. *Artikel anlegen*, *Bestand prüfen*), dazugehörige User‑Stories im Format *Als Lagerverwalter …* und konkrete Akzeptanzkriterien.

2. **User‑Story bewerten (Python):**

```python
from openai import OpenAI
import os
client = OpenAI()
with open("story.txt", "r", encoding="utf-8") as f:
    story = f.read().strip()
prompt = f"Bewerte diese User Story und formuliere verbesserte Akzeptanzkriterien:\n{story}"
completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[{"role": "user", "content": prompt}],
)
print(completion.choices[0].message.content)
```

Wenn die `story.txt` z.B. den Text

```
Als Benutzer möchte ich Artikel aus dem Lager ausbuchen, damit der Bestand korrekt bleibt.
```

enthält, generiert das Modell typische Verbesserungen wie *Berücksichtigung von Benutzerrollen* und konkrete Akzeptanzkriterien (z. B. Eingabevalidierung, Bestandsabgleich).

3. **WolframAlpha‑Abfrage:**

```python
import requests
import os
app_id = os.environ["WOLFRAM_APP_ID"]
query = "Anzahl Arbeitstage von 1. Oktober 2025 bis 15. Oktober 2025"
params = {"input": query, "appid": app_id, "output": "JSON"}
res = requests.get("https://api.wolframalpha.com/v2/query", params=params)
json_data = res.json()
# Suche das erste Pod mit Resultaten
pods = json_data.get("queryresult", {}).get("pods", [])
for pod in pods:
    if pod.get("title", "").lower().startswith("result"):
        subpods = pod.get("subpods", [])
        if subpods:
            print(subpods[0].get("plaintext"))
            break
```

Die Antwort von WolframAlpha enthält die Zahl der Werktage in dem gegebenen Zeitraum.  Dieses Skript extrahiert den Text aus dem *Result*-Pod der JSON‑Antwort.
