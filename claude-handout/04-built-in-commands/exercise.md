# Übung: Built-in Commands

**Zeit:** ca. 30 min | **Projekt:** `1205/todo-app/`

---

## Aufgabe 1 – CLAUDE.md automatisch generieren (10 min)

Benenne eine vorhandene `CLAUDE.md` testweise um und lasse sie neu generieren:

```
> /init
```

Vergleiche das Ergebnis mit der ursprünglichen, manuell geschriebenen Version aus Modul 03.

## Aufgabe 2 – Kosten im Blick behalten (10 min)

```
> /cost
```

Führe eine größere Aufgabe aus (z. B. "Erkläre die komplette Codebase"), dann erneut:

```
> /cost
> /compact
> /cost
```

Notiere den Unterschied im Tokenverbrauch vor/nach `/compact`.

## Aufgabe 3 – Permissions ansehen (10 min)

```
> /permissions
```

Welche Befehle sind aktuell erlaubt/gesperrt? Vergleiche mit `.claude/settings.local.json` (Modul 05).

---

## Zusammenfassung

- [ ] `/init` ausprobiert und Ergebnis bewertet
- [ ] `/cost` vor und nach `/compact` verglichen
- [ ] `/permissions` mit `settings.local.json` abgeglichen
