# Lab 3 – Lösungen

1. **JUnit‑Test für eine Java‑Methode**\

   **Prompt:**

   > "Schreibe einen JUnit‑Test für die Methode `Calculator.add(a, b)`, der die Fälle 1 + 2 = 3, 0 + 0 = 0 und −5 + 5 = 0 testet."

   **Implementierung:**

   ```java
   import static org.junit.jupiter.api.Assertions.assertEquals;
   import org.junit.jupiter.api.Test;

   public class CalculatorTest {
       @Test
       public void testAdd() {
           assertEquals(3, Calculator.add(1, 2));
           assertEquals(0, Calculator.add(0, 0));
           assertEquals(0, Calculator.add(-5, 5));
       }
   }
   ```

2. **Jest‑Tests für eine Hilfsfunktion**\

   ```javascript
   const { toUpperCaseSafe } = require('./helpers');

   test('wandelt normalen String in Großbuchstaben um', () => {
       expect(toUpperCaseSafe('test')).toBe('TEST');
   });

   test('liefert leeren String für null oder undefined', () => {
       expect(toUpperCaseSafe(null)).toBe('');
       expect(toUpperCaseSafe(undefined)).toBe('');
   });
   ```

3. **Integrationstest für ein CLI‑Programm**\

   ```python
   import subprocess

   def test_calc_cli():
       result = subprocess.run([
           'python', 'calc_cli.py', '2', '3'
       ], capture_output=True, text=True)
       assert result.stdout.strip() == '5'

   # Integrationstests prüfen das Zusammenspiel mehrerer Komponenten
   # (z.B. Kommandozeilen‑Parsing, Typkonvertierung, Ausgabe). Sie
   # ergänzen Unit‑Tests, die nur einzelne Funktionen isoliert testen.
   ```
