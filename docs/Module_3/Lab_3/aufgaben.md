# Lab 3 – Testframeworks und erweiterte Tests (Aufgaben)

Dieses Lab untersucht, wie LLMs Tests für verschiedene Sprachen
generieren, einschließlich Java, JavaScript und Python‑Integrationstests.

1. **JUnit‑Test für eine Java‑Methode**\
   Gegeben ist die Klasse `Calculator` mit einer statischen Methode
   `add`:

   ```java
   public class Calculator {
       public static int add(int a, int b) {
           return a + b;
       }
   }
   ```

   Verwenden Sie ein LLM‑Prompt, um einen JUnit‑Test zu formulieren,
   der die Methode `add` mit verschiedenen Parametern überprüft (z.B.
   positive, negative und Null‑Werte). Implementieren Sie den Test
   in Java.

2. **Jest‑Tests für eine Hilfsfunktion**\
   Die folgende Node.js‑Funktion wandelt einen String in Großbuchstaben
   um oder liefert einen leeren String zurück, wenn die Eingabe
   `null` oder `undefined` ist:

   ```javascript
   function toUpperCaseSafe(str) {
       if (!str) return '';
       return str.toUpperCase();
   }
   module.exports = { toUpperCaseSafe };
   ```

   Schreiben Sie mindestens zwei Jest‑Tests, die sowohl normale
   Eingaben als auch Randfälle abdecken.

3. **Integrationstest für ein CLI‑Programm**\
   Das Skript `calc_cli.py` addiert zwei Zahlen, die als Argumente
   übergeben werden:

   ```python
   import sys

   def main():
       if len(sys.argv) != 3:
           print("Usage: calc_cli.py <a> <b>")
           return
       a = int(sys.argv[1])
       b = int(sys.argv[2])
       print(a + b)

   if __name__ == '__main__':
       main()
   ```

   Schreiben Sie einen Integrationstest mit `subprocess`, der
   sicherstellt, dass die Ausgabe für die Eingaben `2` und `3` den
   Wert `5` liefert. Erläutern Sie in einem Satz, warum
   Integrationstests über Unit‑Tests hinaus sinnvoll sind.
