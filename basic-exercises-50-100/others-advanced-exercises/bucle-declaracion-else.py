for i in range(5):
    print(f"El valor de i es: {i}")
    break
else:
    print("El ciclo for terminó sin interrupciones.")

# Y con while el funcionamiento es similar

numero = int(input("Ingrese un número: "))
while numero < 5:
    print(f"El número es: {numero}.")
    numero += 1
else:
    print("El ciclo while terminó sin interrupciones.")
