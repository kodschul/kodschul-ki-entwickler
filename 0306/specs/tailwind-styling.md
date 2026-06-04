# Spec: Style Todo App with Tailwind CSS

## User Story

Als Nutzer möchte ich, dass die Todo-App mit Tailwind CSS gestylt ist, damit sie modern und übersichtlich aussieht und angenehm zu benutzen ist.

## Datenmodell-Änderungen

Keine – reine UI-Änderung, keine Daten-Logik wird verändert.

## UI-Anforderungen

- Modern purple DESIGN

- Tailwind CSS über CDN einbinden (kein Build-Schritt nötig)
- Zentriertes Layout mit max. Breite (`max-w-xl` o.ä.) und vertikalem Spacing
- Seiten-Header (`<h1>`) mit prominenter Schrift und Farbe
- Eingabeformular:
  - Text-Input, Priority-Select und Date-Input mit Tailwind-Klassen (Rahmen, Padding, Rounded)
  - Submit-Button in Primärfarbe (z. B. Blau) mit Hover-Effekt
- Todo-Liste:
  - Jedes Todo als Card mit Hintergrund und Shadow
  - Erledigte Todos mit durchgestrichenem Text und gedämpfter Farbe
  - Priority-Badge farbig je nach Stufe (rot = high, gelb = medium, grün = low)
  - „Done/Undo"- und „Delete"-Buttons mit eigenen Farben (Grün/Rot)
- Link zum Calculator ebenfalls gestylt

## Akzeptanzkriterien

1. Die Seite lädt Tailwind CSS ausschließlich per CDN-`<script>`-Tag – kein lokaler Build, kein npm.
2. Das Layout ist auf mobilen Bildschirmen (< 640 px) und Desktop gleichermaßen lesbar.
3. Erledigte Todos sind visuell klar als „done" erkennbar (Strikethrough + gedämpfte Farbe).
4. Priority-Labels erscheinen als farbige Badges (High = Rot, Medium = Gelb, Low = Grün).
5. Alle Buttons haben sichtbare Hover-Zustände und sind groß genug zum Tippen (min. 36 px Höhe).
