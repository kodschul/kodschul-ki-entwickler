# m08 — Agentic Lab: Geschäftslogik mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/business-logic.instructions.md`

```markdown
---
applyTo: "HotelApp.Domain/**/*.cs,HotelApp.Application/**/*.cs"
---

## Geschäftslogik-Konventionen

- Geschäftslogik lebt AUSSCHLIESSLICH in Domain-Entitäten oder Domain Services
- Application Services orchestrieren nur: Repository laden → Domain-Methode aufrufen → speichern
- Controller und Razor Views enthalten KEINE Geschäftslogik
- Infrastructure-Klassen (EF Core, HTTP-Clients) enthalten KEINE Geschäftslogik

## Exception-Typen

- `ArgumentException` — ungültige Eingabe beim Erstellen (Konstruktor)
- `InvalidOperationException` — ungültige Zustandsänderung (Methode)
- `DomainException` — fachliche Regel verletzt (eigene Basisklasse)
- `NotFoundException` — Entität nicht gefunden (Application Service)

## Application Service Regeln

- Jede Methode ist `async Task` oder `async Task<T>`
- Dependency Injection über primären Konstruktor
- Keine direkte `new`-Instanziierung von Domain-Objekten außerhalb von Factories
- Repository-Pattern: niemals `DbContext` direkt in Domain-Klassen
- Alle Datenbankoperationen über `await db.SaveChangesAsync()` abschließen
```

---

## 2. `.github/prompts/implement-business-rules.prompt.md`

Aufruf: `/implement-business-rules`

```markdown
---
name: implement-business-rules
description: Extrahiert Geschäftsregeln aus Anforderungstext und implementiert sie als C#
---

Du bist Senior C#-Entwickler (.NET 9, DDD, Clean Architecture).

Schritt 1 — Regelkategorisierung:
Analysiere den Anforderungstext und kategorisiere alle Geschäftsregeln:

- **Muss-Regeln**: immer gültig, wirft Exception bei Verletzung
- **Verbots-Regeln**: Pre-Conditions, verhindert Aktion
- **Berechnungsregeln**: leitet Werte ab (Rabatt, Gebühr, Preis)

Für jede Regel: Wo implementieren?
→ Entitäts-Methode (Zustandsänderung der Entität selbst)
→ Domain Service (Regel betrifft mehrere Entitäten)
→ Application Service (Orchestrierung, DB-Abfragen nötig)

Schritt 2 — Implementierung:
Implementiere alle Regeln als C#-Code.
Exception-Typen: ArgumentException, InvalidOperationException, DomainException.
Nur Code, keine Erklärungen.

Anforderungstext:
{{selection}}
```

---

## 3. `.github/agents/business-logic-implementer.agent.md`

```markdown
---
name: business-logic-implementer
description: >
  Liest Anforderungsdokumente und implementiert alle Geschäftsregeln
  vollständig in die richtigen Schichten (Domain / Application Service)
tools:
  - codebase
  - new_file
---

Du bist Senior C#-Entwickler (.NET 9, DDD, Clean Architecture).

Aufgabe:

1. Lese alle `.cs`-Dateien in `HotelApp.Domain/` und `HotelApp.Application/`
2. Extrahiere alle Geschäftsregeln und kategorisiere sie
3. Prüfe welche Regeln bereits in `HotelApp.Domain/*.cs` oder `HotelApp.Application/*.cs` implementiert sind
4. Implementiere alle fehlenden Regeln in der richtigen Schicht:
   - Zustandsänderungen einer Entität → Methode in der Entitätsklasse
   - Regeln über mehrere Entitäten → neuer Domain Service
   - Regeln die DB-Abfragen brauchen → Application Service Methode
5. Erstelle `business-rules-status.md` mit Übersicht: Regel → Implementiert in

Konventionen (immer einhalten):

- Niemals Geschäftslogik im Controller oder in EF Core Konfigurationen
- Exception-Typen: ArgumentException (Konstruktor), InvalidOperationException (Methoden)
- Alle Application Service Methoden sind async
```

**Workflow:**

```
HotelApp.Domain/ + HotelApp.Application/  →  [business-logic-implementer]  →  HotelApp.Domain/*.cs (Methoden ergänzt)
                                                                             →  HotelApp.Application/*Service.cs
                                                                             →  business-rules-status.md
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lies alle Klassen in HotelApp.Domain/ und HotelApp.Application/. Extrahiere alle Geschäftsregeln, kategorisiere sie
und implementiere alle fehlenden in HotelApp.Domain/ und HotelApp.Application/.
Erstelle danach business-rules-status.md mit dem aktuellen Umsetzungsstatus.
```

---

## 4. `.github/skills/business-logic-helper/SKILL.md`

Per `/business-logic-helper` abrufbar — extrahiert und implementiert Geschäftsregeln.

```markdown
---
name: business-logic-helper
description: >
  Extracts and implements business rules for .NET DDD projects following
  Clean Architecture. Use when implementing domain rules, categorizing
  business logic into the right layer (entity method, domain service,
  application service), or auditing existing code for misplaced logic.
  Trigger words: business rule, domain logic, geschäftsregel, application
  service, domain service, InvalidOperationException, DomainException,
  clean architecture, layer violation, business logic audit.
---

# Business Logic Helper

Extrahiert Geschäftsregeln aus Anforderungen und implementiert sie in der richtigen Schicht.

## Wann verwenden

- Neue Geschäftsregeln aus Anforderungsdokumenten ableiten
- Regeln in die richtige Schicht einordnen (Domain vs. Application)
- Bestehenden Code auf Layer-Violations prüfen
- `business-rules-status.md` aktuell halten

## Voraussetzungen

- HotelApp Projekt geklont und in VS Code geöffnet
- `HotelApp.Domain/` und `HotelApp.Application/` vorhanden
- Konventionen aus [`references/business-logic-conventions.md`](./references/business-logic-conventions.md)

## Entscheidungsbaum: Wo implementieren?
```

Regel betrifft eine Entität allein?
→ Ja: Methode in der Entitätsklasse (Domain/)
→ Nein: Regel betrifft mehrere Entitäten?
→ Ja: Domain Service (Domain/Services/)
→ Nein: DB-Abfragen nötig?
→ Ja: Application Service (Application/)

```

## Vorgehen

1. Lese alle `.cs`-Dateien in `HotelApp.Domain/` und `HotelApp.Application/`
2. Kategorisiere alle Regeln (Muss / Verbots / Berechnungs)
3. Prüfe vorhandene Implementierungen auf Vollständigkeit
4. Implementiere fehlende Regeln in der richtigen Schicht
5. Aktualisiere `specs/business-rules-status.md`

## Beispiel-Aufruf

```

/business-logic-helper
Extrahiere alle Geschäftsregeln aus HotelApp.Domain/ und HotelApp.Application/ und implementiere die fehlenden

```

```

**Skill-Struktur anlegen:**

```
.github/skills/business-logic-helper/
├── SKILL.md
└── references/
    └── business-logic-conventions.md    ← Regeln aus business-logic.instructions.md
```
