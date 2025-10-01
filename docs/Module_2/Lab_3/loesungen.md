# Lab 3 – Lösungen

1. **Rekursion vs. Iteration**\

   a) Bei großen `n` kann die rekursive Variante einen **Stack Overflow**
   verursachen, da pro Aufruf ein neuer Eintrag auf dem Call‑Stack
   angelegt wird. Außerdem kann die Berechnung bei sehr großen Zahlen
   langsam werden.

   b) Eine iterative Version vermeidet diese Probleme:

   ```python
   def factorial_iterative(n: int) -> int:
       """Berechnet die Fakultät von n iterativ.

       :param n: Nichtnegative ganze Zahl
       :return: Fakultät von n
       """
       result = 1
       for i in range(1, n + 1):
           result *= i
       return result
   ```

2. **Code‑Duplikate entfernen**\

   ```javascript
   function printCourseInfo() {
       console.log("Wir hoffen, Sie genießen den Kurs.");
       console.log("Bitte stellen Sie Fragen.");
   }

   function showWelcomeMessage() {
       console.log("Willkommen!");
       printCourseInfo();
   }

   function showGoodbyeMessage() {
       console.log("Auf Wiedersehen!");
       printCourseInfo();
   }
   ```

   Der wiederholte Text wird in der neuen Funktion
   `printCourseInfo()` zusammengefasst, sodass Änderungen an der
   Kursinformation nur an einer Stelle vorgenommen werden müssen.

3. **Fehlerbehandlung und Ressourcenmanagement**\

   a) Wenn der Pfad nicht existiert oder keine Leserechte vorliegen,
   wird eine Ausnahme ausgelöst. Außerdem kann vergessen werden, die
   Datei zu schließen, wenn später eine Ausnahme auftritt.

   b) Verbessert mit Context Manager und Fehlerbehandlung:

   ```python
   def read_file(path: str) -> str:
       """Liest den Inhalt einer Datei ein und gibt ihn als String zurück.

       :param path: Pfad zur Datei
       :return: Inhalt der Datei
       :raises FileNotFoundError: wenn die Datei nicht existiert
       :raises OSError: bei anderen Ein-/Ausgabefehlern
       """
       try:
           with open(path, "r", encoding="utf-8") as f:
               return f.read()
       except FileNotFoundError:
           raise FileNotFoundError(f"Datei nicht gefunden: {path}")
       except OSError as err:
           raise OSError(f"Fehler beim Lesen von {path}: {err}")
   ```
