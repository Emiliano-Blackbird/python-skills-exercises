def obtener_longitud(palabra):
    return len(palabra)


palabras = ['Pikachu', 'Mewtwo', 'Charizard', 'Scizor', 'Gengar']
longitudes = list(map(obtener_longitud, palabras))

print(f"Palabras y longitudes: {list(zip(palabras, longitudes))}")
