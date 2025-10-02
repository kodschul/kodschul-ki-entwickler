# Lab 4.3 – Coding‑Stile und Design‑Patterns etablieren

In diesem Lab wird gezeigt, wie LLM‑basierte Assistenten als *Coding Coach* eingesetzt werden können: Sie erkennen unleserlichen Code und schlagen Verbesserungen gemäß Team‑Standards vor.  Typische Stilrichtlinien umfassen Namenskonventionen (snake_case für Python, camelCase für JavaScript/TypeScript), konsequentes Einrücken, hilfreiche Kommentare und Docstrings.  Durch klare Prompts kann man das Modell anweisen, sich an diese Regeln zu halten【626807851092106†L164-L175】.

### Schlecht formatierter Python‑Code

Die Slides enthielten ein Beispiel für unformatierten Python‑Code:

```python
# unformatierter Code
def calc(a,b):return a*b
```

Mit einem Prompt wie

> „Formatiere folgenden Python‑Code gemäß PEP 8, verwende snake_case und füge einen Docstring hinzu: …“

wird der Code aufgeräumt, eingerückt und mit Beschreibung versehen.

### TypeScript‑Service mit Factory‑Pattern

Ein weiteres Beispiel demonstrierte, wie man den Stil und das Design‑Pattern per Prompt erzwingen kann.  Der Prompt lautete: „Schreibe eine TypeScript‑Klasse `UserService` mit camelCase‑Methoden, verwende das Factory‑Pattern und füge JSDoc‑Kommentare hinzu.“  Das resultierende Skript erzeugte eine Klasse mit Factory‑Methode und Kommentaren.

### Singleton in Java

Zur Verdeutlichung des Singleton‑Patterns wurde ein Java‑Beispiel gezeigt:

```java
public class Logger {
    private static Logger instance;
    private Logger() {}
    public static synchronized Logger getInstance() {
        if (instance == null) {
            instance = new Logger();
        }
        return instance;
    }
    public void log(String msg) {
        System.out.println(msg);
    }
}
```

Der Singleton stellt sicher, dass es genau eine Instanz der Klasse gibt und bietet einen globalen Zugriffspunkt【977489249547423†L8-L12】.  Die statische Methode `getInstance()` kümmert sich um die Lazy‑Initialisierung【977489249547423†L52-L59】.
