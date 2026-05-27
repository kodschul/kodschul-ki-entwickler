---
name: user-environment
description: Arbeitsumgebung und technische Einschränkungen des Nutzers
metadata:
  type: user
---

Nutzer arbeitet auf einem lokalen Arbeitsrechner ohne Admin-Rechte.

**Konsequenz:** Keine Software-Installationen möglich. Alle Anwendungen müssen ohne Installation lokal lauffähig sein.

**How to apply:** Beim Vorschlagen von Tools, Laufzeitumgebungen oder Abhängigkeiten immer prüfen, ob diese ohne Admin-Rechte / ohne Installer nutzbar sind. Bevorzuge: portable Binaries, npx, uvx, bereits installierte Laufzeiten (Node, Python via pyenv o.ä.), Browser-basierte Lösungen oder containerlose Ansätze.
