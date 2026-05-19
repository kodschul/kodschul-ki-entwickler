# Modul 8 — Übungen

---

## Übung 8.1-A — Geschäftsregeln aus Anforderungen extrahieren

**Anforderungstext:**
```
Im Hotelreservierungssystem gelten folgende Regeln:
- Buchungen können frühestens heute und höchstens 2 Jahre im Voraus gemacht werden
- Check-out muss mindestens einen Tag nach Check-in liegen
- Stornierungen sind kostenlos bis 48 Stunden vor Check-in
- Bei Stornierung 24-48h vor Check-in: 50% Stornierungsgebühr vom Gesamtpreis
- Bei Stornierung unter 24h vor Check-in oder No-Show: 100% Gebühr
- Stammkunden (> 5 abgeschlossene Buchungen) erhalten 10% Rabatt
- Suiten können nicht online gebucht werden (nur telefonisch)
- Maximal 3 aktive Buchungen pro Gast gleichzeitig
```

**Aufgabe:**
1. Erstellen Sie einen KI-Prompt der alle Regeln kategorisiert
2. Führen Sie den Prompt aus
3. Sortieren Sie die Regeln nach Implementierungsort:

| Regel | Muss/Kann/Verbots | Implementierungsort | Begründung |
|---|---|---|---|
| Check-out nach Check-in | | | |
| 48h kostenlose Stornierung | | | |
| Stammkunden-Rabatt | | | |
| Max. 3 aktive Buchungen | | | |
| Suiten nur telefonisch | | | |

---

## Übung 8.1-B — Verantwortlichkeiten verteilen

**Aufgabe:** Entscheiden Sie für jede Regel welche Klasse / welcher Service sie implementiert und begründen Sie kurz warum.

| Regel | Implementiert in | Begründung |
|---|---|---|
| Check-in muss in Zukunft liegen | | |
| Check-out nach Check-in | | |
| Stornierungsgebühr berechnen | | |
| Stammkunden-Rabatt berechnen | | |
| Max. 3 aktive Buchungen prüfen | | |
| Suiten nicht online buchbar | | |
| Gesamtpreis berechnen | | |

---

## Übung 8.2-A — Buchungslogik implementieren

**Aufgabe:** Implementieren Sie mit KI folgende Methoden auf der `Booking`-Klasse:

1. `CalculateCancellationFee(DateTimeOffset cancellationTime) → decimal`
   - Kostenlos wenn ≥ 48h vor Check-in
   - 50% wenn 24-48h vor Check-in
   - 100% wenn < 24h vor Check-in oder nach Check-in

2. `Reschedule(DateTime newCheckIn, DateTime newCheckOut)`
   - Nur wenn Status `Pending` oder `Confirmed`
   - Dieselbe Validierung wie beim Erstellen
   - Domain Event `BookingRescheduled`

3. Prüfen Sie nach der Generierung:
   - Werden alle Zeitgrenzen korrekt berechnet?
   - Wird `DateTimeOffset` statt `DateTime` verwendet (Zeitzonen!)?
   - Gibt es einen Off-by-one-Fehler bei genau 48h?

---

## Übung 8.2-B — PricingService implementieren

**Preisberechnung:**
```
Basispreis    = Zimmerpreis × Anzahl Nächte
Wochenende    = +20% für Nächte auf Sa/So
Stammkunde    = -10% wenn > 5 abgeschlossene Buchungen
Frühbucher    = -15% wenn Buchung > 60 Tage vor Check-in
Rabatte       = addiert, max. 25% Gesamtrabatt
Endergebnis   = auf 2 Dezimalstellen gerundet
```

1. Schreiben Sie den KI-Prompt für `BookingPricingService`
2. Generieren Sie den Code
3. Schreiben Sie xUnit-Tests für alle Rabattkombinationen:
   - Beide Rabatte → 25% (Cap)
   - Nur Stammkunde → 10%
   - Nur Frühbucher → 15%
   - Kein Rabatt → 0%
   - Grenzwert Frühbucher: genau 60 Tage (kein Rabatt), 61 Tage (Rabatt)

---

## Übung 8.3-A — Edge Cases mit KI finden

**Aufgabe:** Lassen Sie KI Edge Cases für die `CalculateCancellationFee`-Methode finden.

**Prompt:**
```
Analysiere diese Methode und identifiziere alle Edge Cases und möglichen Bugs:
[Code der Methode einfügen]

Für jeden Edge Case:
1. Szenario beschreiben
2. Was passiert aktuell?
3. Korrekte Erwartung
4. Falls Bug: korrigierter Code

Berücksichtige: Zeitzonenproblemen, Grenzwerte (genau 48h, genau 24h),
Stornierung nach Check-in, null-Referenzen.
```

---

## Übung 8.3-B — KI-Code kritisch prüfen

**KI-generierter Code:**
```csharp
public decimal CalculateCancellationFee(DateTime cancellationTime)
{
    var hoursUntilCheckIn = (CheckInDate - cancellationTime).TotalHours;

    if (hoursUntilCheckIn >= 48) return 0;
    if (hoursUntilCheckIn >= 24) return TotalPrice * 0.5m;
    return TotalPrice;
}
```

**Aufgabe:** Finden Sie alle Probleme:
1. Funktioniert der Code für alle Szenarien aus den Anforderungen?
2. Was passiert wenn `cancellationTime > CheckInDate`?
3. Was ist mit Zeitzonen (`DateTime` vs. `DateTimeOffset`)?
4. Off-by-one bei genau 48h?
5. Schreiben Sie 5 xUnit-Tests die Grenzfälle abdecken

---

## Übung 8.4-A — Vollständiger Application Service

**Aufgabe:** Implementieren Sie `BookingApplicationService` mit:

1. `CreateBookingAsync(CreateBookingCommand cmd, CancellationToken ct) → Guid`
   - Gast laden (KeyNotFoundException)
   - Zimmer laden + Kategorie prüfen (Suiten → InvalidOperationException)
   - Verfügbarkeit prüfen (via Repository)
   - Max-3-Buchungen prüfen
   - Preis berechnen via IPricingService
   - Booking erstellen + speichern + Domain Events dispatchen

2. `CancelBookingAsync(CancelBookingCommand cmd, CancellationToken ct)`
   - Booking laden
   - Prüfen ob cmd.RequestingGuestId der Besitzer ist (UnauthorizedAccessException)
   - Stornierungsgebühr berechnen
   - Booking.Cancel() aufrufen + speichern

---

## Übung 8.4-B — Integrations-Checkliste anwenden

Wenden Sie die Integrations-Checkliste auf Ihren Service aus 8.4-A an:

| Punkt | Erfüllt? | Nachweis oder was fehlt? |
|---|---|---|
| Domain Events werden dispatched | | |
| Repository-Calls nur im Application Layer | | |
| Kein DbContext im Domain Layer | | |
| Transaktionen bei zusammengehörigen Ops | | |
| Domain- von Infrastructure-Exceptions getrennt | | |
| CancellationToken überall | | |
| Logging für kritische Operationen | | |

Schreiben Sie für jeden nicht erfüllten Punkt einen Integrationstest der ihn nachweist und beheben Sie das Problem.
