# m05 — Lab: Domain Driven Design

---

## Demo

**Szenario:** Aus einem unstrukturierten Anforderungstext ein Domänenmodell ableiten.

**Prompt (in Copilot Chat oder ChatGPT eingeben):**

```
Du bist Domain-Experte und Senior-Entwickler. Analysiere diesen Anforderungstext
und liefere:

1. Eine Liste aller Entitäten (Substantive die einen Lebenszyklus haben)
2. Eine Liste aller Value Objects (Substantive ohne eigene Identität)
3. Aggregate Roots (welche Entität "besitzt" andere?)
4. Domain Events (Was passiert fachlich? Vergangenheitsform)
5. Ein Ubiquitous Language Glossar (10 Einträge, DE → Code-Begriff)

Anforderungstext:
"Gäste können Zimmer für bestimmte Zeiträume buchen. Zimmer haben Kategorien
(Einzel, Doppel, Suite) und einen Tagespreis. Buchungen durchlaufen Zustände:
Anfrage → Bestätigt → Eingecheckt → Ausgecheckt → Storniert. Bei Stornierung
nach Bestätigung fällt abhängig vom Zeitpunkt eine Gebühr an. Stammkunden
erhalten Rabatt."
```

**Erwartetes Ergebnis:** Copilot liefert strukturierte Liste — gemeinsam reviewen welche Begriffe korrekt sind und welche nicht.

---

## Deine Aufgabe

Verwende denselben Prompt mit diesem Anforderungstext:

```
Ein Online-Shop verkauft Produkte. Kunden legen Produkte in einen Warenkorb
und geben Bestellungen auf. Bestellungen werden bezahlt, verpackt und versendet.
Bei Problemen können Bestellungen zurückgegeben werden. Produkte können
vergriffen sein — dann können sich Kunden benachrichtigen lassen.
```

1. Führe den Prompt aus
2. Vergleiche dein Ergebnis mit der Musterlösung unten
3. Was hat Copilot richtig erkannt? Was hat gefehlt oder war falsch?

---

<details>
<summary>💡 Musterlösung anzeigen</summary>

### Entitäten

- `Customer` — hat Identität, Lebenszyklus (registriert, aktiv, gesperrt)
- `Order` — zentrales Aggregate, durchläuft Zustände
- `Product` — eigene Identität, Bestand änderbar
- `Cart` — kurzlebig, gehört zu einem Customer

### Value Objects

- `Address` — Lieferadresse, keine eigene Identität
- `Money` — Betrag + Währung
- `OrderLine` — Produkt + Menge + Preis zum Zeitpunkt der Bestellung

### Aggregate Roots

- `Order` — besitzt `OrderLine`s
- `Customer` — besitzt `Cart`
- `Product` — verwaltet Bestand

### Domain Events

- `OrderPlaced`
- `OrderPaid`
- `OrderShipped`
- `OrderReturned`
- `ProductRestocked`
- `CustomerNotificationRequested`

### Ubiquitous Language Glossar

| Deutsch             | Code-Begriff        |
| ------------------- | ------------------- |
| Bestellung aufgeben | `PlaceOrder()`      |
| Warenkorb           | `Cart`              |
| Bestellposition     | `OrderLine`         |
| vergriffen          | `OutOfStock`        |
| Rückgabe            | `Return`            |
| Versand             | `Shipment`          |
| Benachrichtigung    | `StockNotification` |
| Stammkunde          | `LoyalCustomer`     |
| Tagespreis          | `DailyRate`         |
| Stornierung         | `Cancellation`      |

</details>
