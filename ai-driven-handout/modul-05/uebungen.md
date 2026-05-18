# Modul 5 — Übungen

---

## Übung 5.1-A — Ubiquitous Language entwickeln

**Anforderungstext (bewusst unstrukturiert):**
```
Unsere Bücherei hat Bücher die ausgeliehen werden können. Leute die bei
uns angemeldet sind dürfen Bücher nehmen. Wenn jemand zu spät zurückbringt
muss er zahlen. Manchmal ist ein Buch schon weg dann kann man sich auf eine
Warteliste setzen. Bücher können auch kaputt sein und sind dann nicht verfügbar.
```

**Aufgaben:**
1. Identifizieren Sie alle Fachbegriffe aus dem Text
2. Bereinigen Sie umgangssprachliche Begriffe und schlagen Sie präzisere Alternativen vor
3. Erstellen Sie ein **Glossar** mit mindestens 10 Einträgen im folgenden Format:

```
Begriff (umgangssprachlich): [Original aus Text]
Fachbegriff (deutsch):       [Präziser Begriff]
Code-Name (englisch):        [ClassName]
Definition:                  [Was bedeutet es genau?]
Abgrenzung zu:               [Womit könnte man es verwechseln?]
```

4. Nutzen Sie KI zur Analyse und vergleichen Sie das Ergebnis mit Ihrer manuellen Arbeit. Was hat die KI übersehen?

---

## Übung 5.1-B — KI-gestützte Domänenanalyse

**Anforderungstext:**
```
Das Unternehmen betreibt eine Kurierdienst-Plattform. Absender können Pakete
aufgeben und dabei Empfänger, Gewicht und gewünschte Liefergeschwindigkeit
(Standard 3-5 Tage, Express 1-2 Tage, Same-Day) angeben. Das System berechnet
automatisch den Preis basierend auf Gewicht und Geschwindigkeit.

Pakete durchlaufen folgende Stationen:
Abgeholt → Im Lager → In Zustellung → Zugestellt / Zustellung gescheitert

Bei gescheiterter Zustellung kann der Empfänger einen neuen Termin wählen oder
das Paket im Lager abholen. Absender werden per E-Mail über alle Statusänderungen
informiert.
```

**Aufgabe:**
1. Erstellen Sie einen vollständigen KI-Prompt zur DDD-Domänenanalyse
2. Führen Sie den Prompt aus
3. Ergänzen/korrigieren Sie das Ergebnis fachlich
4. Erstellen Sie das finale Domänenmodell:
   - Entitäten (mit Begründung)
   - Value Objects (mit Begründung)
   - Aggregate Roots (mit Begründung)
   - Domain Events (mindestens 6, in Vergangenheitsform)

---

## Übung 5.2-A — Entity vs. Value Object entscheiden

Entscheiden Sie für jedes Konzept und begründen Sie:

| Konzept | Entity oder Value Object? | Begründung |
|---|---|---|
| Lieferadresse (Straße, PLZ, Ort) | | |
| Fahrer (Name, Führerscheinnummer) | | |
| Preis (Betrag, Währung) | | |
| Paket (Tracking-Nummer, Gewicht) | | |
| GPS-Koordinate (Lat, Lon) | | |
| Zustellversuch (Datum, Ergebnis, Notiz) | | |
| E-Mail-Adresse | | |
| Benutzer-Session (SessionId, UserId, ExpiresAt) | | |
| Währungsbetrag (Decimal, ISO-Währung) | | |
| Lieferzeitraum (Von-Datum, Bis-Datum) | | |

---

## Übung 5.2-B — Domänenmodell in C# implementieren

**Aufgabe:** Implementieren Sie das Domänenmodell für den Kurierdienst aus Übung 5.1-B.

Erstellen Sie mit KI-Unterstützung (und kritischer Prüfung):

1. **`Shipment` als Aggregate Root** mit:
   - Status-Übergängen als explizite Methoden (nicht `SetStatus(string)`)
   - Validierung bei jedem Statusübergang
   - Domain Events für jeden Übergang
   - `private readonly List<DeliveryAttempt>` als Backing Field

2. **`Address` als Value Object** mit:
   - Vollständigen Felder (Straße, HausNr, PLZ, Stadt, Land)
   - Validierung (PLZ 5-stellig für DE)
   - `Format()`-Methode die lesbare Adresse liefert

