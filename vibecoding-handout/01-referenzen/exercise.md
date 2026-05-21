# Exercise: Referenzen - Kontext fuer Claude anlegen

## Ziel

Du legst die Grundstruktur deiner App an - allein durch Beschreibungen an Claude.
Kein Code, keine Konfiguration von Hand.

---

## Aufgabe 1: Projektstruktur von Claude anlegen lassen

Schreibe diesen Prompt an Claude:

```text
Erstelle die komplette Ordnerstruktur fuer eine App namens "Offer Studio".
Lege an:
- frontend/src/pages (leer)
- frontend/src/components (leer)
- .claude/skills/ (leer)
- .claude/commands/ (leer)
- .claude/agents/ (leer)
- .claude/specs/ (leer)
- .claude/hooks/ (leer)
- CLAUDE.md mit einem Platzhaltertext
- README.md mit einer kurzen App-Beschreibung
```

Beobachte: Claude legt alles an. Du hast nichts selbst erstellt.

---

## Aufgabe 2: In eigenen Worten beschreiben

Schreibe Claude, was deine App tun soll - so als wuerdest du einem Freund erklaeren:

```text
Beispiel:
"Meine App soll Vertriebsmitarbeitern helfen, schnell professionelle Angebote
zu erstellen. Sie geben Kundendaten und Projektinfos ein, klicken auf
'Angebot erstellen' und bekommen sofort einen fertigen Text."
```

Schreibe deine eigene Version:

```
Meine App: _______________________________________________
___________________________________________________________
___________________________________________________________
```

Sende sie an Claude und lass Claude daraus eine `README.md` erstellen.

---

## Aufgabe 3: Prompt-Vergleich erleben

**Prompt A (unklar):**

```text
Erstelle eine App.
```

**Prompt B (klar und konkret):**

```text
Erstelle eine Web-App "Offer Studio" mit einer Startseite.
Die Seite zeigt ein Formular mit den Feldern: Kundenname, Firma,
Projektbeschreibung, Budget (Zahl in Euro), gewuenschte Lieferzeit.
Unten gibt es einen blauen Button "Angebot erstellen".
```

Teste beide und notiere:

```
Prompt A: ________________________________________________
Prompt B: ________________________________________________
```

---

## Aufgabe 4: Eigene Beschreibung verbessern

Nimm die App-Beschreibung aus Aufgabe 2 und bitte Claude:

```text
Verbessere meine App-Beschreibung so, dass sie als Basis fuer
eine CLAUDE.md genutzt werden kann. Struktur: App-Name, Zielgruppe,
Hauptfunktionen, gewuenschter Ton.
```

---

## Done-Kriterien

- [ ] Projektstruktur von Claude angelegt
- [ ] App-Idee in eigenen Worten beschrieben
- [ ] Prompt-Qualitaet verglichen
- [ ] README.md von Claude generiert

## Naechstes Modul

`02-claude.md-setup`: Claude deiner App beibringen.

## Abgabe

- Vergleich A/B (kurz)
- finaler Prompt v1
- 3 wichtigste Lernpunkte

## Done-Kriterien

- [ ] Grundstruktur vorhanden
- [ ] UI-Definition vorhanden
- [ ] Promptvergleich dokumentiert

Naechstes Modul: `02-claude.md-setup`.
