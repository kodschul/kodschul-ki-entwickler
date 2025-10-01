# Lab 1 – Testfälle generieren mit natürlicher Sprache (Aufgaben)

Dieses Lab zeigt, wie Sie mithilfe von LLMs Tests für verschiedene
Programmiersprachen generieren können. Die Beispiele lehnen sich an
die Folien an.

1. **pytest‑Tests für eine Multiplikationsfunktion**\
   Die Funktion `multiply` multipliziert zwei Ganzzahlen:

   ```python
   def multiply(a: int, b: int) -> int:
       return a * b
   ```

   Formulieren Sie einen Prompt für ein LLM, das mindestens vier
   `pytest`‑Testfunktionen für diese Funktion generiert. Die Tests
   sollen normale Fälle (z.B. 2 × 3), den Faktor 0 sowie negative
   Eingaben abdecken. Schreiben Sie die generierten Testfunktionen in
   eine Python‑Datei.

2. **Jest‑Tests für eine Palindrom‑Funktion**\
   Die folgende JavaScript‑Funktion prüft, ob ein String ein Palindrom
   ist:

   ```javascript
   function isPalindrome(str) {
       const reversed = str.split('').reverse().join('');
       return str === reversed;
   }
   ```

   Erstellen Sie mithilfe eines LLM‑Prompts drei **Jest**‑Tests für
   diese Funktion. Die Tests sollen auch Sonderfälle wie Leerzeichen
   und Groß-/Kleinschreibung berücksichtigen.

3. **Integrationstest für ein CLI‑Programm**\
   Gegeben sei das Skript `greet.py`:

   ```python
   import sys

   def main():
       if len(sys.argv) < 2:
           print("Usage: greet.py <name>")
       else:
           print(f"Hello, {sys.argv[1]}!")

   if __name__ == "__main__":
       main()
   ```

   Schreiben Sie mit `pytest` einen Integrationstest, der das Programm
   über das Modul `subprocess` ausführt und überprüft, dass bei Eingabe
   von `Alice` die Ausgabe `Hello, Alice!` erscheint.
