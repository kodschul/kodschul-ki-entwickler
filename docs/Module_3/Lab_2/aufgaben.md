# Lab 2 – Edge Cases und Fehlerpfade erkennen (Aufgaben)

Das zweite Lab in Modul 3 widmet sich der Identifikation von Randfällen
und Fehlerpfaden. Diese Aufgaben sollen Ihnen helfen, Risiken in
Programmen zu erkennen und geeignete Tests zu formulieren.

1. **Edge Cases für eine Divisionsfunktion**\
   Die Funktion `divide` teilt zwei Zahlen:

   ```python
   def divide(a: int, b: int) -> float:
       return a / b
   ```

   a) Nennen Sie mindestens drei Edge Cases, die bei dieser Funktion
   berücksichtigt werden müssen.

   b) Schreiben Sie drei entsprechende `pytest`‑Tests für diese
   Edge Cases.

2. **Fehlerpfade bei getUser**\
   Die folgende Funktion gibt Benutzer‑Informationen zurück:

   ```javascript
   function getUser(id) {
       if (!id) throw new Error('Missing ID');
       if (id === 0) return null;
       return { id, name: 'User' };
   }
   ```

   a) Beschreiben Sie mögliche Fehlerpfade und Randfälle.

   b) Formulieren Sie drei Jest‑Tests, die diese Situationen abdecken.

3. **Sicherheitskritische Logins**\
   Die Funktion `login` soll einen Benutzer authentifizieren:

   ```python
   def login(username: str, password: str) -> bool:
       return username == 'admin' and password == 'secret'
   ```

   Welche Angriffsszenarien oder ungewöhnlichen Eingaben sollten Sie
   testen (zum Beispiel SQL‑Injection, leere Strings, extrem lange Inputs)?
   Formulieren Sie entsprechende Testfälle (Pseudo‑Code genügt).
