# MCP

**Block:** 13:15 - 15:00 Uhr (Tag 2)

---

## Wie funktioniert das unter der Haube?

```
Offer Studio braucht Zusatzdaten
	-> MCP verbindet Claude mit externer Quelle
	-> relevante Felder werden gemappt
	-> Angebotsabschnitt wird mit Echtkontext verbessert
```

MCP ermoeglicht **kontextreiche Angebote mit externen Daten**, ohne den Basisflow zu brechen.

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
