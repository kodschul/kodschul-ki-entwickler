# Lab 3 – Lösungen

1. **Prompt erweitern**\
   Um das Modell zu einer Schritt‑für‑Schritt‑Erklärung zu bewegen, kann
   man den Prompt explizit um diese Anweisung ergänzen, zum Beispiel:

   > "Erstelle eine kurze Zusammenfassung eines Blogartikels über Tests in Rust **und erkläre Schritt für Schritt, wie du die wichtigsten Informationen auswählst und organisierst**."

   Diese Formulierung nutzt **Zero‑Shot‑Prompting** (keine
   Beispielantworten) kombiniert mit der **Chain‑of‑Thought**‑Strategie,
   bei der das Modell aufgefordert wird, sein Vorgehen zu erläutern. Bei
   Bedarf könnte man auch **Few‑Shot‑Prompting** einsetzen, indem man
   Beispiel‑Paare aus Frage und gewünschter Schritt‑für‑Schritt‑Antwort
   voranstellt【626807851092106†L164-L175】.

2. **JSONL‑Format erstellen**\
   Der Inhalt der Datei `training_data.jsonl` könnte folgendermaßen
   aussehen (jede Zeile ist ein gültiges JSON-Objekt):

   ```jsonl
   {"prompt": "Was ist die Hauptstadt von Frankreich?", "completion": "Paris"}
   {"prompt": "Wer hat die Relativitätstheorie entwickelt?", "completion": "Albert Einstein"}
   ```

   JSONL steht für **JSON Lines**; jede Zeile enthält ein eigenständiges
   JSON‑Objekt und erleichtert damit das Streaming großer Datenmengen.

3. **Fine‑Tuning‑Befehle verstehen**\
   * `openai tools fine_tunes.prepare_data -f training_data.jsonl` –
     Dieses Kommando überprüft und bereitet das Rohdatenset (JSONL) für
     das Fine‑Tuning auf. Es entfernt fehlerhafte Zeilen, konvertiert
     Sonderzeichen und speichert das Ergebnis als
     `training_data_prepared.jsonl`.
   * `openai api fine_tunes.create -t training_data_prepared.jsonl -m gpt-3.5-turbo` –
     Startet den Fine‑Tuning‑Prozess mit dem vorbereiteten Datensatz (`-t`)
     auf dem angegebenen Basismodell (`-m`). Der Befehl überträgt die
     Daten in die API, erzeugt einen Fine‑Tune‑Job und gibt eine ID
     zurück.

   **Ablauf:** Zunächst müssen die Trainingsbeispiele in das
   JSONL‑Format gebracht und mit `fine_tunes.prepare_data` bereinigt
   werden. Anschließend überträgt `fine_tunes.create` diese Daten an die
   OpenAI‑Plattform, wo das Modell mehrere Epochen lang auf den
   Beispielen trainiert wird. Nach Abschluss des Trainings steht
   ein neues Modell zur Verfügung, das über die API mit der Modell‑ID
   angesprochen werden kann. Die Folien zeigen auch ein Python‑Beispiel
   für die Nutzung eines fine‑getunten Modells mit
   `openai.ChatCompletion.create(...)`.
