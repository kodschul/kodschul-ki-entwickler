# Lab 2 – Lösungen

1. **Edge Cases für eine Divisionsfunktion**\

   a) Mögliche Edge Cases:
   * **Division durch Null** – Das zweite Argument `b` darf nicht 0
     sein, sonst tritt eine Ausnahme auf.
   * **Negative Zahlen** – Sowohl `a` als auch `b` können negativ sein.
   * **Große Zahlen oder Gleitkommaüberlauf** – Wenn `a` sehr groß und
     `b` sehr klein ist, kann es zu Gleitkomma‑Grenzfällen kommen.

   b) Beispielhafte Tests mit `pytest`:

   ```python
   import pytest
   from my_module import divide

   def test_divide_normal():
       assert divide(10, 2) == 5.0

   def test_divide_by_zero():
       with pytest.raises(ZeroDivisionError):
           divide(5, 0)

   def test_divide_negative():
       assert divide(-6, 3) == -2.0
   ```

2. **Fehlerpfade bei getUser**\

   a) Mögliche Fehlerpfade:
   * Aufruf ohne ID → es wird eine Exception geworfen.
   * ID == 0 → es soll `null` zurückgegeben werden.
   * Gültige ID → ein Objekt mit `id` und `name` wird geliefert.

   b) Jest‑Tests:

   ```javascript
   const { getUser } = require('./user');

   test('wirft Fehler bei fehlender ID', () => {
       expect(() => getUser(undefined)).toThrow('Missing ID');
   });

   test('gibt null zurück bei ID == 0', () => {
       expect(getUser(0)).toBeNull();
   });

   test('liefert Benutzerobjekt bei gültiger ID', () => {
       const user = getUser(5);
       expect(user).toEqual({ id: 5, name: 'User' });
   });
   ```

3. **Sicherheitskritische Logins**\

   Zu testende Szenarien:
   * **Leere Strings** – Benutzername oder Passwort ist leer.
   * **SQL‑Injection‑Versuche** – Strings wie `' OR '1'='1'` sollten
     nicht zum Erfolg führen, auch wenn in diesem einfachen Beispiel
     keine Datenbank verwendet wird.
   * **Sehr lange Eingaben** – Überlange Strings könnten eine
     Denial‑of‑Service‑Lücke offenbaren.

   **Beispieltests (Pseudo‑Code):**
   ```python
   from my_module import login

   def test_empty_credentials():
       assert not login('', '')

   def test_sql_injection_like_input():
       assert not login("' OR '1'='1", "anything")

   def test_long_input():
       long_user = 'a' * 10000
       long_pass = 'b' * 10000
       assert not login(long_user, long_pass)
   ```

   In realen Anwendungen würde die Funktion nicht einfach einen
   Stringvergleich durchführen, sondern die Eingaben an einen
   Authentifizierungsdienst weiterreichen. Die hier formulierten
   Tests dienen dazu, ungewöhnliche Eingaben frühzeitig zu erkennen.
