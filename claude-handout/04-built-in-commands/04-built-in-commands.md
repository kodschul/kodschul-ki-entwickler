# 04 – Built-in Commands

**Block:** 90 min | **Tag 2**

---

## Was sind Built-in Commands?

Claude Code bringt bereits eine Reihe von **eingebauten Slash-Commands** mit – ohne dass du dafür etwas konfigurieren musst. Sie unterscheiden sich von Custom Commands (Modul 07), die du selbst als `.md`-Dateien anlegst.

```
> /help
```

zeigt die vollständige, aktuelle Liste – **immer die verlässlichste Quelle**, da sich Commands zwischen Versionen ändern können.

---

## Die wichtigsten Built-in Commands

| Command             | Zweck                                                             |
| ---------------------- | -------------------------------------------------------------------- |
| `/help`                 | Zeigt alle verfügbaren Commands                                      |
| `/clear`                | Leert den Konversationsverlauf, startet frischen Kontext              |
| `/compact`              | Fasst den bisherigen Verlauf zusammen, um Kontext/Tokens zu sparen (Modul 10) |
| `/cost`                 | Zeigt Token-/Kostenverbrauch der aktuellen Session                    |
| `/init`                 | Generiert eine erste `CLAUDE.md` aus der bestehenden Codebase          |
| `/permissions`          | Zeigt/ändert erlaubte bzw. gesperrte Befehle für die Session           |
| `/agents`               | Verwaltet Custom Agents (Modul 08)                                    |
| `/mcp`                  | Zeigt verbundene MCP-Server und deren Status (Modul 13)                |
| `/model`                | Wechselt das verwendete Modell                                        |
| `/review`               | Startet einen Code-Review-Workflow für den aktuellen Stand             |
| `/resume`               | Setzt eine frühere Session fort                                       |
| `/bug`                  | Meldet ein Problem mit Claude Code direkt an Anthropic                |
| `/doctor`               | Prüft die lokale Claude-Code-Installation auf Probleme                |

> Die exakte Liste kann sich mit neuen Claude-Code-Versionen ändern – `/help` in der aktuell installierten Version prüfen.

---

## Warum / Wann nicht?

| Warum nutzen                                | Wann nicht                                     |
| ---------------------------------------------- | --------------------------------------------------- |
| `/clear` bei Themenwechsel                       | Mitten in einer zusammenhängenden Aufgabe            |
| `/compact` bei langen Sessions                   | Kurze, einfache Sessions – kein Bedarf               |
| `/cost` zur Budget-Kontrolle im Team              | Irrelevant bei Pauschal-Abo ohne Nutzungsgrenzen     |
| `/init` bei neuem/unbekanntem Projekt             | `CLAUDE.md` existiert bereits und ist gepflegt       |

---

## Praktisches Beispiel: Session-Hygiene

```
> /cost
   Aktuelle Session: 42.000 Tokens

> /compact
   [Zusammenfassung des bisherigen Verlaufs]

> /cost
   Aktuelle Session: 8.500 Tokens
```

`/compact` reduziert den Kontext auf eine Zusammenfassung – sinnvoll bei langen, aber noch nicht abgeschlossenen Aufgaben. `/clear` dagegen verwirft den Kontext komplett und ist für einen echten Themenwechsel gedacht.
