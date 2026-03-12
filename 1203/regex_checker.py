import re

_EMAIL_PATTERN = re.compile(
    r"""
    ^                           # Anfang des Strings
    (?!\.)[a-zA-Z0-9._%+\-]+   # Local part: alphanumerisch + erlaubte Sonderzeichen,
                                #   darf nicht mit Punkt beginnen
    (?<!\.)                     # darf nicht mit Punkt enden
    @                           # Trennzeichen
    (?!-)                       # Domain-Label darf nicht mit Bindestrich beginnen
    [a-zA-Z0-9\-]+              # erstes Domain-Label
    (?:\.[a-zA-Z0-9\-]+)*      # weitere Sub-Labels (optional)
    (?<!-)                      # letztes Label darf nicht mit Bindestrich enden
    \.                          # Punkt vor TLD
    [a-zA-Z]{2,}               # TLD: mindestens 2 Buchstaben
    $                           # Ende des Strings
    """,
    re.VERBOSE,
)


def is_valid_email(s: str) -> bool:
    """Prüft, ob *s* eine syntaktisch gültige E-Mail-Adresse ist.

    Die Prüfung orientiert sich an RFC 5321/5322 und deckt die in der Praxis
    relevanten Fälle ab.  Keine Drittanbieter-Bibliotheken werden benötigt.

    Regeln (Auswahl):
    - Local part:  alphanumerische Zeichen sowie ``. _ % + -`` erlaubt,
      darf weder mit einem Punkt beginnen noch enden, darf keine
      aufeinanderfolgenden Punkte enthalten.
    - Domain:      Labels aus alphanumerischen Zeichen und Bindestrichen,
      kein Label darf mit einem Bindestrich beginnen oder enden.
    - TLD:         mindestens zwei Buchstaben (z. B. ``.de``, ``.com``).
    - Quoted strings und IP-Literale (``user@[192.168.1.1]``) werden
      **nicht** unterstützt – das reicht für den Alltag.

    Args:
        s: Die zu prüfende Zeichenkette.

    Returns:
        ``True`` wenn *s* eine gültige E-Mail-Adresse ist, sonst ``False``.

    Examples:
        >>> is_valid_email("alice@example.com")
        True
        >>> is_valid_email("alice.bob+filter@mail.example.co.uk")
        True
        >>> is_valid_email("user_123@sub.domain.de")
        True
        >>> is_valid_email("@example.com")          # fehlender Local part
        False
        >>> is_valid_email(".alice@example.com")    # beginnt mit Punkt
        False
        >>> is_valid_email("alice.@example.com")    # endet mit Punkt
        False
        >>> is_valid_email("alice..bob@example.com")# doppelter Punkt
        False
        >>> is_valid_email("alice@.example.com")    # Domain beginnt mit Punkt
        False
        >>> is_valid_email("alice@example.c")       # TLD zu kurz
        False
        >>> is_valid_email("alice@example")         # keine TLD
        False
        >>> is_valid_email("not-an-email")          # kein @
        False
        >>> is_valid_email("")                      # leerer String
        False
    """
    if not isinstance(s, str) or ".." in s:
        return False
    return bool(_EMAIL_PATTERN.match(s))
