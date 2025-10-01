# Lab 3 – Zusammenfassung der Slides

In den Folien zum dritten Lab geht es um den praktischen Einsatz
von LLMs. Folgende Themen werden behandelt:

* **Prompt‑Engineering** – Techniken wie Zero‑Shot, One‑Shot und
  Few‑Shot werden vorgestellt. Beim Few‑Shot‑Prompting gibt man dem
  Modell ein oder mehrere Beispiele, um das gewünschte Antwortformat
  vorzubereiten【626807851092106†L164-L175】. Darüber hinaus wird gezeigt, wie
  man durch zusätzliche Instruktionen (zum Beispiel *"Erkläre Schritt für
  Schritt"*) die Qualität der Antworten steigern kann.

* **Datenvorbereitung** – Für das Fine‑Tuning eines Modells müssen die
  Trainingsdaten ein einheitliches Format besitzen. Die Folien
  demonstrieren das **JSONL‑Format** (jedes Beispiel in einer Zeile mit
  `"prompt"` und `"completion"`) und betonen, dass konsistente
  Schreibweisen wichtig sind.

* **Fine‑Tuning‑Prozess** – Es werden Befehle der OpenAI‑CLI vorgestellt,
  um Daten zu validieren (`fine_tunes.prepare_data`) und einen
  Fine‑Tune‑Job zu starten (`fine_tunes.create`). Außerdem zeigen die
  Folien einen Python‑Code, der nach dem Fine‑Tuning das neue Modell
  mittels `openai.ChatCompletion.create` nutzt. Dieser Prozess erlaubt
  die Anpassung eines Basismodells an unternehmensspezifische Inhalte.

Durch geschicktes Prompt‑Design und qualitativ hochwertige Daten
können Sie ein LLM gezielt für Ihre Anwendungen optimieren.
