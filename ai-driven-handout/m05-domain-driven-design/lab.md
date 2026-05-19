# m05 — Lab: Domain Driven Design

---

## Demo

**Szenario:** Aus einem unstrukturierten Anforderungstext ein Domänenmodell ableiten.

Dies ist die Hauptdomäne von **HotelApp** — das Projekt das wir den ganzen Tag aufbauen.

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

Verwende denselben Prompt — analysiere jetzt den **Housekeeping-Bereich** von HotelApp:

```
Du bist Domain-Experte und Senior-Entwickler. Analysiere diesen Anforderungstext
und liefere:
1. Eine Liste aller Entitäten
2. Eine Liste aller Value Objects
3. Aggregate Roots
4. Domain Events (Vergangenheitsform)
5. Ubiquitous Language Glossar (10 Einträge, DE → Code-Begriff)

Anforderungstext:
"Housekeeping-Mitarbeiter reinigen Zimmer nach dem Check-out.
Ein Zimmer kann den Zustand Belegt, Zu reinigen oder Bereit haben.
Nach jeder Reinigung wird ein Reinigungsprotokoll erstellt.
Mitarbeiter sind bestimmten Etagen zugewiesen.
Defekte werden gemeldet und müssen repariert werden bevor das Zimmer freigegeben wird."
```

1. Führe den Prompt aus
2. Vergleiche dein Ergebnis mit der Musterlösung unten
3. Welche zusätzlichen Entitäten gehören in `HotelApp.Domain/`?

---

<details>
<summary>💡 Musterlösung anzeigen</summary>

### Entitäten

- `HousekeepingTask` — hat Lebenszyklus (Pending → InProgress → Done)
- `Staff` — Mitarbeiter mit Etagen-Zuweisung
- `CleaningReport` — Protokoll einer abgeschlossenen Reinigung
- `Defect` — gemeldeter Defekt, blockiert Zimmer-Freigabe

### Value Objects

- `FloorAssignment` — Mitarbeiter + Etage (keine eigene Identität)
- `CleaningDuration` — Start- und Endzeit der Reinigung

### Aggregate Roots

- `HousekeepingTask` — besitzt `CleaningReport` und `Defect`-Liste
- `Staff` — verwaltet Etagen-Zuweisungen

### Domain Events

- `RoomCleaningCompleted`
- `DefectReported`
- `DefectRepaired`
- `RoomReadyForGuest`

### Ubiquitous Language Glossar

| Deutsch | Code-Begriff |
|---------|-------------|
| Reinigung | `Cleaning` |
| Reinigungsauftrag | `HousekeepingTask` |
| Bereit | `ReadyForGuest` |
| Zu reinigen | `NeedsCleaning` |
| Reinigungsprotokoll | `CleaningReport` |
| Defekt melden | `ReportDefect()` |
| Etage | `Floor` |
| Mitarbeiterzuweisung | `FloorAssignment` |
| Freigabe | `RoomRelease` |
| Inspektion | `Inspection` |

### Neue Dateien in HotelApp.Domain/

```
HotelApp.Domain/
├── HousekeepingTask.cs
├── Staff.cs
├── CleaningReport.cs
├── Defect.cs
└── Enums/
    ├── RoomCondition.cs       ← Occupied, NeedsCleaning, Ready
    └── HousekeepingStatus.cs  ← Pending, InProgress, Done
```

</details>
