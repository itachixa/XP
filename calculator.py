def add(a, b):
    """Additionne deux nombres."""
    return a + b

def subtract(a, b):
    """Soustrait b de a."""
    return a - b

def multiply(a, b):
    """Multiplie deux nombres."""
    return a * b

def divide(a, b):
    """Divise a par b."""
    if b == 0:
        raise ValueError("Division par zéro impossible.")
    return a / b
