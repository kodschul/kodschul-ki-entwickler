# Lab 3 – LLMs in der Praxis einsetzen (Aufgaben)

In diesem Lab üben Sie den praktischen Umgang mit Sprachmodellen. Sie
lernen, wie man Prompts gestaltet, Daten für das Fine‑Tuning
aufbereitet und Befehle zum Starten eines Fine‑Tuning‑Jobs versteht.

1. **Prompt erweitern**\
   Im folgenden Python‑Beispiel wird das OpenAI‑Chat‑API genutzt, um eine
   Zusammenfassung zu erstellen:

   ```python
   import openai

   openai.api_key = "sk-..."  # Demo-Schlüssel

   messages = [
       {"role": "user", "content": "Erstelle eine kurze Zusammenfassung eines Blogartikels über Tests in Rust."}
   ]

   response = openai.ChatCompletion.create(
       model="gpt-3.5-turbo",
       messages=messages,
       temperature=0.7,
   )

   print(response.choices[0].message.content)
   ```

   **Aufgabe:** Ändern Sie den Prompt so, dass das Modell **Schritt für Schritt**
   erklärt, wie es die Zusammenfassung erstellt. Welche
   Prompt‑Engineering‑Techniken (z.B. Zero‑Shot, Few‑Shot) wenden Sie dabei an?

2. **JSONL‑Format erstellen**\
   Konvertieren Sie das folgende Frage‑Antwort‑Set in eine
   JSONL‑Datei. Jede Zeile soll ein JSON-Objekt mit den Feldern
   `prompt` und `completion` enthalten:

   * Frage: *Was ist die Hauptstadt von Frankreich?* – Antwort: *Paris*
   * Frage: *Wer hat die Relativitätstheorie entwickelt?* – Antwort: *Albert Einstein*

   Speichern Sie die zwei Zeilen in der Datei `training_data.jsonl`.

3. **Fine‑Tuning‑Befehle verstehen**\
   Die Folien zeigen zwei Befehle zum Fine‑Tuning eines Modells:

   * `openai tools fine_tunes.prepare_data -f training_data.jsonl`
   * `openai api fine_tunes.create -t training_data_prepared.jsonl -m gpt-3.5-turbo`

   Erklären Sie, wofür diese Befehle verwendet werden und was die
   einzelnen Parameter bedeuten. Beschreiben Sie den Ablauf des
   Fine‑Tuning‑Prozesses in eigenen Worten.
