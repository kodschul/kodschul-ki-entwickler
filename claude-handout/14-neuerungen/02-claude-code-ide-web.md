# 14b – Claude Code in der IDE & im Web

**Seit wann:** Die VS Code/JetBrains-Erweiterung sowie ein Web-Interface für Claude Code wurden im Laufe von 2025 ergänzt, nachdem Claude Code zunächst rein terminal-basiert gestartet ist.

> Vor dem Unterrichten aktuellen Stand prüfen – dieser Bereich hat sich seit dem Terminal-only-Start am schnellsten weiterentwickelt.

---

## Was ist neu?

Claude Code war ursprünglich ein reines CLI-Tool (Modul 02). Mittlerweile gibt es zusätzliche Zugänge:

- **IDE-Erweiterungen** (VS Code, JetBrains): Diffs, Datei-Kontext und Terminal-Ausgabe direkt im Editor, ohne separates Terminal-Fenster
- **Claude Code im Browser/Web**: Aufgaben delegieren, ohne lokale Installation – ähnlich in der Idee zum GitHub Copilot Coding Agent (cloud-seitig)

```
Terminal-CLI (Ursprung)  →  IDE-Erweiterung  →  Web/Cloud-Zugang
   Modul 02                  Diffs im Editor      delegierbar, ohne lokales Setup
```

## Warum wichtig?

- Senkt die Einstiegshürde für Entwickler:innen, die primär in der IDE arbeiten
- Der Cloud-/Web-Zugang erlaubt Delegation ähnlich der in Modul 15 (Parallele Sessions & Delegation) beschriebenen Workflows – Aufgabe abgeben, ohne die eigene Session zu blockieren

## Abgrenzung

| Terminal-CLI                           | IDE-Erweiterung                             | Web/Cloud                          |
| -------------------------------------- | ------------------------------------------- | ---------------------------------- |
| Volle Kontrolle, alle Flags (Modul 11) | Diffs direkt im Editor sichtbar             | Keine lokale Installation nötig    |
| Für Automation/Skripte am mächtigsten  | Guter Alltags-Workflow für IDE-Nutzer:innen | Für Delegation an andere/unterwegs |
