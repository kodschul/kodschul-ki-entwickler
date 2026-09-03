# 14c – Copilot Code Review

**Seit wann:** Preview seit Ende 2024, seit ca. April 2025 **General Availability**. Seither laufend erweitert (u. a. Effort-Level-Einstellungen und die Möglichkeit, PRs direkt zu genehmigen, kamen im Verlauf von 2026 dazu).

> Genaues GA-Datum und aktuellen Funktionsstand immer gegen den [GitHub Changelog](https://github.blog/changelog/?label=copilot) prüfen – dieser Bereich ändert sich häufig.

---

## Was ist neu?

GitHub Copilot kann automatisiert **Pull Requests reviewen** – entweder auf Anfrage ("Request review from Copilot") oder automatisch per Repository-Regel.

```
PR wird geöffnet
  → Copilot analysiert Diff + Projektkontext (inkl. copilot-instructions.md)
  → hinterlässt Inline-Kommentare direkt im PR
  → Team behandelt Copilot-Kommentare wie die eines menschlichen Reviewers
```

**Einrichtung (Repository-Ebene):**

1. Repo-Settings → Rules → Branch-Regel mit "Request pull request review from Copilot"
2. Optional: eigene Review-Instructions in `.github/copilot-instructions.md` hinterlegen (Abschnitt "Do/Don't" wird auch beim Review berücksichtigt, siehe Modul 05)

**Wann sinnvoll:**

| Sinnvoll                                           | Kein Ersatz für                           |
| -------------------------------------------------- | ----------------------------------------- |
| Erste automatische Prüfung vor menschlichem Review | Fachliches / Domain-Review durch das Team |
| Konsistenz-Checks gegen Team-Konventionen          | Sicherheits-Audit bei kritischem Code     |
| Frühes Feedback für Entwickler ohne Wartezeit      | Verantwortungsübernahme (siehe Modul 06)  |
