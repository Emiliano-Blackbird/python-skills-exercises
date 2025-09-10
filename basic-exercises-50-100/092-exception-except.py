mi_lista = [1, 2, 3, 4, 5]

try:
    print(mi_lista[10])
except IndexError:
    print("Error: Índice fuera de rango.")
