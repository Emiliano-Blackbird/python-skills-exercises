def contar_vocales(palabra):
    """Cuenta el número de vocales en una palabra dada.

    Args:
        palabra (str): La palabra en la que se contarán las vocales.

    Returns:
        int: El número de vocales en la palabra.
    """
    vocales = 'aeiou'
    return sum(1 for letra in palabra if letra.lower() in vocales)


palabras = ['Pikachu', 'Mewtwo', 'Charizard', 'Scizor', 'Gengar']
conteo_vocales = list(map(contar_vocales, palabras))

print(f"Palabras y conteo de vocales: {list(zip(palabras, conteo_vocales))}")
