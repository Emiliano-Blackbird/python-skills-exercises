# Cortar el ciclo con break

numero = int(input("Ingrese un número: "))
while True:  # Ciclo infinito
    print(f"El número es: {numero}.")
    numero += 1
    if numero > 10:  # Condición para salir del ciclo
        break  # Salir del ciclo
print("Fin del ciclo.")
