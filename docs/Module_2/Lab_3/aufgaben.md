# Lab 3 – Refactoring und Optimierung (Aufgaben)

In diesem Lab trainieren Sie, bestehende Funktionen zu verbessern,
indem Sie sie effizienter, lesbarer oder sicherer gestalten. Nutzen
Sie Ihre Kenntnisse aus den Folien und eigene Erfahrungen.

1. **Rekursion vs. Iteration**\
   Die folgende rekursive Python‑Funktion berechnet die Fakultät:

   ```python
   def factorial(n):
       if n == 0:
           return 1
       else:
           return n * factorial(n - 1)
   ```

   a) Welche Probleme können auftreten, wenn `n` sehr groß wird?

   b) Schreiben Sie eine **iterative** Version dieser Funktion, die das
   Problem vermeidet. Dokumentieren Sie die Funktion mit einer
   Docstring.

2. **Code‑Duplikate entfernen**\
   Im folgenden JavaScript‑Code werden mehrere Nachrichten ausgegeben:

   ```javascript
   function showWelcomeMessage() {
       console.log("Willkommen!");
       console.log("Wir hoffen, Sie genießen den Kurs.");
       console.log("Bitte stellen Sie Fragen.");
   }

   function showGoodbyeMessage() {
       console.log("Auf Wiedersehen!");
       console.log("Wir hoffen, Sie genießen den Kurs.");
       console.log("Bitte stellen Sie Fragen.");
   }
   ```

   Refaktorieren Sie den Code so, dass der wiederholte Teil in einer
   Hilfsfunktion gekapselt wird. Dadurch vermeiden Sie
   Code‑Duplikate und verbessern die Wartbarkeit.

3. **Fehlerbehandlung und Ressourcenmanagement**\
   Die folgende Funktion liest eine Datei und gibt den Inhalt zurück:

   ```python
   def read_file(path):
       f = open(path, "r")
       data = f.read()
       f.close()
       return data
   ```

   a) Welche Probleme können auftreten, wenn diese Funktion mit einem
   nicht existierenden Pfad oder bei Lesefehlern aufgerufen wird?

   b) Verbessern Sie die Funktion, indem Sie einen Kontextmanager
   (`with`‑Anweisung) verwenden und Fehlerbehandlung integrieren.
