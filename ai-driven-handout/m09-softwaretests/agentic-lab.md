# m09 — Agentic Lab: Softwaretests mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/testing.instructions.md`

```markdown
---
applyTo: "**/*.Tests/**/*.cs,**/*Tests.cs,**/*Specs.cs"
---

## Test-Konventionen (xUnit + FluentAssertions)

- Testprojekte heißen `[Projektname].Tests` und liegen auf gleicher Ebene wie das Quellprojekt
- Namenskonvention: `MethodName_Szenario_ErwarteterZustand`
  - Beispiel: `Cancel_LessThan24HoursBeforeCheckIn_ChargesFullFee`
- Aufbau: Arrange / Act / Assert — immer drei Blöcke, durch Leerzeile getrennt
- `FluentAssertions` für alle Assertions — niemals `Assert.Equal`
- Testdaten via private Hilfsmethoden oder `static` Factory-Methoden — keine Magic Strings
- Jeder Test prüft genau eine Sache — niemals mehrere Act-Schritte pro Test
- Happy Path, Grenzwert-Tests und Fehlerfälle sind Pflicht für jede Methode
- Exceptions testen mit: `act.Should().Throw<ExceptionType>()`
- Async-Tests: `async Task` — niemals `async void`
- EF Core Integrationstests: `UseInMemoryDatabase` oder Testcontainers
```

---

## 2. `.github/prompts/generate-tests.prompt.md`

Aufruf: `/generate-tests`

```markdown
---
name: generate-tests
description: Generiert vollständige xUnit Tests mit FluentAssertions für eine Klasse oder Methode
---

Du bist Senior C#-Entwickler mit TDD-Erfahrung (.NET 9, xUnit, FluentAssertions).

Generiere vollständige xUnit Tests für den markierten Code.

Pflicht-Szenarien für jede Methode:

- Happy Path (gültige Eingabe → erwarteter Zustand)
- Alle Grenzwerte (genau am Limit, knapp darunter, knapp darüber)
- Alle Fehlerfälle (ungültige Eingaben → korrekte Exception)
- Ungültige Zustandsübergänge (falsche Status → InvalidOperationException)

Regeln:

- Namenskonvention: `MethodName_Szenario_ErwarteterZustand`
- FluentAssertions für alle Assertions
- Private Hilfsmethode `Create[Klasse]()` für Testdaten
- Arrange / Act / Assert Struktur (durch Leerzeile getrennt)
- Nur Code, keine Erklärungen

Code:
{{selection}}
```

---

## 3. `.github/agents/test-generator.agent.md`

```markdown
---
name: test-generator
description: >
  Liest alle Domain- und Application-Klassen und generiert vollständige
  xUnit Testsuites für alle noch nicht getesteten Methoden
tools:
  - codebase
  - new_file
---

Du bist Senior C#-Entwickler mit TDD-Erfahrung (.NET 9, xUnit, FluentAssertions).

Aufgabe:

1. Lese alle `.cs`-Dateien unter `Domain/` und `Application/`
2. Prüfe welche Klassen/Methoden noch keine Tests unter `*.Tests/` haben
3. Generiere für jede ungetestete Klasse eine vollständige Testdatei unter `[Projektname].Tests/`
4. Folge der Namenskonvention: `[Klassenname]Tests.cs`
5. Erstelle `test-coverage-status.md` mit: Klasse → Getestet (Ja/Nein) → Fehlende Szenarien

Test-Pflichtszenarien pro Methode:

- Happy Path
- Alle Grenzwerte (genau am Limit)
- Alle Fehlerfälle (korrekte Exception + Message)
- Ungültige Zustandsübergänge

Namenskonvention: `MethodName_Szenario_ErwarteterZustand`
Frameworks: xUnit, FluentAssertions
```

**Workflow:**

```
Domain/*.cs + Application/*.cs  →  [test-generator]  →  *.Tests/**Tests.cs
                                                     →  test-coverage-status.md
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese alle Klassen unter Domain/ und Application/.
Generiere vollständige xUnit Testsuites für alle Klassen die noch keine Tests haben.
Erstelle danach test-coverage-status.md mit dem aktuellen Stand.
```

---

## Bonus — Testdaten per Prompt generieren

```
# In Copilot Chat:
Generiere 10 realistische Testdatensätze für die Booking-Klasse als C# Liste.
Variiere: gültige Buchungen, überfällige Buchungen, stornierte Buchungen,
Stammkunden-Buchungen. Verwende DateOnly für Datumsfelder.
```
