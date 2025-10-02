# Lab 6.1 – Security: Was tun bei generiertem Code?

LLMs können Sicherheitslücken einschleusen, wenn sie unüberprüft in den Entwicklungsprozess eingebracht werden.  Typische Risiken sind **SQL‑Injection**, versteckte Backdoors oder unsichere Authentifizierung.  Um sich zu schützen, empfiehlt die OWASP‑Cheat‑Sheet die Verwendung von **Prepared Statements**, d. h. Parameterbindung statt String‑Konkatenation【785242695121746†L244-L253】.  Prepared Statements trennen Code und Daten, sodass ein Angreifer die Bedeutung der Abfrage nicht verändern kann【785242695121746†L244-L253】.

### Injektionen vermeiden

Unsicherer Code aus den Slides:

```python
# unsicher: direkte Konkatenation
query = "SELECT * FROM users WHERE name = '" + user_input + "'"
cursor.execute(query)
```

Sichere Variante mit Parameterbindung:

```python
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (user_input,))
```

Hier wird der Platzhalter `?` verwendet; das Datenbank‑API übernimmt das Escaping und verhindert Injection.

### Backdoor entfernen

In einem Beispiel wurde eine Backdoor gezeigt, in der ein bestimmter Benutzername Admin‑Rechte erhält:

```javascript
if (username === "testadmin") {
    role = "admin";
}
```

Solche Hintertüren dürfen nicht eingesetzt werden; die Rolle sollte anhand eines sicheren Authentifizierungs‑ und Autorisierungssystems vergeben werden.

### Weitere Sicherheitsmaßnahmen

- Führe manuelle **Code‑Reviews** durch, insbesondere bei AI‑generiertem Code.
- Nutze **Static Application Security Testing (SAST)**‑Werkzeuge wie SonarQube oder Semgrep, um Schwachstellen zu entdecken.
- **Input‑Validierung** und **Output‑Encoding** vermeiden Injection‑Angriffe.
- Schütze **Secrets** (API‑Keys, Passwörter) durch Umgebungsvariablen und Secrets‑Management.
