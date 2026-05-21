# MCP - Echte Daten einbinden

**Block:** 13:15 - 15:00 Uhr (Tag 2, optional)

---

## Was ist MCP?

MCP (Model Context Protocol) ist eine Moeglichkeit, Claude mit **echten Daten** zu verbinden -
ohne Code zu schreiben. Du beschreibst, welche Daten du brauchst und woher sie kommen sollen.
Claude bindet sie automatisch in deine App ein.

Beispiel: Statt Preise manuell einzutippen, holt sich die App die aktuellen Preise
automatisch aus einer Tabelle oder einem System.

```
Deine App braucht aktuelle Daten
  -> MCP verbindet Claude mit der Datenquelle
  -> Claude holt die relevanten Informationen
  -> App-Ausgabe wird mit echten Daten angereichert
  -> Kein manuelles Copy-Paste mehr
```

---

## Warum / Wann nicht?

| Warum nutzen                           | Wann nicht                                        |
| -------------------------------------- | ------------------------------------------------- |
| Aktuelle Daten direkt in der App       | Wenn kein stabiler Datenzugang vorhanden ist      |
| Keine Fehler durch manuelles Eintragen | Wenn Datenschutzfreigabe noch fehlt               |
| App wird mit jeder Nutzung besser      | Wenn du nur einen Prototyp ohne Integration baust |

---

## Typische Quellen fuer Offer Studio

- Preislisten / Rate Cards
- Teamverfuegbarkeit
- Branchenvorlagen und Textbausteine
- Kundendatenbank (CRM)

---

## Wie beschreibst du eine MCP-Integration?

Du erklaerst Claude in einfachen Worten:

- Welche Daten sollen eingebunden werden?
- Aus welcher Quelle?
- Welches Feld in der App soll damit befuellt werden?
- Was passiert, wenn die Quelle nicht erreichbar ist?

Kein Code, keine Konfiguration - nur eine klare Beschreibung.

---

## Vollstaendiges Beispiel

**Integrationsplan fuer Preisliste:**

```markdown
# MCP-Integration: Preisliste

## Quelle

Preisliste aus einer Excel-Tabelle oder Google Sheet.

## Was wird eingebunden?

- Rolle (z.B. "Senior Berater")
- Tagessatz in Euro
- Regionaler Aufschlag

## Wo erscheint es in der App?

Der Preis-Abschnitt im Angebotsentwurf wird automatisch
mit den aktuellen Tagessaetzen befuellt.

## Was wenn die Quelle nicht erreichbar ist?

Standardwerte verwenden und im Angebot deutlich kennzeichnen:
"Preise basieren auf Standardannahmen, bitte aktuell pruefen."
```

---

## So laesst du Claude den Integrationsplan erstellen

```text
Erstelle einen Plan, wie ich aktuelle Preise aus einer Tabelle
in Offer Studio einbinden kann.
Zeige: Welche Felder benoetigt werden, wo sie im Angebot erscheinen
und was passiert, wenn die Tabelle nicht erreichbar ist.
```

---

## Muster-Prompts

```text
Erstelle einen MCP-Integrationsplan fuer Offer Studio.
Quelle: Preisliste. Zeige Felder, Mapping und Fallback.
```

```text
Welche 3 Datenfelder aus einer Preisliste wuerden
Angebote am meisten verbessern? Erklaere warum.
```

```text
Simuliere zwei Faelle:
1) Preisliste ist verfuegbar -> wie sieht das Angebot aus?
2) Preisliste nicht verfuegbar -> wie geht die App damit um?
```

---

## Ergebnis

Du kannst entscheiden, wann echte Daten echten Mehrwert bringen
und wie du sie risikoarm einbindest - ohne eine Zeile Code.

---

## Warum / Wann nicht?

| Warum nutzen                             | Wann nicht                                          |
| ---------------------------------------- | --------------------------------------------------- |
| Aktuelle Preis- und Teamdaten im Angebot | Wenn kein stabiler Datenzugang vorhanden ist        |
| Weniger manuelle Copy/Paste Fehler       | Wenn Datenschutzfreigabe fehlt                      |
| Hoehere Relevanz und Genauigkeit         | Wenn Workshopziel nur Prototyp ohne Integration ist |

---

## Typische MCP-Quellen fuer Offer Studio

- Rate Cards / Preisdaten
- Teamverfuegbarkeit
- Branchenvorlagen
- Standardbausteine fuer Leistungsbeschreibung

---

## Aufbau - Integrationsskizze Beispiel

**Quelle:** Rate Card

**Mapping:**

- `role_name` -> Pricing Tabelle / Rolle
- `daily_rate` -> Preis je Tag
- `region_factor` -> Regionaler Multiplikator

**Fallback-Regel:**

- Wenn Quelle nicht erreichbar ist: Standardpreisband + Hinweis "Preisannahme"

---

## Muster-Prompts

```text
Erstelle einen MCP-Integrationsplan fuer die Datenquelle "Rate Card"
mit Mapping in den Pricing-Abschnitt und sauberem Fallback.
```

```text
Definiere fuer Offer Studio eine Minimalintegration:
Welche 3 Felder reichen aus, um Pricing in Angeboten besser zu machen?
```

```text
Simuliere den Fehlerfall "MCP nicht verfuegbar" und zeige,
wie der Angebotsflow trotzdem sinnvoll weiterlaeuft.
```

---

## Ergebnis

TN koennen entscheiden, wann MCP echten Mehrwert bietet und wie man risikoarm integriert.
