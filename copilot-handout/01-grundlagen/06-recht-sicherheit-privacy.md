# 06 – Was es sonst noch unbedingt zu beachten gilt

**Block:** 45 min | **Tag 1**

---

## Security-Fragen bei KI-generiertem Code

- KI kennt keine Threat-Models eures Projekts – generiert Code, der "funktioniert", nicht zwingend Code, der sicher ist
- Typische Risiken: fehlende Input-Validierung, unsichere Defaults, veraltete/kompromittierte Dependencies, hartkodierte Secrets
- Gegenmaßnahme: Security-Instructions (`.github/instructions/security.instructions.md`, Modul 06) + verpflichtender Review, nie ungeprüft mergen

## Wer hat das Urheberrecht bei generiertem Code?

- Rechtslage uneinheitlich und in Bewegung – grober Konsens: rein KI-generierter Output ohne menschliche schöpferische Leistung ist in vielen Rechtsordnungen nicht (allein) urheberrechtsfähig
- Praktische Konsequenz: Herkunft/Trainingsdaten der genutzten KI kennen, Lizenzbedingungen des Tools (z. B. GitHub Copilot Business/Enterprise Code-Referencing-Filter) beachten
- Bei Zweifeln: Rechtsabteilung einbeziehen, nicht selbst auslegen

## Wer haftet bei fehlerhaftem oder schadhaftem Code?

- KI-Anbieter haftet in der Regel nicht für Schäden durch generierten Code (siehe AGB/Lizenzbedingungen)
- Verantwortung bleibt bei der Person/Organisation, die den Code committed und freigibt
- Merksatz: **KI schlägt vor, der Mensch verantwortet.**

## Privacy-by-design: Datenschutz einhalten

- Keine echten Kunden-/Personendaten in Prompts, Screenshots oder Testdaten verwenden
- Prüfen, ob der genutzte Copilot-Plan Prompt-/Code-Daten zu Trainingszwecken speichert (Business/Enterprise i. d. R. opt-out by default)
- Bei MCP-Servern (Modul 13) besonders vorsichtig sein: externe Server sehen ggf. Repo-Inhalte – nur vertrauenswürdige Server einbinden
