def even_or_odd(number: int) -> str:
    """Determina si un número es par o impar.

    Args:
        number (int): El número a evaluar.

    Returns:
        str: Un mensaje indicando si el número es par o impar.
    """
    if number % 2 == 0:
        return f"El número {number} es par."
    else:
        return f"El número {number} es impar."


# Ejemplo de uso
num = int(input("Introduce un número: "))
print(even_or_odd(num))
