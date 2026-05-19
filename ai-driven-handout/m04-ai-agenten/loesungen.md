# Modul 4 — Lösungen

---

## Lösung 4.1-A — Agent vs. Chat (erwartete Ergebnisse)

| Kriterium | Einstufig | Mehrstufig |
|---|---|---|
| Vollständigkeit der Klassen | Oberflächlich (fehlende Methoden, Validierung) | Vollständig nach DDD |
| EF Core Konfiguration | Generisch, ohne Feinheiten | Spezifisch, Owned Types, Konvertierungen |
| Qualität der Tests | Oft nur Happy Path | Alle Szenarien abgedeckt |
| Nachbearbeitungsaufwand | Hoch (30–60 min) | Gering (5–15 min) |
| Typische Fehler | Alles vermischt, public setter, kein Event | Präziser, aber Schritt 2 hängt von Schritt 1 ab |

**Fazit:** Mehrstufig lohnt sich ab mittlerer Komplexität. Einfache CRUD-Operationen können einstufig bleiben.

---

## Lösung 4.1-B — Chancen-Risiken-Analyse

**Zwingend menschliche Prüfpunkte:**
- Nach Schritt 2 (Plan): Ist die Implementierungsplanung korrekt? Keine Fehlinterpretation des Issues?
- Nach Schritt 3 (Code): Code-Review! Logikfehler, Sicherheitsprobleme, fehlende Tests
- Nach Schritt 4 (Tests): Sind die Tests wirklich aussagekräftig oder nur grüne Platzhalter?
- Schritt 5 (Merge): Muss immer manuell erfolgen – kein automatisches Mergen in production

**Konkrete Risiken:**
- Schritt 1: Issue falsch interpretiert → falsche Implementierung
- Schritt 3: Sicherheitslücke generiert (SQL Injection, Auth-Bypass)
- Schritt 5: Breaking Change unbemerkt gemerged

**Sicherer Workflow:**
```
Issue lesen ← AGENT
Plan erstellen ← AGENT
Plan zeigen → MENSCH prüft und genehmigt
Code schreiben ← AGENT
Code-Review → MENSCH (zwingend)
PR erstellen ← AGENT
CI ausführen ← AUTOMATISCH
Merge → MENSCH (zwingend)
```

**Sicherheitsregeln für Agenten:**
```
Du darfst NIEMALS:
- Direkt in main/master branchen ohne PR
- Produktionsdatenbanken lesen oder schreiben
- Secrets, API-Keys oder Passwörter in Code einfügen
- Externe Services aufrufen ohne explizite Genehmigung
- Dateien außerhalb des Projekt-Verzeichnisses ändern

Du MUSST:
- Nach jedem Plan-Schritt auf menschliche Bestätigung warten
- Alle Änderungen in einem Feature-Branch machen
- Bei Unsicherheit stoppen und fragen statt raten
```

---

## Lösung 4.2-A — Prompt-Kette für Lagerbestandserhöhung

| Schritt | Input | Prompt-Stichwort | Erwarteter Output | Prüfpunkt |
|---|---|---|---|---|
| 1 | User Story + Akzeptanzkriterien | „Analysiere nach DDD: Entitäten, Methode, Validierungsregeln, Event-Struktur" | Strukturierte Analyse | Alle AKs abgedeckt? |
| 2 | Analyse | „Erstelle/ergänze Product-Entität C# .NET 9: ReplenishStock(int, string) + StockReplenished-Event" | C#-Klassen | private setter? Event korrekt? |
| 3 | Klassen | „Erstelle xUnit Tests für Product.ReplenishStock(): Happy Path, negative Menge, über Max-Bestand" | Testklasse | Alle AKs als Tests? |
| 4 | Tests | „Implementiere ReplenishStock() so dass alle Tests grün werden" | Fertige Methode | Tests grün? |
| 5 | Klassen | „Erstelle EF Core 9 Konfiguration für Product inkl. StockReplenished Domain Event Speicherung" | Konfiguration | Owned Types? Index auf FK? |

---

## Lösung 4.3-B — Sicherheitsregeln für Testdaten-Agent

```
Du bist ein Testdaten-Generierungs-Agent für das Hotelreservierungssystem.

SICHERHEITSREGELN (nicht verhandelbar, immer aktiv):
- Du darfst NUR auf Datenbanken mit "_Test" oder "_Dev" im Namen zugreifen
- Du darfst KEINE Produktions-Verbindungsstrings verwenden
- Alle Operationen in einer einzigen Transaktion ausführen
- Bei jedem Fehler: sofort ROLLBACK, Fehler ausgeben, STOPPEN

PFLICHT-VALIDIERUNGEN (automatisch nach Schritt 3):
- Prüfe ob alle FK-Referenzen auflösbar sind
- Prüfe ob generierte Datumsfelder realistisch sind (keine Checkouts vor Checkins)
- Prüfe ob alle NOT NULL Felder belegt sind
- Prüfe ob unique Constraints verletzt werden

WORKFLOW:
Schritt 1: Schema lesen → zeigen was gefunden wurde → STOP
Schritt 2: Testdaten generieren als JSON → zeigen → STOP, warte auf "OK"
Schritt 3: SQL-Skript erstellen → zeigen → STOP, warte auf "OK"
Schritt 4: Nur nach explizitem "AUSFÜHREN" → Transaktion starten → INSERTs → Bestätigung

Rollback-Anweisung: Der Agent erzeugt ein ROLLBACK-Skript bevor er Step 4 beginnt.
```

---

## Lösung 4.4-A — Mini-Sprint-Plan (Bestellhistorie)

| Schritt | Was | Tool | Prompt-Stichwort | Prüfpunkt | Zeit KI | Zeit manuell |
|---|---|---|---|---|---|---|
| 1 | Anforderung → ViewModel | Claude | „OrderHistoryViewModel, OrderSummaryViewModel mit Pagination" | Alle UI-Felder? | 5 min | 20 min |
| 2 | Query-Service Interface | Claude | „IOrderQueryService.GetCustomerOrdersAsync paginiert" | Signature korrekt? | 3 min | 10 min |
| 3 | EF Core Abfrage | Claude | „EF Core 9 Include + Pagination, N+1 vermeiden" | Kein N+1? Performance? | 7 min | 25 min |
| 4 | Controller | Copilot | Inline completion | Review nötig | 5 min | 15 min |
| 5 | Razor Views | Claude | „Index + Details View mit Bootstrap, Pagination-Controls" | HTML korrekt? | 10 min | 45 min |
| 6 | Unit-Tests | Claude | „Tests für Query-Service + Controller" | Coverage ok? | 10 min | 40 min |
| **Gesamt** | | | | | **40 min** | **155 min** |

**Pflicht-Prüfpunkte (menschlich):**
- Nach Schritt 3: Ist die Query performant? `.AsNoTracking()` gesetzt?
- Nach Schritt 5: Responsive? Barrierefreiheit?
- Nach Schritt 6: Testen die Tests wirklich das Richtige?
