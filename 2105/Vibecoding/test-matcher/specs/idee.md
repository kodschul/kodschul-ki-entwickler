# Test-Matcher — App-Idee

## Was ist die Idee?

Eine App, die automatisch erkennt, welche Testfälle für ein bestimmtes Release relevant sind — damit Teams nie wieder raten müssen, was sie vor einem Release testen sollen.

---

## Das Problem

Vor jedem Release stellt sich die gleiche Frage:
**"Was müssen wir eigentlich testen?"**

Meistens wird das händisch entschieden — aus dem Bauchgefühl heraus oder basierend auf dem, woran zuletzt gearbeitet wurde. Dabei werden Testfälle vergessen, doppelt ausgeführt oder falsch priorisiert. Das kostet Zeit und führt zu Fehlern in der Produktion.

---

## Die Lösung

Der **Test-Matcher** verbindet zwei Dinge, die bisher getrennt verwaltet werden:

1. **Releases** — Was wurde geändert? Welche Features, Tickets oder Komponenten sind im Release enthalten?
2. **Testfälle** — Welche Tests gibt es? Was deckt jeder Test ab?

Die App analysiert ein Release und sagt dir automatisch:
- Welche Testfälle sind **direkt betroffen** (müssen definitiv laufen)
- Welche Testfälle sind **indirekt betroffen** (könnten durch Änderungen beeinflusst werden)
- Welche Testfälle sind **nicht relevant** (können übersprungen werden)

---

## Kernfunktionen

### 1. Release einlesen
- Release-Beschreibung, Changelog oder Ticket-Liste einfügen (Text, CSV, Copy-Paste)
- Alternativ: direkte Anbindung an Jira, GitHub, GitLab oder Azure DevOps

### 2. Testfall-Bibliothek verwalten
- Testfälle anlegen mit Namen, Beschreibung und Tags (z. B. Bereich, Komponente, Feature)
- Testfälle importieren (Excel, CSV, Zephyr, TestRail)

### 3. Matching-Analyse
- KI-gestützte Analyse: Release-Inhalt wird mit Testfall-Beschreibungen verglichen
- Ergebnis: priorisierte Testliste mit Begründung, warum jeder Test relevant ist
- Konfidenzwert: Wie sicher ist die Empfehlung? (hoch / mittel / niedrig)

### 4. Test-Report exportieren
- Export als PDF, Excel oder direkt in ein Test-Management-Tool
- Übersicht: Wie viel Prozent der Testfälle abgedeckt? Was wurde übersprungen?

---

## Wer nutzt das?

| Rolle | Nutzen |
|---|---|
| QA-Engineer | Weiß sofort, welche Tests er ausführen muss |
| Testmanager | Kann den Testumfang begründen und dokumentieren |
| Entwickler | Sieht, welche Tests seine Änderung berührt |
| Release-Manager | Hat eine klare Übersicht vor dem Go-Live |

---

## Wie würde das in der Praxis aussehen?

1. Release-Manager fügt die Release-Notes für Version 2.4.1 ein
2. Der Test-Matcher analysiert: "Login-Flow geändert, Payment-Service aktualisiert"
3. Ergebnis: 12 Testfälle direkt betroffen, 5 indirekt, 43 nicht relevant
4. QA-Team bekommt eine priorisierte Liste und kann sofort loslegen
5. Der Report wird automatisch an das Team geschickt

---

## Mögliche Erweiterungen (später)

- **Lernfunktion**: Die App lernt aus vergangenen Releases, welche Tests wirklich fehlschlugen
- **Testabdeckungs-Score**: Wie gut ist die Testbibliothek für typische Releases aufgestellt?
- **Slack / Teams Integration**: Testliste direkt in den Team-Chat schicken
- **Historische Analyse**: Welche Bereiche schlagen bei Releases immer wieder fehl?

---

## Status

- [x] Idee dokumentiert
- [x] Anforderungen konkretisiert
- [x] Technischer Stack entschieden
- [x] MVP gebaut
