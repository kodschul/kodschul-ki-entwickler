# 06 – Was es sonst noch unbedingt zu beachten gilt

**Block:** 45 min | **Tag 1**

---

## Security-Fragen bei KI-generiertem Code

- KI kennt keine Threat-Models eures Projekts – generiert Code, der "funktioniert", nicht zwingend Code, der sicher ist
- Typische Risiken: fehlende Input-Validierung, unsichere Defaults, veraltete/kompromittierte Dependencies, hartkodierte Secrets
- Gegenmaßnahme: Security-Regeln in `CLAUDE.md`/eigenem `security-reviewer`-Agent (Modul 08) + verpflichtender Review, nie ungeprüft mergen
- Claude Code kann eigenständig Befehle ausführen – **`permissions.deny`** (Modul 05) ist die technische Leitplane gegen gefährliche Aktionen (`rm -rf`, `git push --force`, Schreibzugriff auf Systemdateien)

## Wer hat das Urheberrecht bei generiertem Code?

- Rechtslage uneinheitlich und in Bewegung – grober Konsens: rein KI-generierter Output ohne menschliche schöpferische Leistung ist in vielen Rechtsordnungen nicht (allein) urheberrechtsfähig
- Praktische Konsequenz: Herkunft/Trainingsdaten der genutzten KI kennen, Lizenzbedingungen des Anbieters (z. B. Anthropic Commercial Terms) beachten
- Bei Zweifeln: Rechtsabteilung einbeziehen, nicht selbst auslegen

## Wer haftet bei fehlerhaftem oder schadhaftem Code?

- KI-Anbieter haftet in der Regel nicht für Schäden durch generierten Code (siehe AGB/Lizenzbedingungen)
- Verantwortung bleibt bei der Person/Organisation, die den Code committed und freigibt – auch wenn Claude Code autonom gearbeitet hat
- Merksatz: **KI schlägt vor bzw. handelt, der Mensch verantwortet.**

## Privacy-by-design: Datenschutz einhalten

- Keine echten Kunden-/Personendaten in Prompts, `CLAUDE.md`, Screenshots oder Testdaten verwenden
- Prüfen, welcher Anthropic-Plan/API-Vertrag genutzt wird und ob Prompt-/Code-Daten zu Trainingszwecken verwendet werden (Business/Enterprise-Verträge regeln das i. d. R. explizit)
- Bei MCP-Servern (Modul 13) besonders vorsichtig sein: externe Server sehen ggf. Repo-Inhalte – nur vertrauenswürdige Server einbinden
- Siehe auch Modul 15 – EU-KI-Verordnung für den regulatorischen Rahmen
