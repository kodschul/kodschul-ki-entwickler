---
name: bug-finder
description: Analysiert Python-Code auf unbehandelte Exceptions, fehlende Input-Validierung bei Flask-Routen, hardcodierte Werte (Passwörter, Tokens, Ports) und fehlende Tests für neue Funktionen. Aktivieren, wenn jemand nach Fehlern, Bugs, Problemen oder Schwachstellen im Code fragt.
---

# Bug Finder

Analysiere den relevanten Python-Code (den aktuellen Diff, die genannte Datei, oder bei
allgemeiner Frage das ganze Projekt) systematisch auf die folgenden vier Kategorien:

## 1. Unbehandelte Exceptions

- Datei-I/O, JSON-Parsing, Netzwerk- oder Dict-/List-Zugriffe ohne try/except, die bei
  ungültigen Daten oder fehlenden Dateien abstürzen.
- Zu breite `except:`- oder `except Exception:`-Blöcke, die Fehler verschlucken statt sie
  sinnvoll zu behandeln oder weiterzugeben.
- Stellen, an denen ein Fehler den Flask-Request mit einem rohen 500er statt einer
  kontrollierten Antwort beendet.

## 2. Fehlende Input-Validierung bei Flask-Routen

- `request.form`, `request.args`, `request.json` oder URL-Parameter (z. B. `<id>`), die
  ungeprüft weiterverwendet werden (kein Trimmen, kein Leer-Check, kein Typ-/Format-Check).
- Fehlende Prüfung, ob eine ID/ein Objekt überhaupt existiert, bevor darauf zugegriffen wird.
- Fehlende Längen-/Format-Grenzen, die zu unerwartetem Verhalten oder Datenmüll führen können.

## 3. Hardcodierte Werte

- Passwörter, API-Keys, Tokens, Secrets direkt im Code statt in Umgebungsvariablen/Config.
- Hardcodierte Ports, Hosts oder Dateipfade, die Deployment/Portabilität einschränken.
- `app.secret_key`, Debug-Flags oder ähnliche sicherheitsrelevante Konstanten fest im Code.

## 4. Fehlende Tests für neue Funktionen

- Neue oder geänderte Routen/Funktionen ohne zugehörigen Test in `test_app.py` (oder der
  passenden Testdatei).
- Fehlende Tests für Edge Cases, die in der Spec als Akzeptanzkriterium genannt sind
  (z. B. leere Eingabe, nicht existierende ID).

## Vorgehen

1. Identifiziere den zu prüfenden Code (Diff, genannte Datei, oder Projekt-weit falls nichts
   spezifiziert wurde).
2. Gehe die vier Kategorien der Reihe nach durch und sammle konkrete Fundstellen mit
   Datei:Zeile.
3. Gib pro Fund: was das Problem ist, warum es ein Problem ist (konkretes Fehlerszenario),
   und einen Vorschlag zur Behebung.
4. Wenn nichts gefunden wurde, sage das explizit statt Fundstellen zu erfinden.
5. Biete an, die Fixes umzusetzen — führe sie aber nur nach Bestätigung durch.
