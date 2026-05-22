# KI-Analyse

## Was ist das?

Die KI-Analyse ist das Herzstück des Test-Matchers. Sie liest einen Release-Inhalt und entscheidet automatisch, welche Testfälle aus der Bibliothek für dieses Release relevant sind — und welche nicht.

## Warum brauchen wir das?

Vor jedem Release müssen Teams manuell entscheiden, was getestet wird. Das kostet Zeit, ist fehleranfällig und hängt oft vom Wissen einzelner Personen ab. Die KI-Analyse nimmt diese Entscheidung ab und liefert eine begründete, nachvollziehbare Testliste in Sekunden.

## Was kann der Nutzer damit tun?

1. Release-Beschreibung eingeben (z. B. Changelog, Ticket-Liste, Freitext)
2. Analyse starten
3. Ergebnis erhalten: Eine priorisierte Liste aller Testfälle, aufgeteilt in drei Gruppen:
   - **Muss laufen** — direkt von der Änderung betroffen
   - **Sollte laufen** — könnte indirekt betroffen sein
   - **Kann übersprungen werden** — kein Bezug zum Release
4. Zu jedem Testfall gibt es eine kurze Begründung, warum er in diese Gruppe fällt
5. Wenn Änderungen im Release durch keinen Testfall abgedeckt sind, erscheint eine Warnung

## Was gehört dazu?

- Eingabefeld für den Release-Inhalt
- Anbindung an die Testfall-Bibliothek
- KI-Analyse mit Claude (Modell: claude-sonnet-4-6)
- Ergebnisanzeige mit drei Kategorien und Begründungen
- Konfidenzanzeige pro Testfall (Wie sicher ist die Empfehlung?)
- Warnhinweise bei fehlender Testabdeckung
- Zusammenfassung: Wie viel Prozent des Releases ist durch Tests abgedeckt?

## Status

- [x] Geplant
- [x] In Umsetzung
- [x] Fertig
