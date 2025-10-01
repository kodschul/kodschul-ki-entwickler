# Lab 2 – Code analysieren und verstehen (Aufgaben)

In diesem Lab untersuchen Sie bestehende Codebeispiele und verbessern
sie hinsichtlich Laufzeit, Sicherheit und Struktur. Die Aufgaben
orientieren sich an den Beispielen aus den Folien.

1. **Laufzeit optimieren**\
   Betrachten Sie die folgende Python‑Funktion zur Ermittlung von
   Duplikaten:

   ```python
   def find_duplicates(nums):
       duplicates = []
       for i in range(len(nums)):
           for j in range(i + 1, len(nums)):
               if nums[i] == nums[j] and nums[i] not in duplicates:
                   duplicates.append(nums[i])
       return duplicates
   ```

   a) Bestimmen Sie die asymptotische Laufzeit dieser Implementierung.

   b) Refaktorieren Sie die Funktion so, dass sie Duplikate in
   **linearer Zeit O(n)** findet. Verwenden Sie geeignete
   Datenstrukturen. Testen Sie Ihre Lösung mit der Liste `[1, 2, 3, 2, 4, 3, 5]`.

2. **Sicherheitslücke finden und beheben**\
   Der folgende Code liest einen Benutzer aus einer SQLite‑Datenbank:

   ```python
   import sqlite3

   def get_user(username):
       conn = sqlite3.connect('users.db')
       cursor = conn.cursor()
       query = "SELECT * FROM users WHERE username = '%s'" % username
       cursor.execute(query)
       result = cursor.fetchone()
       conn.close()
       return result
   ```

   a) Beschreiben Sie die Sicherheitslücke in diesem Code.

   b) Korrigieren Sie den Code, indem Sie vorbereitete Anweisungen
   (prepared statements) verwenden, um SQL‑Injection zu verhindern.

3. **Funktion modularisieren**\
   Die folgende JavaScript‑Funktion ist sehr lang und führt mehrere
   Aufgaben aus:

   ```javascript
   function processData(data) {
       // trim whitespace
       let cleaned = data.trim();
       // split by comma
       const parts = cleaned.split(",");
       // convert to numbers
       const nums = [];
       for (let i = 0; i < parts.length; i++) {
           nums.push(parseInt(parts[i]));
       }
       // filter even numbers
       const evens = [];
       for (let i = 0; i < nums.length; i++) {
           if (nums[i] % 2 === 0) {
               evens.push(nums[i]);
           }
       }
       return evens;
   }
   ```

   Zerlegen Sie diese Funktion in kleinere, leicht verständliche
   Funktionen mit klaren Verantwortlichkeiten (z.B. `clean_data`,
   `split_data`, `to_numbers`, `filter_even`). Dokumentieren Sie jede
   Funktion mit einem kurzen Kommentar.
