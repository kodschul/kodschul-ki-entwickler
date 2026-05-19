# Modul 2 — Übungen

---

## Übung 2.1-A — Anbieter-Steckbriefe erstellen

Recherchieren Sie (z. B. mit Perplexity oder Phind) und erstellen Sie für **drei** der folgenden Anbieter einen Steckbrief. Nutzen Sie dabei das vorgegebene Format.

Anbieter zur Auswahl: OpenAI · Anthropic · Google · Mistral · GitHub (Copilot)

**Steckbrief-Format:**
```
Anbieter:         [Name]
Hauptmodell:      [Aktuelles Flaggschiff-Modell Stand 2025]
Kontextfenster:   [Token-Größe]
Serverstandort:   [Land / Region]
DSGVO-konform:    [Ja / Nein / Bedingt – kurze Begründung]
Preismodell:      [Free / Paid / API-Kosten]
Stärke:           [1–2 Sätze]
Schwäche:         [1–2 Sätze]
Ideal für:        [2–3 konkrete Entwickler-Szenarien]
```

---

## Übung 2.1-B — Auswahlentscheidung für ein konkretes Szenario

**Szenario:** Sie arbeiten als Entwickler bei einem deutschen Krankenhaus. Die IT-Abteilung soll KI in der Software-Entwicklung für das interne Patientenmanagementsystem einsetzen.

Beantworten Sie folgende Fragen ausführlich:
1. Welche KI-Dienste scheiden sofort aus und warum?
2. Welche Anbieter kommen grundsätzlich in Frage?
3. Welche vertraglichen und technischen Voraussetzungen müssen zwingend erfüllt sein?
4. Skizzieren Sie eine datenschutzkonforme Architektur für den KI-Einsatz (Flussdiagramm oder beschreibend).

---

## Übung 2.2-A — Kopf-an-Kopf-Vergleich

Stellen Sie **denselben Prompt** an zwei verschiedene KI-Systeme (z. B. Claude und ChatGPT) und vergleichen Sie die Ergebnisse systematisch.

**Test-Prompt:**
```
Du bist ein erfahrener .NET-Architekt.

Ich baue ein Event-Driven-System mit ASP.NET Core 9.
Komponente A sendet Ereignisse, Komponente B verarbeitet sie asynchron.

Aufgabe: Erkläre mir die drei gängigsten Lösungsansätze in .NET:
- Je ein kurzes, kompilierbares Code-Beispiel
- Vor- und Nachteile für jede Variante
- Eine konkrete Empfehlung für ein 5-10-köpfiges Entwicklungsteam

Kontext: Mittelgroße Anwendung, kein Cloud-Zwang, kein Event Sourcing.
```

**Auswertungsbogen (für jedes System ausfüllen):**

| Kriterium | System A: _______ | System B: _______ |
|---|---|---|
| Code kompilierbar / korrekte Syntax? | | |
| Alle drei Ansätze vollständig? | | |
| Empfehlung konkret und begründet? | | |
| Verständlichkeit der Erklärungen | | |
| Moderne .NET 9 Features genutzt? | | |
| Länge / Detailtiefe (angemessen?) | | |

**Fazit:** Welches System würden Sie für diese Aufgabe bevorzugen und warum?

---

## Übung 2.2-B — GitHub Copilot praktisch erkunden

**Voraussetzung:** GitHub Copilot in Ihrer IDE verfügbar (Free-Tier oder Trial).

**Aufgabe A – Inline-Completion:**
Öffnen Sie eine neue C#-Datei und tippen Sie schrittweise folgende Kommentare. Beobachten Sie die Vorschläge von Copilot:

```csharp
// Erstelle eine Klasse Product als DDD-Entität mit Id, Name, Price und Stock
// Füge eine Methode hinzu die prüft ob genug Lagerbestand vorhanden ist
// Füge eine statische Factory-Methode Create mit Validierung hinzu
```

Notieren Sie:
- Wie vollständig ist der generierte Code?
- Welche Design-Entscheidungen hat Copilot getroffen?
- Was fehlt oder ist falsch?

**Aufgabe B – Copilot Chat:**
Nutzen Sie den Chat für folgende Befehle auf Ihrem generierten Code:
- `/explain` – Lassen Sie den Code erklären
- `/tests` – Tests generieren lassen
- `/fix` – Einen absichtlichen Fehler finden lassen (entfernen Sie z. B. die Validierung)

**Dokumentation:** Was hat überrascht? Was hat gut funktioniert? Wo müssen Sie manuell eingreifen?

---

## Übung 2.3-A — Perplexity für technische Recherche nutzen

Führen Sie folgende Recherchen auf perplexity.ai durch und bewerten Sie die Ergebnisse.

