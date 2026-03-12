# Lab 3.1 – Code-Generierung, Erklärung und Dokumentation mit KI

## Szenario

Du bist neu im Team eines mittelständischen E-Commerce-Unternehmens und sollst
an einem bestehenden **Bestellverwaltungssystem** weiterarbeiten. Der vorherige
Entwickler hat die Codebasis nur teilweise fertiggestellt und keine Dokumentation
hinterlassen. Deine Aufgabe ist es, den fehlenden Code zu vervollständigen, den
vorhandenen Code zu verstehen und alles sauber zu dokumentieren – mithilfe eines
KI-Assistenten.

---

## Projekt-Überblick

Das Projekt ist ein einfaches **Order Management System** in TypeScript/Node.js.
Es verwaltet Bestellungen, Produkte und Kunden. Teile der Geschäftslogik fehlen
noch komplett, andere sind unvollständig oder undokumentiert.

```
Project/
├── src/
│   ├── models/
│   │   ├── Order.ts          ← teilweise implementiert
│   │   ├── Product.ts        ← vollständig, aber undokumentiert
│   │   └── Customer.ts       ← vollständig, aber undokumentiert
│   ├── services/
│   │   ├── OrderService.ts   ← viele TODOs, unfertig
│   │   ├── PricingService.ts ← fehlt komplett (TODO-Kommentar)
│   │   └── DiscountService.ts← teilweise implementiert
│   ├── utils/
│   │   └── validators.ts     ← fehlt komplett
│   └── index.ts              ← Einstiegspunkt
├── README.md                 ← leer
└── package.json
```

---

## Lernziele

- KI-Assistenten zur Code-Generierung einsetzen
- Unbekannten Code mit Hilfe von KI schnell verstehen
- JSDoc-Kommentare mit KI generieren
- Eine README-Datei automatisch erstellen lassen

---

## Aufgaben

### Aufgabe 1 – Bestehenden Code verstehen (15 Min.)

Öffne die Dateien `Order.ts`, `Product.ts` und `Customer.ts`.

Nutze den **KI-Chat (Ask-Modus)**, um folgende Fragen zu beantworten:

1. Erkläre mir, was die Klasse `Order` macht und welche Felder sie hat.
2. Welche Beziehung besteht zwischen `Order`, `Product` und `Customer`?
3. Was fehlt in der Implementierung von `Order.ts`?

> **Tipp:** Markiere den Code und frage die KI direkt: *„Erkläre diesen Code"*
> oder *„Was macht diese Klasse?"*

---

### Aufgabe 2 – Fehlende Methoden generieren (20 Min.)

In `OrderService.ts` sind mehrere Methoden mit `// TODO` markiert.

Nutze den **KI-Edit-Modus oder Inline-Chat**, um:

1. Die Methode `calculateOrderTotal(orderId: string)` zu implementieren.
   - Sie soll alle `OrderItem`-Preise summieren.
   - Rabatte aus dem `DiscountService` sollen berücksichtigt werden.
2. Die Methode `cancelOrder(orderId: string)` zu implementieren.
   - Der Status der Bestellung soll auf `CANCELLED` gesetzt werden.
   - Bereits versendete Bestellungen dürfen nicht storniert werden.
3. Die Methode `getOrdersByCustomer(customerId: string)` zu implementieren.

> **Tipp:** Beschreibe der KI den Kontext:  
> *„Diese Methode soll alle Bestellungen eines Kunden aus dem in-memory Store
> zurückgeben. Der Store ist ein `Map<string, Order>`."*

---

### Aufgabe 3 – `PricingService.ts` komplett generieren (20 Min.)

Die Datei `PricingService.ts` ist leer bis auf einen Kommentar.

Lies den Kommentar und nutze die KI, um den gesamten Service zu generieren:

- Methode: `calculateUnitPrice(product: Product, quantity: number): number`
  - Mengenrabatt: Ab 10 Stück → 5% Rabatt, ab 50 Stück → 10% Rabatt
