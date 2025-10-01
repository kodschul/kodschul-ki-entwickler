# Lab 1 – Lösungen

1. **E‑Mail‑Validator implementieren**\

   ```python
   import re

   def is_valid_email(email: str) -> bool:
       """
       Prüft, ob die übergebene E‑Mail‑Adresse ein @‑Zeichen und einen
       einfachen Domain‑Teil enthält.

       :param email: Die zu prüfende E‑Mail‑Adresse
       :return: True, wenn die Adresse dem Muster entspricht, sonst False
       """
       pattern = r"^[^@]+@[^@]+\.[^@]+$"
       return re.match(pattern, email) is not None
   ```

2. **Pytest‑Tests erstellen**\

   ```python
   import pytest
   from my_module import is_valid_email

   def test_valid_email():
       assert is_valid_email("user@example.com")

   def test_missing_at():
       assert not is_valid_email("userexample.com")

   def test_missing_domain():
       assert not is_valid_email("user@")
   ```

3. **TypeScript‑Funktion dokumentieren**\

   ```typescript
   /**
    * Gruppiert Elemente einer Liste nach einem durch `keyGetter` berechneten Schlüssel.
    *
    * @template T Der Typ der Elemente in der Liste
    * @param list Eine Liste von Elementen, die gruppiert werden sollen
    * @param keyGetter Eine Funktion, die für jedes Element einen Gruppierungsschlüssel liefert
    * @returns Ein Objekt, dessen Schlüssel die von `keyGetter` berechneten Werte sind
    *          und dessen Werte Arrays mit den jeweils zugehörigen Elementen enthalten
    */
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