**Recherche-Aufgaben:**
1. „Was ist neu in Entity Framework Core 9 gegenüber EF Core 8?"
2. „Welche NuGet-Pakete empfehlen sich für Resilience und Retry in ASP.NET Core 9?"
3. „MediatR vs. Wolverine für CQRS in .NET – Vergleich 2025"

**Bewertung pro Recherche:**

| Kriterium | Ergebnis |
|---|---|
| Quellen angegeben (ja/nein)? | |
| Quellen vertrauenswürdig? | |
| Informationen aktuell (Datum prüfen)? | |
| Unterschied zu Google-Suche? | |
| Wo liegen die Grenzen? | |

---

## Übung 2.3-B — Multi-Tool-Challenge

Lösen Sie folgende Entwicklungsaufgabe mit **mindestens drei verschiedenen KI-Tools**. Dokumentieren Sie welches Tool Sie wann eingesetzt haben.

**Aufgabe:**
> Implementieren Sie einen `EmailNotificationService` in C# (.NET 9), der beim Versand einer Bestellung eine E-Mail sendet. Nutzen Sie das NuGet-Paket **MailKit**.

**Empfohlener Workflow:**
1. **Perplexity/Phind:** MailKit recherchieren (aktuelle Version, grundlegende API, SmtpClient-Nutzung)
2. **Claude/ChatGPT:** Service-Klasse mit Interface generieren lassen
3. **GitHub Copilot:** Code in IDE vervollständigen und verfeinern
4. **Claude/ChatGPT:** Unit-Tests mit gemocktem SMTP generieren

**Dokumentationsvorlage:**

| Schritt | Tool | Prompt (Kurzform) | Ergebnis | Qualität 1–5 |
|---|---|---|---|---|
| 1 Recherche | | | | |
| 2 Service generieren | | | | |
| 3 Verfeinern | | | | |
| 4 Tests | | | | |

---

## Übung 2.4-A — Entscheidungsmatrix für Ihr Team

**Szenario:** Sie arbeiten in einem 8-köpfigen .NET-Entwicklungsteam bei einem deutschen Finanzdienstleister. Sie sollen eine KI-Tool-Strategie für das nächste Jahr entwickeln.

Füllen Sie die Matrix aus und ergänzen Sie die Kostenschätzung:

| Aufgabe | Häufigkeit | Empfohlenes Tool | Begründung | Datenschutz-Risiko (L/M/H) |
|---|---|---|---|---|
| Tägliche Code-Completion | Täglich | | | |
| API-Dokumentation lesen | Täglich | | | |
| Unit-Tests schreiben | Täglich | | | |
| Bug-Analyse / Debugging | Wöchentlich | | | |
| Architektur-Reviews | Monatlich | | | |
| Anforderungen analysieren | Wöchentlich | | | |
| Library-/API-Auswahl | Monatlich | | | |

**Kostenschätzung:** Berechnen Sie die monatlichen Gesamtkosten für Ihr Team (8 Entwickler) mit den gewählten Tools.

---

## Übung 2.4-B — Prompt-Portierung zwischen Tools

Testen Sie ob ein gut formulierter Prompt auf verschiedenen KI-Systemen ähnliche Qualität liefert.

**Verwenden Sie exakt diesen Prompt bei mindestens zwei Tools:**

```
Du bist erfahrener C# .NET 9 Entwickler mit DDD-Expertise.

Erstelle ein Repository-Interface und eine EF Core 9 Implementierung
für eine Order-Entität mit diesen Methoden:
- GetByIdAsync(Guid id, CancellationToken ct) → Order?
- GetByCustomerIdAsync(Guid customerId, int page, int pageSize, CancellationToken ct) → PagedResult<Order>
- GetPendingOrdersAsync(CancellationToken ct) → IReadOnlyList<Order>
  (Status: Open oder Confirmed)
- SaveAsync(Order order, CancellationToken ct)
  (Add wenn neu, Update wenn vorhanden)
- SoftDeleteAsync(Guid id, CancellationToken ct)
  (setzt IsDeleted = true, DeletedAt = DateTime.UtcNow)

Anforderungen:
- .NET 9 / C# 13
- Nullable Reference Types aktiviert
- CancellationToken in allen async-Methoden
- XML-Dokumentation für alle public Member
- Zuerst Interface, dann Implementierung
```

**Vergleichsmatrix:**

| Kriterium | Tool 1: _______ | Tool 2: _______ |
|---|---|---|
| Alle 5 Methoden implementiert? | | |
| Code kompilierbar? | | |
| CancellationToken überall? | | |
| Nullable korrekt behandelt? | | |
| XML-Docs vorhanden? | | |
| Modernes C# 13 genutzt? | | |
| Gesamtqualität (1–5) | | |
