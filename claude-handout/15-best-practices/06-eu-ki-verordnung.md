# Best Practices – EU-KI-Verordnung (AI Act)

**Block:** 30 min | **Tag 4**

---

## Was ist die EU-KI-Verordnung?

Die **EU AI Act** (Verordnung (EU) 2024/1689) ist der EU-weite Rechtsrahmen für den Umgang mit KI-Systemen. Sie ist am 1. August 2024 in Kraft getreten und wird gestaffelt anwendbar (die meisten Pflichten ab 2. August 2026, einzelne Verbote bereits seit Februar 2025).

> Rechtsstand vor dem Unterrichten immer aktuell prüfen – dies ist keine Rechtsberatung, sondern eine Einordnung für den Entwickler-Alltag.

## Risikobasierter Ansatz

| Risikostufe          | Beispiel                                           | Konsequenz                                                    |
| -------------------- | -------------------------------------------------- | ------------------------------------------------------------- |
| Unannehmbares Risiko | Social Scoring, bestimmte biometrische Überwachung | Verboten                                                      |
| Hochrisiko           | KI in kritischer Infrastruktur, Personalauswahl    | Strenge Auflagen (Dokumentation, Risikomanagement)            |
| Begrenztes Risiko    | Chatbots, generative KI-Tools                      | Transparenzpflichten (z. B. Kennzeichnung von KI-Interaktion) |
| Minimales Risiko     | Spamfilter, viele Alltagsanwendungen               | Keine besonderen Pflichten                                    |

**Claude Code** fällt für die meisten Teams unter "begrenztes Risiko" (KI-gestütztes Entwicklerwerkzeug) – relevant sind vor allem Transparenz- und Sorgfaltspflichten, nicht die strengen Hochrisiko-Auflagen.

## Was das für Entwickler:innen konkret bedeutet

- **Transparenz:** KI-generierter Code sollte im Team erkennbar/nachvollziehbar bleiben (z. B. über Commit-Konventionen oder Review-Vermerke)
- **Verantwortung bleibt beim Menschen:** Auch bei automatisiertem Code über Headless-Modus (Modul 11) oder delegierte Agents (Modul 15) bleibt die rechtliche Verantwortung für ausgeliefertem Code beim Unternehmen/den Entwickler:innen (siehe Modul 01f – Recht & Security)
- **Dokumentationspflichten** betreffen vor allem Unternehmen, die KI-Systeme selbst entwickeln/anbieten – weniger die reine Nutzung von Tools wie Claude Code
- **DSGVO gilt zusätzlich und unabhängig** vom AI Act, insbesondere bei personenbezogenen Daten in `CLAUDE.md`, Prompts oder Skills

## Praxis-Tipp

> Keine sensiblen/personenbezogenen Daten in Prompts, `CLAUDE.md` oder Skills einfügen, unabhängig vom AI-Act-Risiko-Level – das ist bereits eine Grundregel aus der DSGVO (siehe Modul 01f).
