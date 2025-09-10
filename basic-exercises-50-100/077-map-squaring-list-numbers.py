def cuadrado(n):
    return n**2


numeros = [1, 2, 3, 4, 5, 6, 7, 8]
numeros_cuadrados = list(map(cuadrado, numeros))

print(numeros)
print(numeros_cuadrados)
