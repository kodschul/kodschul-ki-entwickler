# Email Validator

Dieses Projekt enthält ein einfaches Python-Skript zur Überprüfung, ob eine E-Mail-Adresse ein gültiges Format hat.

## Inhalt

- [`email_validator.py`](./email_validator.py): Enthält die Funktion zur E-Mail-Validierung und einige Beispieltests.

## Verwendung

1. **Klonen oder Herunterladen** des Repositories.
2. **Ausführen** des Skripts:

   ```bash
   python email_validator.py
   ```

3. Die Ausgabe zeigt für jede Test-E-Mail, ob sie gültig ist (`True`) oder nicht (`False`).

## Funktionsweise

Die Funktion `is_valid_email(email: str) -> bool` prüft mit einem regulären Ausdruck, ob die E-Mail-Adresse das Muster `text@text.text` erfüllt.

**Beispiel:**

```python
is_valid_email("beispiel@domain.de")  # True
is_valid_email("invalid-email")       # False
```

## Hinweise

- Die Validierung prüft nur das grundlegende Format, nicht die Existenz der Domain oder weitere RFC-Konformität.
- Für komplexere Anforderungen sollte eine spezialisierte Bibliothek verwendet werden.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