- Methode: `applyTax(price: number, taxRate: number): number`
- Methode: `formatPrice(amount: number, currency: string): string`

> **Tipp:** Zeige der KI das `Product`-Interface und beschreibe die
> Geschäftsregeln. Nutze den Prompt:  
> *„Erstelle einen TypeScript-Service mit folgenden Methoden und Regeln: …"*

---

### Aufgabe 4 – `validators.ts` generieren (15 Min.)

Die Datei `validators.ts` existiert, ist aber völlig leer.

Generiere mit KI folgende Validierungsfunktionen:

1. `isValidEmail(email: string): boolean`
2. `isValidOrderId(id: string): boolean` – Format: `ORD-XXXXXX` (6 Ziffern)
3. `isValidProductQuantity(quantity: number): boolean` – positiv, ganzzahlig, max. 9999
4. `isValidCustomer(customer: Customer): boolean` – Name und E-Mail müssen vorhanden sein

> **Tipp:** Nutze den Prompt:  
> *„Schreibe TypeScript-Validierungsfunktionen mit JSDoc-Kommentaren.
> Verwende keine externen Bibliotheken."*

---

### Aufgabe 5 – Dokumentation mit JSDoc generieren (15 Min.)

Alle Klassen und Methoden sind undokumentiert.

Nutze KI, um JSDoc-Kommentare zu generieren für:

1. Alle Klassen in `models/`
2. Alle öffentlichen Methoden in `OrderService.ts`
3. Alle Funktionen in `validators.ts`

> **Tipp:** Markiere eine Klasse oder Methode und nutze den Prompt:  
> *„Füge JSDoc-Kommentare zu dieser TypeScript-Klasse hinzu."*

---

### Aufgabe 6 – README.md generieren (10 Min.)

Die `README.md` ist leer. Generiere eine vollständige README mit KI.

Die README soll enthalten:
- Projektbeschreibung
- Installationsanleitung
- Verwendungsbeispiele
- Beschreibung der wichtigsten Module/Klassen
- Hinweise zur Erweiterung

> **Tipp:** Teile der KI alle Quelldateien mit und nutze den Prompt:  
> *„Erstelle eine professionelle README.md für dieses Node.js-Projekt auf Basis
> des vorhandenen Codes."*

---

## Erwartetes Ergebnis

Nach Abschluss aller Aufgaben sollte das Projekt:

- ✅ Alle `TODO`-Marker entfernt haben
- ✅ `PricingService.ts` vollständig implementiert sein
- ✅ `validators.ts` alle vier Funktionen enthalten
- ✅ Alle Klassen und Methoden mit JSDoc dokumentiert sein
- ✅ Eine vollständige `README.md` besitzen
- ✅ `npm run build` fehlerfrei durchlaufen

---

## Hinweise zum KI-Einsatz

| Aufgabe                    | Empfohlener Modus        | Beispiel-Prompt                                              |
|----------------------------|--------------------------|--------------------------------------------------------------|
| Code verstehen             | Ask / Chat               | „Erkläre diese Klasse und ihre Abhängigkeiten"               |
| Methoden implementieren    | Edit / Inline-Chat       | „Implementiere diese TODO-Methode basierend auf dem Kontext" |
| Neuen Service generieren   | Edit / Chat + Copy-Paste | „Erstelle diesen Service mit folgenden Anforderungen: …"     |
| JSDoc schreiben            | Inline-Chat              | „Füge JSDoc zu allen public Methoden hinzu"                  |
| README erstellen           | Chat mit Datei-Kontext   | „Erstelle eine README für dieses Projekt"                    |

---

## Bewertungskriterien

- Vollständigkeit: Sind alle TODOs gelöst?
- Korrektheit: Funktioniert die Logik (Rabatte, Stornierung, Validierung)?
- Dokumentation: Sind JSDoc-Kommentare vorhanden und sinnvoll?
- README: Ist die README für einen neuen Entwickler hilfreich?
