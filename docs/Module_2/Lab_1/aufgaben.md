# Lab 1 – Code schreiben, debuggen und dokumentieren (Aufgaben)

In diesem Lab üben Sie, mithilfe von Sprachmodellen Code zu schreiben,
zu testen und zu dokumentieren. Die folgenden Aufgaben orientieren
sich an Beispielen aus den Folien.

1. **E‑Mail‑Validator implementieren**\
   Schreiben Sie eine Python‑Funktion `is_valid_email(email: str) -> bool`,
   die überprüft, ob eine E‑Mail‑Adresse ein `@` und einen einfachen
   Domain‑Teil enthält. Verwenden Sie dazu eine reguläre
   Ausdrucksprüfung. Dokumentieren Sie die Funktion mit einer
   Docstring, die Parameter und Rückgabewert erläutert.

2. **Pytest‑Tests erstellen**\
   Schreiben Sie drei `pytest`‑Testfunktionen für Ihre
   `is_valid_email`‑Funktion. Testen Sie dabei typische gültige und
   ungültige Fälle wie `'user@example.com'`, `'userexample.com'` und
   `'user@'`.

3. **TypeScript‑Funktion dokumentieren**\
   Gegeben ist die folgende TypeScript‑Funktion, die Elemente nach
   einem Schlüssel gruppiert:

   ```typescript
   function groupBy<T>(list: T[], keyGetter: (item: T) => string): { [key: string]: T[] } {
       const result: { [key: string]: T[] } = {};
       for (const item of list) {
           const key = keyGetter(item);
           if (!result[key]) {
               result[key] = [];
           }
           result[key].push(item);
       }
       return result;
   }
   ```

   Fügen Sie einen ausführlichen JSDoc‑Kommentar oberhalb der Funktion
   hinzu, der Zweck, Parameter und Rückgabewert beschreibt.
