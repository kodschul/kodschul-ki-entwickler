# 14d – Agent Skills als toolübergreifender Standard

**Seit wann:** Agent Skills (`SKILL.md`) wurden ursprünglich für Claude Code entwickelt; im Laufe von 2025 begannen auch andere Anbieter (u. a. GitHub Copilot, siehe eigener Kurs) ein vergleichbares Konzept zu übernehmen.

> Vor dem Unterrichten prüfen, ob sich das Dateiformat/die Konventionen inzwischen zwischen den Tools angeglichen haben oder weiterhin leicht unterscheiden.

---

## Was ist neu?

Was in Modul 06 als Claude-Code-spezifisches Feature eingeführt wurde, entwickelt sich zunehmend zu einem **werkzeugübergreifenden Muster**: Eine `SKILL.md`-Datei mit `name`/`description` im Frontmatter, die eine wiederverwendbare Fähigkeit beschreibt und situativ aktiviert wird.

```
.claude/skills/<name>/SKILL.md      ← Claude Code (Ursprung)
.github/skills/<name>/SKILL.md      ← von anderen Tools übernommenes, ähnliches Konzept
```

## Warum wichtig?

- Skills, die für ein Projekt geschrieben wurden, lassen sich leichter auf andere Tools übertragen, wenn das Grundformat kompatibel bleibt
- Teams, die mehrere KI-Tools parallel einsetzen (siehe Modul 15 – Best Practices), profitieren von einem gemeinsamen Vokabular statt tool-spezifischer Insellösungen

## Praxis-Tipp

> Skills so schreiben, dass sie **werkzeugunabhängig** verständlich bleiben (klare `description`, keine Claude-Code-spezifischen Tool-Namen in der Kernlogik) – das erleichtert eine spätere Portierung, falls das Team das Tool wechselt oder ergänzt.
