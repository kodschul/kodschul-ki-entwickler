# Lab 2 – Zusammenfassung der Slides

Die Folien erklären die technischen Grundlagen von LLMs:

* **Tokenisierung** – Bevor ein Modell Text versteht, wird er in
  einzelne Tokens zerlegt. Moderne Modelle verwenden zum Beispiel
  Byte‑Pair‑Encoding, das häufige Teilwörter zu Tokens zusammenfasst.
  Die richtige Tokenisierung ist entscheidend für die Effizienz und
  Genauigkeit eines Modells【626807851092106†L95-L105】.

* **Embeddings** – Jedem Token wird ein Vektor zugeordnet, der seine
  Bedeutung im Kontext anderer Wörter repräsentiert【626807851092106†L114-L119】.
  In dieser Repräsentation liegen ähnliche Wörter nah beieinander,
  wodurch semantische Beziehungen mathematisch fassbar werden.

* **Kontextfenster** – Modelle verarbeiten eine begrenzte Anzahl von
  Tokens gleichzeitig (Kontextfenster). Ein größeres Kontextfenster
  erlaubt längere Eingaben, verbraucht aber mehr Rechenleistung【626807851092106†L82-L87】.

* **Trainingsphasen** – Die Präsentation stellt die Schritte
  Pretraining, Feinjustierung und RLHF vor. RLHF verbindet
  menschliche Rückmeldungen mit Reinforcement‑Learning, um die
  Antwortqualität zu verbessern【199146385693552†L90-L100】.

Diese Bausteine bilden die Basis für das Verständnis komplexer
Interaktionen mit LLMs.
