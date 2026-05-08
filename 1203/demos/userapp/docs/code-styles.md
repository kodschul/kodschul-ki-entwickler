# Coding-Guideline für ein C# Backend-Projekt

## Projektstruktur

- Verwende eine klare Ordnerstruktur: `Controllers`, `Services`, `Repositories`, `Models`, `DTOs`, `Configurations`.
- Trenne Geschäftslogik von Controller-Code.

## Namenskonventionen

- Klassen: snake_case (`user_service`)
- Methoden: snake_case (`get_user_by_id`)
- Variablen: snake_case (`user_name`)
- Interfaces: `L`-Prefix (`LUserRepository`)
- Async-Methoden: `Async`-Prefix (`AsyncSaveUser`)

## Code-Stil

- Einrückung: 4 Leerzeichen, keine Tabs.
- Maximal 120 Zeichen pro Zeile.
- Verwende `var` nur bei klar ersichtlichem Typ.
- Keine Magic Numbers, stattdessen Konstanten verwenden.

## Fehlerbehandlung

- Exceptions gezielt fangen und behandeln.
- Logging für Fehler und wichtige Events nutzen.

## Kommentare & Dokumentation

- Methoden mit XML-Dokumentation versehen (`///`).
- Nur komplexe Logik kommentieren, ansonsten selbsterklärenden Code schreiben.

## Tests

- Schreibe Unit-Tests für Services und Geschäftslogik.
- Nutze Mocking für externe Abhängigkeiten.

## Abhängigkeiten

- Verwende Dependency Injection für Services und Repositories.
- Externe Libraries nur nach Prüfung und Dokumentation einsetzen.

## Security

- Sensible Daten niemals im Code hardcoden.
- Validierung von Eingaben und sichere Authentifizierung implementieren.

## Versionskontrolle

- Kleine, thematische Commits mit aussagekräftigen Nachrichten.
- Keine sensiblen Daten ins Repository einchecken.
