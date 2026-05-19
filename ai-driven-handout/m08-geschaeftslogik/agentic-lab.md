# m08 — Agentic Lab: Geschäftslogik mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/business-logic.instructions.md`

```markdown
---
applyTo: "Domain/**/*.cs,Application/**/*.cs"
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

1. Lese alle `.md`-Dateien in `specs/` oder `docs/`
2. Extrahiere alle Geschäftsregeln und kategorisiere sie
3. Prüfe welche Regeln bereits in `Domain/*.cs` oder `Application/*.cs` implementiert sind
4. Implementiere alle fehlenden Regeln in der richtigen Schicht:
   - Zustandsänderungen einer Entität → Methode in der Entitätsklasse
   - Regeln über mehrere Entitäten → neuer Domain Service
   - Regeln die DB-Abfragen brauchen → Application Service Methode
5. Erstelle `specs/business-rules-status.md` mit Übersicht: Regel → Implementiert in

Konventionen (immer einhalten):

- Niemals Geschäftslogik im Controller oder in EF Core Konfigurationen
- Exception-Typen: ArgumentException (Konstruktor), InvalidOperationException (Methoden)
- Alle Application Service Methoden sind async
```

**Workflow:**

```
specs/anforderungen.md  →  [business-logic-implementer]  →  Domain/*.cs (Methoden ergänzt)
                                                         →  Application/*Service.cs
                                                         →  specs/business-rules-status.md
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese specs/anforderungen.md. Extrahiere alle Geschäftsregeln, kategorisiere sie
und implementiere alle fehlenden in Domain/ und Application/.
Erstelle danach business-rules-status.md mit dem aktuellen Umsetzungsstatus.
```
