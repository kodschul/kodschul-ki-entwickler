# Lab 2 – Lösungen

1. **Laufzeit optimieren**\

   a) Die gegebene Implementierung verwendet zwei verschachtelte
   Schleifen und hat damit eine Laufzeit von **O(n²)**. Für jede Zahl
   werden alle folgenden Zahlen erneut verglichen.

   b) Eine Variante mit linearer Laufzeit nutzt ein Set, um bereits
   gesehene Werte zu merken, und ein weiteres Set, um Duplikate zu
   sammeln:

   ```python
   def find_duplicates_linear(nums):
       seen = set()
       duplicates = set()
       for n in nums:
           if n in seen:
               duplicates.add(n)
           else:
               seen.add(n)
       return list(duplicates)

   # Test
   print(find_duplicates_linear([1, 2, 3, 2, 4, 3, 5]))  # Ausgabe: [2, 3]
   ```

2. **Sicherheitslücke finden und beheben**\

   a) Die Sicherheitslücke ist **SQL‑Injection**. Der Benutzername wird
   direkt in die SQL‑Abfrage eingebettet. Ein Angreifer könnte durch
   spezielle Eingaben (`'admin' OR '1'='1'`) auf andere Daten
   zugreifen.

   b) Die Lösung verwendet vorbereitete Anweisungen mit
   Platzhaltern, sodass Parameter getrennt vom SQL‑String übergeben
   werden:

   ```python
   import sqlite3

   def get_user(username):
       conn = sqlite3.connect('users.db')
       cursor = conn.cursor()
       query = "SELECT * FROM users WHERE username = ?"
       cursor.execute(query, (username,))
       result = cursor.fetchone()
       conn.close()
       return result
   ```

3. **Funktion modularisieren**\

   ```javascript
   // Entfernt führende und nachfolgende Leerzeichen
   function clean_data(data) {
       return data.trim();
   }

   // Zerlegt den String anhand eines Trennzeichens in Teile
   function split_data(data, delimiter = ",") {
       return data.split(delimiter);
   }

   // Konvertiert eine Liste von Strings in Ganzzahlen
   function to_numbers(parts) {
       return parts.map((p) => parseInt(p));
   }

   // Filtert gerade Zahlen aus einer Liste von Ganzzahlen
   function filter_even(nums) {
       return nums.filter((n) => n % 2 === 0);
   }

   // Zusammengesetzter Arbeitsablauf
   function processData(data) {
       const cleaned = clean_data(data);
       const parts = split_data(cleaned);
       const nums = to_numbers(parts);
       return filter_even(nums);
   }
   ```

   Jede Hilfsfunktion hat eine klar definierte Aufgabe und kann
   unabhängig getestet oder wiederverwendet werden.
