import re


def is_valid_email(s: str) -> bool:
    """
    Prüft, ob ein String eine gültige E-Mail-Adresse ist.

    Die Validierung orientiert sich an RFC 5322 und ist praktisch genug
    für den Einsatz in realen Anwendungen. Es werden keine Drittanbieter-
    Bibliotheken verwendet.

    Regeln:
    - Lokaler Teil (vor @): Buchstaben, Ziffern und . _ % + - erlaubt
    - Genau ein @-Zeichen
    - Domain: Buchstaben, Ziffern und Bindestriche erlaubt
    - Mindestens eine TLD (Top-Level-Domain) mit 2–63 Zeichen
    - Keine aufeinanderfolgenden Punkte im lokalen Teil oder der Domain
    - Kein führender oder abschließender Punkt im lokalen Teil

    Args:
        s: Der zu prüfende String.

    Returns:
        True, wenn der String eine gültige E-Mail-Adresse ist, sonst False.

    Examples:
        >>> is_valid_email("user@example.com")
        True
        >>> is_valid_email("user.name+tag@sub.domain.org")
        True
        >>> is_valid_email("user@localhost")
        False
        >>> is_valid_email("user@@example.com")
        False
        >>> is_valid_email(".user@example.com")
        False
        >>> is_valid_email("user@.example.com")
        False
        >>> is_valid_email("user@example..com")
        False
        >>> is_valid_email("plainaddress")
        False
        >>> is_valid_email("")
        False
        >>> is_valid_email("user@ex-ample.co.uk")
        True
    """
    pattern = re.compile(
        r"^(?!.*\.\.)[a-zA-Z0-9._%+\-]+(?<!\.)@(?!\.)[a-zA-Z0-9\-]+(\.[a-zA-Z0-9\-]+)*\.[a-zA-Z]{2,63}$")

    if not isinstance(s, str) or not s:
        return False

    local, _, domain = s.partition("@")

    # Kein führender oder abschließender Punkt im lokalen Teil
    if local.startswith(".") or local.endswith("."):
        return False

    return bool(pattern.match(s))
