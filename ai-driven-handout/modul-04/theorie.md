# Modul 4 — AI-Agenten und Multi-Step-Prompting

## Lab 4.1 — AI-Agenten als Arbeitsmodell

### Agenten vs. einfacher Chat

```
Chat-Prompt:  Frage → Antwort (ein Schritt, kein Gedächtnis)

AI-Agent:     Ziel definiert
                 ↓
              Plan erstellt
                 ↓
              Werkzeug A aufgerufen (z. B. Dateisystem)
                 ↓
              Zwischenergebnis bewertet
                 ↓
              Werkzeug B aufgerufen (z. B. Terminal)
                 ↓
              Ergebnis geliefert
```

**Beispiele aus der Entwicklungspraxis:**
- GitHub Copilot Workspace: Liest Issue → plant Änderungen → schreibt Code → erstellt PR
- Cursor Cascade: Liest Fehlermeldung → sucht Ursache → ändert Dateien → führt Tests aus
- Claude + MCP: Zugriff auf Filesystem, Terminal, Browser, Datenbank

### Chancen und Risiken

| Chancen | Risiken |
|---|---|
| Automatisierung mehrstufiger Workflows | Fehler aus Schritt 2 pflanzt sich bis Schritt 8 fort |
| Konsistente, wiederholbare Abläufe | Schwer debuggbar bei langen Ketten |
| Schnell bei klar definierten Aufgaben | Kein Kontextverlust zwischen Schritten bemerkt |
| 24/7 ohne Ermüdung | Token-Kosten bei langen Läufen erheblich |

**Human-in-the-Loop:** Nach kritischen Schritten muss ein Mensch das Ergebnis prüfen, bevor fortgefahren wird.

---

## Lab 4.2 — Multi-Step-Prompting

### Aufgaben in Schritte zerlegen

**Anti-Pattern:**
```
Analysiere die Anforderungen, erstelle das Domänenmodell, implementiere alle Klassen,
schreibe EF Core Konfigurationen, Migrationen, Tests und Dokumentation.
→ Ergebnis: Oberflächlich, viele Fehler, schwer zu korrigieren
```

**Best Practice – Sequentielle Kette:**
```
Prompt 1: Anforderung analysieren → Entitäten und Events identifizieren
Prompt 2: [Ergebnis 1] → C#-Klassen generieren
Prompt 3: [Klassen] → EF Core Konfiguration
Prompt 4: [Klassen] → Unit-Tests
Prompt 5: [Alles] → README.md generieren
```

### Prüfpunkte nach jedem Schritt

Nach jedem KI-Schritt prüfen:
1. **Fachlich korrekt?** Stimmt das Ergebnis mit der Anforderung überein?
2. **Technisch korrekt?** Kompiliert der Code? Sind Patterns richtig?
3. **Vollständig?** Wurden alle geforderten Elemente erstellt?
4. **Erst dann:** Weiter zum nächsten Prompt

---

## Lab 4.3 — Workflows systematisch strukturieren

### Wiederholbarer Feature-Workflow

```
STEP 1 — Anforderungsanalyse
Input:  User Story + Akzeptanzkriterien
Prompt: "Analysiere nach DDD: Entitäten, Methoden, Events, Validierungsregeln, Edge Cases"
Prüfe: Alle Akzeptanzkriterien abgedeckt?

STEP 2 — Domänenklassen
Input:  Analyseergebnis aus Step 1
Prompt: "[Analyse] → Erstelle DDD-konforme C#-Klassen (.NET 9, private setter, XML-Docs)"
Prüfe: Kompiliert? private setter? Validierung vorhanden?

STEP 3 — Tests (TDD)
Input:  Klassen aus Step 2
Prompt: "[Klassen] → Erstelle xUnit + FluentAssertions Tests für alle öffentlichen Methoden"
Prüfe: Alle Testfälle vorhanden? Tests kompilieren? Rot (noch keine Implementierung)?

STEP 4 — Implementierung
Input:  Tests aus Step 3 + Klassen aus Step 2
Prompt: "Implementiere die Methoden so, dass alle Tests grün werden"
Prüfe: Alle Tests grün? Keine Implementierung die über Tests hinausgeht?

STEP 5 — Refactoring-Review
Input:  Implementierung aus Step 4
Prompt: "Identifiziere Verbesserungspotenzial: DDD, Performance, Lesbarkeit"
Prüfe: Welche Vorschläge übernehmen?
```

---

## Lab 4.4 — Mehrstufige KI-Unterstützung in der Praxis

### Grenzen von Multi-Step-Prompting

**Wann es versagt:**
- Kette zu lang → Kontext geht verloren oder Fenster wird zu groß
- Schritt 2 enthält Fehler → pflanzt sich unweigerlich fort
- Aufgabe ist zu vage → jeder Schritt generiert etwas anderes als erwartet

**Wann es glänzt:**
- Klare, sequentielle Aufgaben mit prüfbaren Zwischenergebnissen
- Jeder Schritt ist unabhängig validierbar
- Standardisierter Workflow der sich wiederholt (z. B. für jedes neue Feature)

### Qualitätsreflexion

Nach jedem Multi-Step-Durchlauf fragen:
1. Könnte ich den generierten Code einem Kollegen vollständig erklären?
2. Haben sich Fehler aus frühen Schritten fortgepflanzt?
3. War der Aufwand kleiner als manuelle Implementierung?
4. Was würde ich beim nächsten Mal anders machen?
