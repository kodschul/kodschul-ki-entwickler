# 04 – Generative KI in Softwareprojekten

**Block:** 45 min | **Tag 1**

---

## Requirements Engineering mit Künstlicher Intelligenz

- User Stories aus Stichpunkten generieren und verfeinern lassen (Claude als Sparringspartner im REPL)
- Akzeptanzkriterien vervollständigen lassen ("Welche Edge Cases fehlen in dieser Story?")
- Vorsicht: KI erfindet plausibel klingende, aber fachlich falsche Anforderungen – fachliche Prüfung bleibt Pflicht

## KI als Hilfe bei der Softwarekonzeption

- Architektur-Optionen gegenüberstellen lassen (Monolith vs. Microservices, für den konkreten Anwendungsfall)
- Domain-Modelle skizzieren lassen (Entities, Beziehungen) als Diskussionsgrundlage, nicht als Endergebnis
- Ideal für Spec-Driven Development (Modul 12): erst Spec/Plan, dann Code

## Coding Styles und Patterns mit generativer KI

- Bestehende Konventionen über `CLAUDE.md` (Modul 05/06) durchsetzen, statt bei jedem Prompt zu wiederholen
- Design Patterns vorschlagen und gegen Overengineering abwägen lassen – KI tendiert dazu, Patterns auch dort einzusetzen, wo einfacher Code reichen würde
- Style Guides (z. B. `ai-rules/styles-guide.md`) in `CLAUDE.md` verlinken, damit generierter Code sich nicht vom Team-Stil unterscheidet

---

## Zusammenspiel mit späteren Modulen

| Thema hier                        | Vertiefung in Modul                     |
| ----------------------------------- | ------------------------------------------ |
| Konventionen durchsetzen             | 05/06 – Konfiguration, `CLAUDE.md`, Skills |
| Spec vor Code                        | 12 – Spec-Driven Development               |
| Architektur-Kontext bereitstellen    | 05 – Konfiguration                         |
