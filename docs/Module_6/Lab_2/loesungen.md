# Lösungen – Lab 6.2 Urheberrecht & Verantwortung

1. **Copyright & Ownership:**

Vollständig von einer AI erzeugter Code kann in vielen Rechtsordnungen nicht urheberrechtlich geschützt werden, da urheberrechtliche Werke eine menschliche Schöpfung erfordern.  Organisationen müssen daher selbst Verantwortung übernehmen: Sie sollten AI‑Outputs überprüfen, anpassen und als eigene Werke kennzeichnen.  Bei der Verwendung von Modellen, die mit Open‑Source‑Code trainiert wurden, besteht das Risiko, dass generierter Code lizenzpflichtige Bestandteile enthält【162658884983038†L86-L112】.  Entwickler sollten die Lizenzbedingungen der zugrunde liegenden Modelle kennen, Code‑Snippets auf Ähnlichkeiten prüfen und gegebenenfalls eigene Implementationen vorziehen.

2. **Prompt‑Anonymisierung:**

*Ursprünglicher Prompt:* „Erstelle eine Benutzerstory für unseren Kunden Max Mustermann (E‑Mail: max@example.com), der sich in unserer App registrieren will.“

*Anonymisierter Prompt:* „Erstelle eine Benutzerstory für einen neuen Nutzer, der sich in unserer App registrieren möchte.“

Personenbezogene Daten wie Namen oder E‑Mail‑Adressen sollten nicht in Prompts auftauchen, da sie ungewollt in das Modelltraining eingehen oder weitergegeben werden könnten.  Durch Generalisierung und Platzhalter schützt man die Privatsphäre und erfüllt Datenschutzanforderungen.

3. **Daten anonymisieren:**

Bei personenbezogenen Spalten (Name, E‑Mail) empfiehlt sich *Pseudonymisierung* oder *Generalisierung*:

- **Namen entfernen oder ersetzen:** Statt echter Namen Zufalls‑IDs oder Platzhalter wie „Benutzer_001“ verwenden.
- **E‑Mails maskieren:** E‑Mail‑Adressen entfernen oder durch generische Werte wie „user@example.com“ ersetzen.
- **Nicht‑sensible Felder behalten:** Die Lieblingsfarbe kann bleiben, da sie keine eindeutige Identifikation ermöglicht.

Die anonymisierte CSV könnte so aussehen:

```
UserID,Email,FavoriteColor
Benutzer_001,user1@example.com,Blau
Benutzer_002,user2@example.com,Rot
```

So bleiben statistische Zusammenhänge erhalten, ohne personenbezogene Daten offenzulegen.