3. **`DeliverySpeed` als Enum** mit:
   - Extension-Methode `GetMaxDeliveryDays()` → int

**Prüfcheckliste nach KI-Generierung:**
- [ ] Alle Properties haben `private set`?
- [ ] Jeder Status-Übergang prüft den aktuellen Status?
- [ ] Domain Events werden in einer `List<IDomainEvent>` gesammelt?
- [ ] `protected Shipment() { }` vorhanden für EF Core?
- [ ] `decimal` statt `double` für Gewicht und Preise?
- [ ] `DateTime.UtcNow` statt `DateTime.Now`?

---

## Übung 5.3-A — Klassendiagramm erstellen

**Aufgabe:** Erstellen Sie ein vollständiges UML-Klassendiagramm für den Kurierdienst.

1. Lassen Sie KI das draw.io XML generieren (Prompt: mindestens 6 Klassen, alle Beziehungen mit Kardinalität)
2. Öffnen Sie das XML in diagrams.net (draw.io)
3. Prüfen Sie das Diagramm:
   - Alle Klassen vorhanden?
   - Beziehungstypen korrekt (Komposition vs. Aggregation)?
   - Kardinalitäten angegeben und korrekt?
4. Exportieren Sie als PNG und speichern Sie als `.drawio.xml`

**Mindestinhalt:**
`Shipment`, `Sender`, `Recipient`, `Address`, `Driver`, `DeliveryAttempt`, `ShipmentStatus` (Enum), `DeliverySpeed` (Enum)

---

## Übung 5.3-B — Diagramm zu Code übersetzen

**Aufgabe:** Zeigen Sie Ihr Diagramm einer KI und lassen Sie C#-Klassen generieren.

**Prompt-Vorlage:**
```
Analysiere dieses UML-Klassendiagramm [Beschreibung oder XML einfügen].

Generiere vollständige C# .NET 9 Klassen nach DDD:
- Entitäten: Klassen mit privaten Settern, protected EF-Ctor
- Value Objects: sealed records mit Validierung im Ctor
- Enums: mit Werten aus dem Diagramm
- Domain Events: records die IDomainEvent implementieren

Anforderungen: .NET 9, C# 13, XML-Dokumentation, private setter.
```

**Prüfen Sie das Ergebnis gegen Ihr Diagramm:**
- Stimmen alle Beziehungen überein?
- Welche sinnvollen Methoden hat die KI hinzugefügt?
- Was fehlt im Code gegenüber dem Diagramm?

---

## Übung 5.4-A — Typische Modellierungsfehler identifizieren

**KI-generierter Code (enthält 8 Probleme):**
```csharp
public class Shipment
{
    public int Id { get; set; }                          // A
    public string Status { get; set; } = "Created";      // B
    public double Weight { get; set; }                   // C
    public DateTime CreatedAt { get; set; }              // D
    public List<DeliveryAttempt> Attempts { get; set; } = []; // E
    public int DriverId { get; set; }                    // F
    public Driver Driver { get; set; }                   // G

    public Shipment() { }                                // H

    public void SetStatus(string newStatus)
    {
        Status = newStatus;                              // I
    }
}
```

Identifizieren Sie für jede markierte Stelle (A–I):
1. Problem beschreiben (DDD-Verletzung, Technisch, EF Core)
2. Korrigierte Version angeben

---

## Übung 5.4-B — EF Core Konfiguration für DDD-Modell

**Aufgabe:** Erstellen Sie für den Kurierdienst die EF Core 9 Konfiguration.

`ShipmentConfiguration : IEntityTypeConfiguration<Shipment>` muss:
- [ ] `ShipmentStatus` als `string` (HasConversion<string>())
- [ ] `Address` als Owned Type mit Spalten-Präfix (`Pickup_`, `Delivery_`)
- [ ] `DeliveryAttempts` als owned collection in separater Tabelle
- [ ] Index auf `SenderId` und `DriverId`
- [ ] `ValueGeneratedNever()` für selbst gesetzte GUIDs
- [ ] `HasPrecision(10, 3)` für Gewicht (decimal)

Nutzen Sie KI für die Generierung und prüfen Sie jeden Punkt der Checkliste ab.
