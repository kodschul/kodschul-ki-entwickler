# Best Practices – Große Codebases (Millionen Codezeilen)

**Block:** 30 min | **Tag 4**

---

## Das Problem bei sehr großen Repos

Bei Codebases mit mehreren Millionen Zeilen passt niemals "der ganze Code" in den Kontext eines Modells (siehe Modul 10 – Token-Management). Ohne gezielte Strategie sucht Copilot entweder an der falschen Stelle oder verbraucht unnötig viele Tokens/Requests bei der Suche.

## Strategien

| Strategie                              | Umsetzung                                                                                                   |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Gezielte Kontext-Referenzen            | `#file`, `#folder`, `#codebase`-Suche statt "durchsuche alles" (Modul 03)                                   |
| Modularisierung ausnutzen              | Instructions pro Modul/Package mit `applyTo`-Pattern statt einer globalen Datei (Modul 06)                  |
| Indexierung/Workspace-Struktur pflegen | Klare Ordnerstruktur und Namenskonventionen erleichtern gezielte Suche erheblich                            |
| Aufgaben in kleinere Schritte zerlegen | Statt "refactor das ganze Modul" lieber Datei-für-Datei oder Paket-für-Paket vorgehen                       |
| MCP-Server für Spezialwissen           | Eigene Server für z. B. interne Doku, Architektur-Entscheidungen (Modul 13)                                 |
| Subagenten für Recherche               | Ein Subagent durchsucht/analysiert einen Teilbereich, der Hauptagent bekommt nur das Ergebnis (Modul 14/15) |

## Praktisches Vorgehen

```
1. Aufgabe eingrenzen: welches Modul/Package ist konkret betroffen?
2. Nur relevante Ordner/Dateien referenzieren, nicht das gesamte Repo
3. Bei unklarer Code-Struktur: erst Recherche-Schritt (read-only), dann Umsetzung
4. Änderungen inkrementell testen statt eine riesige Änderung auf einmal
```

## Wichtig

> Große Codebases sind kein Grund, KI-Unterstützung zu meiden – sie erfordern nur bewussteres Kontext-Management. Die gleichen Prinzipien wie in Modul 10 gelten hier nur in größerem Maßstab.
