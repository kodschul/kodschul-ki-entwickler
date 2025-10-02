# Lösungen – Lab 6.1 Security

1. **SQL‑Injection beheben:**

Die Sicherheitslücke entsteht, weil der Benutzername direkt in die SQL‑Abfrage eingefügt wird.  Ein Angreifer könnte etwa `admin' OR '1'='1` eingeben und alle Datensätze auslesen.  Prepared Statements mit Platzhaltern verhindern das, indem sie Code und Daten trennen【785242695121746†L244-L253】:

```python
import sqlite3
conn = sqlite3.connect('users.db')
user_input = input('Benutzername: ')
query = "SELECT * FROM users WHERE name = ?"
cur = conn.cursor()
cur.execute(query, (user_input,))
print(cur.fetchone())
```

Die SQLite‑API kümmert sich um das Escaping und verhindert, dass eingebettete Quotes die Abfrage verändern.

2. **Backdoor entfernen:**

Der ursprüngliche Code vergibt Admin‑Rechte an einen fest kodierten Benutzernamen – eine Backdoor.  Stattdessen sollte die Rolle aus einer vertrauenswürdigen Quelle stammen, z. B. der Datenbank:

```js
async function checkRole(username) {
  // Beispiel: Abruf der Rolle aus einer Datenbank
  const user = await db.users.findOne({ name: username });
  return user?.role ?? 'user';
}
```

Du kannst auch eine Konfigurationsdatei mit zulässigen Rollen laden.  Hardcodierte Sonderfälle sollten vermieden werden.

3. **Sicherheits‑Best Practices:**

- **Code‑Review:** Jeder AI‑generierte Vorschlag sollte von einer Entwickler:in überprüft werden.  Dadurch erkennt man unerwartete Logik oder Schwachstellen.
- **SAST‑Tools:** Automatisierte Analysewerkzeuge wie SonarQube oder Semgrep finden bekannte Schwachstellen (Injection, unsichere APIs, etc.).
- **Input‑Validierung:** Alle externen Eingaben sollten validiert und, falls erforderlich, bereinigt werden.  Für Datenbank‑Zugriffe sind Parameterbindungen zu verwenden【785242695121746†L244-L253】.
- **Secrets sicher speichern:** API‑Schlüssel und Passwörter gehören nicht in den Code; verwende Umgebungsvariablen oder ein Secrets‑Management.
