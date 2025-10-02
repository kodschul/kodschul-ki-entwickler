# Lösungen – Lab 5.2 Modelle trainieren & lokal einsetzen

1. **Pro‑und‑Kontra‑Tabelle:**

| Aspekt            | Cloud‑LLM                                               | Lokales Modell                             |
|-------------------|---------------------------------------------------------|--------------------------------------------|
| Datenschutz       | Daten werden an externen Dienst gesendet; Compliance‑Risiken | Daten verbleiben lokal; volle Kontrolle     |
| Kosten            | Abrechnung pro Anfrage / Token; keine eigene Hardware   | Einmalige Hardware‑Investition; keine laufenden API‑Kosten |
| Modellqualität    | Aktuellste und leistungsfähigste Modelle                | Möglicherweise kleinere / ältere Modelle      |
| Latenz            | Netzwerkabhängig; höhere Verzögerung                   | Antwort lokal; geringere Latenz             |
| Wartung           | Provider übernimmt Updates und Sicherheit               | Nutzer muss Modelle aktualisieren und warten |

2. **Ollama installieren und Abfrage:**

Installation (Linux/Mac):

```bash
# Download und Installation gemäß Anleitung
tar -xvf ollama-linux-amd64.tar.gz
sudo mv ollama /usr/local/bin/
ollama serve
```

Start des Modells und Abfrage:

```bash
# Terminal 1
ollama run mistral

# Terminal 2
curl http://localhost:11434/api/generate \
  -d '{"model": "mistral", "prompt": "Erkläre kurz den Unterschied zwischen Stack und Heap."}'
```

Die Antwort erläutert typischerweise, dass der Stack Speicher für lokale Variablen in Funktionsaufrufen verwendet, während der Heap dynamisch allozierten Speicher für Objekte bereitstellt.

3. **Code‑Modell nutzen:**

Starte ein Code‑spezialisiertes Modell:

```bash
ollama run codellama
curl http://localhost:11434/api/generate \
  -d '{"model": "codellama", "prompt": "Schreibe eine Python‑Funktion, die die Zahlen 1 bis 100 summiert."}'
```

Das Modell gibt eine Funktion wie:

```python
def sum_numbers():
    return sum(range(1, 101))
```

Code‑optimierte Modelle wie CodeLLaMA oder StarCoder wurden speziell auf Programmier‑Daten trainiert.  Dadurch liefern sie syntaktisch korrekten Code mit idiomatischen Konstruktionen und Kommentaren.  Allgemeine LLMs können Code generieren, aber spezialisierte Modelle sind konsistenter und beherrschen Programmiersprachen besser.
