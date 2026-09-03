# Best Practices – Große Codebases (Millionen Codezeilen)

**Block:** 30 min | **Tag 4**

---

## Das Problem bei sehr großen Repos

Bei Codebases mit mehreren Millionen Zeilen passt niemals "der ganze Code" in den Kontext eines Modells (Modul 10). Ohne gezielte Strategie durchsucht Claude entweder an der falschen Stelle oder verbraucht unnötig viele Tokens bei der Suche.

## Strategien

| Strategie                                  | Umsetzung                                                                                                     |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------- |
| Gezielte Aufgaben statt "durchsuche alles" | Konkreten Ordner/Datei/Funktion nennen (Modul 10)                                                             |
| Modularisierung ausnutzen                  | Verschachtelte `CLAUDE.md` pro Modul/Package statt einer globalen Datei (Modul 06)                            |
| Klare Ordnerstruktur pflegen               | Erleichtert Claudes eigene `Glob`/`Grep`-Suche erheblich                                                      |
| Aufgaben in kleinere Schritte zerlegen     | Statt "refactor das ganze Modul" lieber Datei-für-Datei oder Paket-für-Paket vorgehen                         |
| MCP-Server für Spezialwissen               | Eigene Server für z. B. interne Doku, Architektur-Entscheidungen (Modul 13)                                   |
| Subagenten für Recherche                   | Ein Subagent durchsucht/analysiert einen Teilbereich, die Hauptsession bekommt nur das Ergebnis (Modul 08/15) |

## Praktisches Vorgehen

```
1. Aufgabe eingrenzen: welches Modul/Package ist konkret betroffen?
2. Nur relevante Ordner/Dateien nennen, nicht das gesamte Repo
3. Bei unklarer Code-Struktur: erst Recherche-Schritt (Read-only-Agent), dann Umsetzung
4. Änderungen inkrementell testen statt eine riesige Änderung auf einmal
```

## Wichtig

> Große Codebases sind kein Grund, KI-Unterstützung zu meiden – sie erfordern nur bewussteres Kontext-Management. Die gleichen Prinzipien wie in Modul 10 gelten hier nur in größerem Maßstab.
