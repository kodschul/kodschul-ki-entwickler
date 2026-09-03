# 12b – Spec-Kit: Strukturiertes Spec-Driven Development

**Block:** Teil von Modul 12 | **Tag 4**

---

## Was ist das Spec-Kit?

Das Spec-Kit ist ein **eingebauter Workflow in Claude Code** für strukturiertes, dreistufiges Entwickeln:

```
/spec plan    → Claude erstellt einen Plan aus deiner Anforderung
/spec         → Claude implementiert nach dem Plan
/spec test    → Claude schreibt Tests gegen den Plan
```

> Kein freies Improvisieren. Claude folgt dem Plan – nicht seiner eigenen Interpretation.

---

## Wie funktioniert das unter der Haube?

```
Nutzer: /spec plan "Fälligkeitsdatum für Todos"
  → Claude analysiert Codebase
  → Erstellt SPEC.md mit: Änderungen, Dateien, Schritte
  → Wartet auf Bestätigung

Nutzer: /spec
  → Claude liest SPEC.md
  → Implementiert Schritt für Schritt
  → Hakt Schritte in SPEC.md ab

Nutzer: /spec test
  → Claude liest SPEC.md (Akzeptanzkriterien)
  → Schreibt Tests nur für das, was in der Spec steht
```

**Wichtig:** Claude verändert während `/spec` nichts außerhalb der in der Spec definierten Dateien.

---

## Warum / Wann nicht?

| Warum nutzen                             | Wann nicht                                    |
| ---------------------------------------- | --------------------------------------------- |
| Reproduzierbarer Workflow im Team        | Schneller Bugfix → direkt tippen              |
| Claude bleibt im Scope                   | Explorativer Prototyp → Spec zu früh          |
| Plan vor Code sichtbar + bestätigbar     | Feature ändert sich noch → Spec wird veraltet |
| Tests aus Akzeptanzkriterien generierbar | Einmalige Migration / Skript                  |

---

## SPEC.md – Aufbau

```markdown
# Spec: Fälligkeitsdatum für Todos

## Ziel

Todos können ein optionales Fälligkeitsdatum bekommen.
Überfällige Todos werden rot markiert.

## Betroffene Dateien

- `app.py` – Routen /add und / anpassen
- `templates/index.html` – Datum anzeigen, rot markieren
- `test_app.py` – neue Tests hinzufügen

## Implementierungsschritte

- [ ] Feld `due_date` in /add-Route entgegennehmen
- [ ] Feld `due_date` in todos.json speichern
- [ ] Template: Datum-Eingabe im Formular
- [ ] Template: Datum in der Liste anzeigen
- [ ] Template: Rote Markierung wenn Datum < heute

## Akzeptanzkriterien

- [ ] Todo mit Datum speicherbar
- [ ] Todo ohne Datum funktioniert weiterhin
- [ ] Überfälliges Todo visuell hervorgehoben
- [ ] Datum korrekt in todos.json gespeichert
```

---

## Schritt-für-Schritt: Spec-Kit Workflow

**1. Plan erstellen**

```
/spec plan Fälligkeitsdatum für Todos
```

Claude analysiert `app.py`, `templates/`, `test_app.py` und schreibt `specs/due-dates-spec.md`. Vor der Implementierung prüfen: Sind alle betroffenen Dateien korrekt? Sind die Schritte sinnvoll sortiert? Fehlen Akzeptanzkriterien?

**2. Implementieren**

```
/spec
```

Claude arbeitet die Checkboxen von oben nach unten ab, hakt sie nach jedem Schritt ab. Abbruch jederzeit möglich – Spec bleibt erhalten, Fortschritt sichtbar.

**3. Tests generieren**

```
/spec test
```

**4. Review**

```
/spec review
```

Claude vergleicht Implementierung mit Spec und meldet Abweichungen.

---

## Spec-Kit vs. manuelle Spec

|                   | Spec-Kit (`/spec`)                      | Manuelle Spec                 |
| ----------------- | --------------------------------------- | ----------------------------- |
| **Erstellung**    | Claude analysiert Codebase selbst       | Du schreibst die Spec         |
| **Kontrolle**     | Claude schlägt vor, du bestätigst       | Volle Kontrolle von Anfang an |
| **Fortschritt**   | Checkboxen in SPEC.md                   | Manuell nachverfolgen         |
| **Empfohlen für** | Unbekannte Codebase, schneller Einstieg | Komplexe Features, Teamarbeit |

---

## Ordnerstruktur

```
1205/todo-app/
└── specs/
    ├── due-dates-spec.md     ← von /spec plan erzeugt
    └── due-dates.md          ← manuelle Spec (Modul 12)
```
