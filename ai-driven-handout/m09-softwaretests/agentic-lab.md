# m09 — Agentic Lab: Softwaretests mit Copilot

Drei Dateien — sofort in dein Projekt kopieren und loslegen.

---

## 1. `.github/instructions/testing.instructions.md`

```markdown
---
applyTo: "HotelApp.Tests/**/*.cs"
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

1. Lese alle `.cs`-Dateien unter `HotelApp.Domain/` und `HotelApp.Application/`
2. Prüfe welche Klassen/Methoden noch keine Tests unter `HotelApp.Tests/` haben
3. Generiere für jede ungetestete Klasse eine vollständige Testdatei unter `HotelApp.Tests/`
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
HotelApp.Domain/*.cs + HotelApp.Application/*.cs  →  [test-generator]  →  HotelApp.Tests/**Tests.cs
                                                                         →  test-coverage-status.md
```

---

## Sofort ausprobieren

```
# In Copilot Chat (Agent Mode):
Lese alle Klassen unter HotelApp.Domain/ und HotelApp.Application/.
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

---

## 4. `.github/skills/test-scaffolder/SKILL.md`

Per `/test-scaffolder` abrufbar — generiert vollständige xUnit Testsuiten auf Knopfdruck.

```markdown
---
name: test-scaffolder
description: >
  Generates complete xUnit test suites with FluentAssertions for .NET projects.
  Use when writing unit tests for domain entities or application services,
  covering happy path, boundary values, error cases, and invalid state
  transitions. Also generates a test coverage status report.
  Trigger words: xUnit, unit test, FluentAssertions, TDD, test coverage,
  test suite, arrange act assert, test generation, missing tests, test scaffold.
---

# Test Scaffolder

Generiert vollständige xUnit Testsuiten für Domain- und Application-Klassen.

## Wann verwenden

- Unit Tests für neue oder ungetestete Klassen anlegen
- Pflicht-Szenarien sicherstellen (Happy Path, Grenzwerte, Fehler)
- Test-Coverage-Status im Projekt dokumentieren
- Testdaten und Factory-Methoden generieren

## Voraussetzungen

- Quellklassen unter `HotelApp.Domain/` und / oder `HotelApp.Application/`
- xUnit + FluentAssertions im Testprojekt installiert
- Konventionen aus [`references/testing-conventions.md`](./references/testing-conventions.md)

## Pflicht-Szenarien pro Methode

| Szenario         | Was prüfen                                       |
| ---------------- | ------------------------------------------------ |
| Happy Path       | Gültige Eingabe → erwarteter Zustand             |
| Grenzwert        | Genau am Limit, knapp darunter, knapp darüber    |
| Fehlerfälle      | Ungültige Eingabe → korrekte Exception + Message |
| Zustandsübergang | Falscher Status → `InvalidOperationException`    |

## Vorgehen

1. Lese alle `.cs`-Dateien unter `HotelApp.Domain/` und `HotelApp.Application/`
2. Identifiziere Klassen ohne entsprechende `*Tests.cs`-Datei unter `HotelApp.Tests/`
3. Generiere Testdatei mit privater `Create[Klasse]()`-Factory
4. Abdeckung: alle `public`-Methoden mit allen Pflicht-Szenarien
5. Erstelle `test-coverage-status.md`

## Namenskonvention
```

MethodName_Szenario_ErwarteterZustand
→ Cancel_LessThan24HoursBeforeCheckIn_ChargesFullFee

```

## Beispiel-Aufruf

```

/test-scaffolder
Generiere alle fehlenden xUnit Tests für HotelApp.Domain/ und HotelApp.Application/

```

```

**Skill-Struktur anlegen:**

```
.github/skills/test-scaffolder/
├── SKILL.md
└── references/
    └── testing-conventions.md    ← Regeln aus testing.instructions.md
```
