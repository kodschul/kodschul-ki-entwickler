# Lab 1 – Lösungen

1. **pytest‑Tests für die Multiplikationsfunktion**\

   **Beispiel‑Prompt:**

   > "Schreibe vier pytest‑Testfunktionen für die Python‑Funktion `multiply(a, b)`, die verschiedene Fälle abdecken: Multiplikation zweier positiver Zahlen, Multiplikation mit 0, Multiplikation mit einer negativen Zahl und Multiplikation zweier negativer Zahlen."

   **Generierte Tests:**

   ```python
   import pytest
   from my_module import multiply

   def test_multiply_positive():
       assert multiply(2, 3) == 6

   def test_multiply_with_zero():
       assert multiply(5, 0) == 0

   def test_multiply_negative():
       assert multiply(-4, 3) == -12

   def test_multiply_both_negative():
       assert multiply(-2, -2) == 4
   ```

2. **Jest‑Tests für die Palindrom‑Funktion**\

   **Beispiel‑Prompt:**

   > "Erstelle drei Jest‑Tests für die Funktion `isPalindrome(str)`,
   >  die prüft, ob ein String ein Palindrom ist. Berücksichtige auch
   >  Fälle mit Leerzeichen und Groß-/Kleinschreibung."

   **Generierte Tests:**

   ```javascript
   const { isPalindrome } = require('./palindrome');

   test('erkennt Palindrom', () => {
       expect(isPalindrome('abba')).toBe(true);
   });

   test('ignoriert Groß-/Kleinschreibung und Leerzeichen', () => {
       expect(isPalindrome('Lagerregal')).toBe(true);
       expect(isPalindrome('Eine Menge Beneige nE Mnie')).toBe(true);
   });

   test('erkennt kein Palindrom', () => {
       expect(isPalindrome('Haus')).toBe(false);
   });
   ```

3. **Integrationstest für das CLI‑Programm**\

   ```python
   import subprocess

   def test_greet_cli():
       result = subprocess.run([
           'python', 'greet.py', 'Alice'
       ], capture_output=True, text=True)
       assert result.stdout.strip() == 'Hello, Alice!'
   ```

   Dieser Test startet das Skript als Subprozess und prüft die
   Standardausgabe. Integrationstests verifizieren, dass mehrere
   Komponenten (z.B. CLI‑Parsing und Ausgabe) zusammenspielen.
