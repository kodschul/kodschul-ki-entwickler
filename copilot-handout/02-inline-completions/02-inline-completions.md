# 02 – Inline Completions

**Block:** 90 min | **Tag 1**

---

## Was sind Inline Completions?

Inline Completions (Ghost Text) sind die grauen Vorschläge, die Copilot direkt im Editor anzeigt – noch bevor du `Enter` drückst. Copilot analysiert:

- Den Code **vor** dem Cursor (primär)
- Den Code **nach** dem Cursor (sekundär)
- Offene Dateien im Editor (Kontext-Fenster)
- Den Dateinamen und die Sprache

```python
# Copilot sieht alles ab hier aufwärts als Kontext
def func_calculate_total(items):
    # Ghost Text erscheint hier ↓
    |
```

---

## Keyboard Shortcuts

| Aktion                      | macOS                | Windows/Linux           |
| --------------------------- | -------------------- | ----------------------- |
| Vorschlag annehmen          | `Tab`                | `Tab`                   |
| Vorschlag ablehnen          | `Esc`                | `Esc`                   |
| **Wort für Wort** annehmen  | `⌘ →`                | `Ctrl →`                |
| Nächster Vorschlag          | `⌥ ]`                | `Alt ]`                 |
| Vorheriger Vorschlag        | `⌥ [`                | `Alt [`                 |
| Alle Vorschläge anzeigen    | `⌥ Enter`            | `Alt Enter`             |
| Completions ein/ausschalten | `⌘ Shift P` → Toggle | `Ctrl Shift P` → Toggle |

> **Tipp:** `⌥ Enter` öffnet das Completions-Panel mit bis zu 10 Alternativen nebeneinander.

---

## Kontext gezielt steuern

### Was Copilot sieht

```
✅ Der Code ÜBER dem Cursor (wichtigster Kontext)
✅ Der Code UNTER dem Cursor
✅ Alle aktuell geöffneten Tabs (bis zum Token-Limit)
✅ Dateiname + Erweiterung
✅ .github/copilot-instructions.md
✅ Passende .instructions.md (via applyTo)
❌ Geschlossene Dateien
❌ Dateien in .gitignore (meistens)
```

### Kontext verbessern – Techniken

**1. Kommentar als Anleitung:**

```python
# Validiert einen Todo-Titel: nicht leer, max 200 Zeichen, kein HTML
def func_validate_title(title):
    |
```

**2. Beispiel-Muster zeigen (Few-Shot):**

```python
# Beispiel-Muster: validate_email gibt (bool, str) zurück
def func_validate_email(email):
    if not email:
        return False, "Email darf nicht leer sein"
    ...

# Jetzt folgt Copilot dem gleichen Muster:
def func_validate_title(title):
    |
```

**3. Import als Hint:**

```python
from datetime import datetime, timezone
# Copilot weiß jetzt welche Datetime-Funktionen verfügbar sind
```

**4. Docstring zuerst schreiben:**

```python
def func_get_overdue_todos(todos):
    """
    Gibt alle Todos zurück, deren due_date vor heute liegt.

    Args:
        todos: Liste von Todo-Dicts mit optionalem 'due_date' (ISO-Format)
    Returns:
        Liste von überfälligen Todos
    """
    |  # Copilot generiert die Implementierung aus dem Docstring
```

---

## Warum erscheint kein Vorschlag?

| Problem                        | Lösung                                           |
| ------------------------------ | ------------------------------------------------ |
| Cursor in leerem File          | Dateiname/Kommentar hinzufügen                   |
| Zu wenig Kontext               | Funktion/Klasse umbenennen, Kommentar hinzufügen |
| Copilot ausgeschaltet          | Status-Bar-Icon prüfen (unten rechts)            |
| Falscher Cursor-Bereich        | Neue Zeile beginnen statt in der Mitte tippen    |
| Completion deaktiviert für Typ | `settings.json` prüfen: `copilot.enable`         |

---

## Copilot gezielt ausschalten

```json
// .vscode/settings.json
{
  "github.copilot.enable": {
    "*": true,
    "markdown": false, // Kein Ghost-Text in .md Dateien
    "plaintext": false, // Kein Ghost-Text in .txt
    "yaml": true
  }
}
```

---

## Next Edit Suggestions (NES)

Copilot erkennt wenn du eine Änderung machst und schlägt die **nächste logische Änderung** automatisch vor:

```python
# Du änderst:
def func_add_todo(title):           # war: add_item(name)
#                  ↑ Copilot schlägt vor, auch den Parameter
#                    und alle Aufrufe zu aktualisieren
```

→ `Tab` annehmen, `Esc` ablehnen – Copilot springt zur nächsten Änderung.
