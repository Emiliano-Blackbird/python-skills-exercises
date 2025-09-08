def clasificar_sustancia(sustancia):
    """
    Clasifica una sustancia química como 'ácido', 'base' o 'neutra' según su pH.

    Parámetros:
    sustancia (dict): Un diccionario que contiene el nombre y el pH de la sustancia.
                      Ejemplo: {'nombre': 'Ácido clorhídrico', 'pH': 1.0}

    Retorna:
    str: La clasificación de la sustancia ('ácido', 'base' o 'neutra').
    """
    pH = sustancia.get('pH')  # Obtener el valor de pH del diccionario

    if pH is None:
        return "pH no especificado"

    if pH < 7:
        return 'ácido'
    elif pH > 7:
        return 'base'
    else:
        return 'neutra'


# Ejemplo de uso
sustancia1 = {'nombre': 'Ácido clorhídrico', 'pH': 1.0}
sustancia2 = {'nombre': 'Hidróxido de sodio', 'pH': 13.0}
sustancia3 = {'nombre': 'Agua pura', 'pH': 7.0}

print(f"La sustancia {sustancia1['nombre']} es {clasificar_sustancia(sustancia1)}.")
print(f"La sustancia {sustancia2['nombre']} es {clasificar_sustancia(sustancia2)}.")
print(f"La sustancia {sustancia3['nombre']} es {clasificar_sustancia(sustancia3)}.")
