# Lösungen – Lab 5.3 Zukunftstrends

1. **Commit‑Nachricht generieren:**

*Prompt*

> "Erstelle eine präzise Commit‑Nachricht für folgenden Code‑Diff. Beschreibe kurz, was implementiert wurde und warum.\n\n```diff\n+ def factorial(n: int) -> int:\n+     \"\"\"Berechnet die Fakultät von n.\"\"\"\n+     if n <= 1:\n+         return 1\n+     return n * factorial(n - 1)\n```"

*Beispielantwort des LLM*

```
feat(math): Implementiere rekursive Fakultätsfunktion

Fügt eine Funktion `factorial` hinzu, die die Fakultät einer Zahl n rekursiv berechnet.  Die Funktion dokumentiert ihr Verhalten im Docstring und behandelt die Basisfälle n ≤ 1.
```

2. **Issue aus Log generieren:**

*Prompt*

> "Leite aus folgendem Log‑Eintrag einen GitHub‑Issue‑Titel und eine Beschreibung ab.  Beschreibe das erwartete Verhalten, den beobachteten Fehler und Schritte zur Reproduktion:\n\nERROR 2025-10-01 12:34:56,789 module.payment: NullReferenceException bei PaymentService.Process()"

*Beispielantwort*

```
**Titel:** NullReferenceException in PaymentService.Process()

**Beschreibung:** Beim Ausführen des Payment‑Services tritt eine NullReferenceException auf.  Der Fehler wurde am 01.10.2025 um 12:34:56 im Modul `module.payment` ausgelöst.  Schritte zur Reproduktion:\n1. Starte den Web‑Service.\n2. Versuche, eine Zahlung ohne gültige Zahlungsdaten zu verarbeiten.\n3. Die Ausnahme wird geworfen und im Log ausgegeben.
```

3. **Pull‑Request‑Beschreibung:**

*Prompt*

> "Du bist ein Software‑Agent.  Erstelle eine Pull‑Request‑Beschreibung für eine neue Funktion, die es Benutzern erlaubt, ihre E‑Mail‑Adresse zu aktualisieren.  Beschreibe die Motivation, die hinzugefügten Endpunkte und notwendige Tests."

*Beispielausgabe*

```
### Titel
Implementiert Endpunkt zum Aktualisieren der E‑Mail‑Adresse

### Beschreibung
Diese Änderung fügt einen neuen REST‑Endpunkt `PUT /users/{id}/email` hinzu, mit dem Benutzer ihre E‑Mail‑Adresse aktualisieren können.  Die Funktion prüft die Eingabe auf gültiges Format und aktualisiert die Datenbank.  Außerdem wurde die Dokumentation im OpenAPI‑Schema ergänzt.

### Tests
- Fügt Unit‑Tests hinzu, die eine erfolgreiche Aktualisierung sowie Fehlermeldungen bei ungültiger E‑Mail prüfen.
- Integrationstest für den vollständigen Request‑/Response‑Flow.
```
