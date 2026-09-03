# Intro – Arten von KI-Integrationen

**Block:** 30 min | **Tag 1**

---

## Warum dieser Einstieg?

Bevor es an die konkreten Copilot-Features geht, brauchen wir ein gemeinsames Vokabular: Nicht jede "KI im Editor" funktioniert gleich. Die Unterscheidung hilft später zu verstehen, warum z. B. Inline Completions anders reagieren als der Agent-Modus.

---

## Die vier Integrationsarten

| Art                           | Beispiel                    | Charakteristik                                         |
| ----------------------------- | --------------------------- | ------------------------------------------------------ |
| **Autocomplete / Ghost Text** | Copilot Inline Completions  | Reaktiv, kein Dialog, greift lokalen Kontext auf       |
| **Chat-Assistent**            | Copilot Chat (Ask-Modus)    | Dialogbasiert, beantwortet, ändert nichts selbst       |
| **Agentisch (in der IDE)**    | Copilot Agent-Modus         | Plant, nutzt Tools, editiert Dateien autonom in Loop   |
| **Agentisch (cloud-seitig)**  | GitHub Copilot Coding Agent | Läuft losgelöst von der IDE, arbeitet Issues zu PRs ab |

```
Autocomplete  →  Chat  →  Agent (lokal)  →  Agent (cloud)
   reaktiv        Dialog     Tool-Loop        vollautonom
   kein Ziel      1 Antwort  mehrere Schritte  eigener PR
```

---

## Rule-based vs. LLM-based

- **Regelbasiert** (klassische Linter, Snippets): deterministisch, 100 % nachvollziehbar, aber unflexibel.
- **LLM-basiert** (Copilot & Co.): probabilistisch, flexibel, aber nicht deterministisch – gleiche Eingabe kann leicht unterschiedliche Ausgabe liefern.

> Merksatz: Je autonomer die Integration, desto wichtiger werden Leitplanken (Instructions, Tool-Whitelists, Reviews) – Thema der kommenden Module.

---

## Wo ordnen sich bekannte Tools ein?

| Tool                        | Haupt-Integrationsart     |
| --------------------------- | ------------------------- |
| GitHub Copilot (Inline)     | Autocomplete              |
| GitHub Copilot Chat         | Chat + Agent (lokal)      |
| GitHub Copilot Coding Agent | Agent (cloud)             |
| Claude Code / Cursor        | Chat + Agent (lokal)      |
| ChatGPT / Claude (Web)      | Chat (kein Datei-Zugriff) |

---

## Was aus diesem Modul mitzunehmen ist

- Vier Integrationsarten unterscheiden zu können, hilft, Erwartungen an ein Feature realistisch einzuordnen.
- Der restliche Kurs bewegt sich von "reaktiv" (Modul 02) zu "vollautonom" (Modul 14).
