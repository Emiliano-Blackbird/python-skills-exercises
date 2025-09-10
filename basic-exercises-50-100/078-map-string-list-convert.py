def convertir_entero(cadena):
    return int(cadena)


cadenas = ['1', '2', '3', '4', '5', '6', '7', '8']
enteros = list(map(convertir_entero, cadenas))  # Utilizo list para convertir el map a lista

print(cadenas)
print(enteros)
