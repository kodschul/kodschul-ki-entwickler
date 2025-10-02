# Lab 5.2 – Modelle trainieren & lokal einsetzen

Cloud‑basierte LLMs (z. B. GPT‑4) liefern hervorragende Ergebnisse, doch nicht jede Anwendung darf Daten an externe Dienste senden.  Lokale Modelle bieten die Möglichkeit, sensible Informationen zu schützen und offline zu arbeiten.  Die Slides erwähnen die Plattform **Ollama**, die verschiedene Modelle (LLaMA 2, Mistral, Gemma, Phi u.a.) im kompakten GGUF‑Format bereitstellt und ein lokales API unter `http://localhost:11434` startet.  Durch Befehle wie `ollama run llama2` wird das Modell gestartet und kann über eine REST‑API angesprochen werden.  Parameter wie Temperatur und Kontextfenster können angepasst werden.

## Installation und Nutzung

1. Lade den Installer von ollama.ai für dein Betriebssystem herunter und führe ihn aus.
2. Starte ein Modell mit `ollama run mistral` oder einem anderen Namen.  Beim ersten Aufruf lädt Ollama das Modell herunter und startet einen lokalen HTTP‑Server auf Port 11434.
3. Zum Testen kannst du den Endpoint `http://localhost:11434/api/generate` mit einem JSON‑Body aufrufen:

```bash
curl http://localhost:11434/api/generate \
  -d '{"model": "mistral", "prompt": "Erkläre kurz den Unterschied zwischen Stack und Heap."}'
```

### Vorteile und Nachteile

Lokale Modelle bedeuten volle Datenkontrolle und keine laufenden API‑Kosten, erfordern aber ausreichend Hardware (GPU/CPU und RAM) und müssen regelmäßig aktualisiert werden.  Cloud‑Modelle bieten höchste Qualität und ständige Updates, bringen aber Datenschutz‑Fragen und Kosten mit sich.
