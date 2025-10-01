# Lab 2 – Lösungen

1. **Tokenisierung**\
   Bei einer groben Worttrennung lautet die Tokenliste:
   `["Generative", "KI", "verändert", "die", "Softwareentwicklung."]`.
   Es entstehen 5 Tokens. In realen Systemen wird eine feinere
   Tokenisierung (zum Beispiel Byte‑Pair‑Encoding) genutzt, um auch
   Sonderzeichen oder zusammengesetzte Wörter effizient zu
   repräsentieren【626807851092106†L95-L105】. Die Wahl des
   Tokenisierungsverfahrens beeinflusst den Wortschatz des Modells und
   die Länge der Kontextfenster.

2. **Vektor‑Embeddings**\
   Ein Embedding ordnet jedem Wort einen Punkt im hochdimensionalen
   Raum zu, sodass semantisch ähnliche Wörter nahe beieinander liegen【626807851092106†L114-L119】.
   Zum Beispiel könnte **Hund** den Vektor `(0.8, 0.1)` und **Katze**
   `(0.75, 0.15)` erhalten, während **Auto** mit `(0.2, 0.9)` weit weg
   liegt. Dieser Abstand spiegelt wider, dass Hund und Katze beides
   Tiere sind, Auto aber nicht. Embeddings ermöglichen es dem Modell,
   Beziehungen zwischen Wörtern zu verstehen und inferenzielle
   Aufgaben zu lösen.

3. **RLHF – drei Phasen**\
   Laut dem RLHF‑Ansatz besteht das Training aus drei Schritten:
   * **Vortraining** – Ein Sprachmodell wird zunächst unüberwacht auf
     großen Textkorpora trainiert, um Sprachmuster zu lernen.
   * **Belohnungsmodell** – Anschließend bewerten menschliche
     Annotatoren Modellantworten; aus diesen Präferenzen wird ein
     Belohnungsmodell gelernt, das gute Antworten belohnt【199146385693552†L90-L100】.
   * **Reinforcement Learning** – Schließlich wird das
     Sprachmodell mittels bestärkendem Lernen (zum Beispiel
     Proximal Policy Optimization) so angepasst, dass es Antworten
     generiert, die beim Belohnungsmodell hoch punkten【199146385693552†L90-L100】.

   RLHF hilft, die Qualität der Antworten zu steigern und
   problematische Ausgaben zu reduzieren, weil menschliche Präferenzen
   explizit in den Trainingsprozess einfließen.
