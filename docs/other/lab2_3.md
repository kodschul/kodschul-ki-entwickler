# Lab 2.3. Refactoring und Optimierung mit KI-Unterstützung

```python
# Ursprünglicher Code
def quadrate_liste(liste):
    result = []
    for i in liste:
        result.append(i * i)
    return result

# Refaktorisierter Code (mit List Comprehension)
def quadrate_liste_optimiert(liste):
    """Gibt eine Liste mit den Quadraten der Elemente zurück."""
    return [i * i for i in liste]
```
