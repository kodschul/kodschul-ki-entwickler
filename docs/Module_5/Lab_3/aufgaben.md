# Aufgaben – Lab 5.3 Zukunftstrends: Der KI‑gesteuerte Dev‑Prozess

1. **Commit‑Nachricht generieren:** Stelle dir vor, du hast folgenden Diff erstellt:

```diff
+ def factorial(n: int) -> int:
+     """Berechnet die Fakultät von n."""
+     if n <= 1:
+         return 1
+     return n * factorial(n - 1)
```

Formuliere einen Prompt für einen LLM, der auf Basis dieses Diffs eine präzise Commit‑Nachricht erzeugt.  Führe den Prompt mit einem Modell (z. B. GPT‑4.1) aus und gib die Commit‑Nachricht an.

2. **Issue aus Log generieren:** Angenommen, ein Web‑Service liefert im Log folgenden Fehler:

```
ERROR 2025-10-01 12:34:56,789 module.payment: NullReferenceException bei PaymentService.Process()
```

Erstelle einen Prompt, der ein LLM dazu bringt, aus diesem Log‑Eintrag einen GitHub‑Issue‑Titel und eine Beschreibung zu generieren, inklusive Schritte zur Reproduktion.  Führe den Prompt aus und präsentiere das Ergebnis.

3. **Pull‑Request‑Beschreibung:** Du hast eine neue Funktion implementiert, die Benutzern erlaubt, ihre E‑Mail‑Adresse zu aktualisieren.  Beschreibe in einem Prompt, wie ein LLM eine Pull‑Request‑Beschreibung generiert, die den Kontext, die neuen Endpunkte und notwendige Tests beschreibt.  Nutze das LLM und gib die generierte PR‑Beschreibung aus.
