# Aufgaben – Lab 6.1 Security

1. **SQL‑Injection beheben:** In der Datei `login.py` steht folgender Python‑Code:

```python
import sqlite3
conn = sqlite3.connect('users.db')
user_input = input('Benutzername: ')
query = f"SELECT * FROM users WHERE name = '{user_input}'"
cur = conn.cursor()
cur.execute(query)
print(cur.fetchone())
```

Identifiziere die Sicherheitslücke und schreibe den Code um, sodass SQL‑Injection mittels Parameterbindung verhindert wird.  Erkläre kurz, warum Prepared Statements sicherer sind.

2. **Backdoor entfernen:** Betrachte diesen Node‑JS‑Ausschnitt:

```js
function checkRole(username) {
  let role = 'user';
  if (username === 'testadmin') {
    role = 'admin';
  }
  return role;
}
```

Erkläre, warum dieser Code problematisch ist, und implementiere eine sichere Alternative, bei der Rollen aus einer Datenbank oder Konfigurationsdatei geladen werden.

3. **Sicherheits‑Best Practices:** Nenne mindestens drei Maßnahmen, die du beim Einsatz von AI‑generiertem Code berücksichtigst, um Sicherheitsrisiken zu minimieren.  Beziehe dich auf die Empfehlungen aus der Theorie.
