numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numero3 = int(input("Introduce el tercer número: "))

numero_mayor = max(numero1, numero2, numero3)
print(f"El número mayor es: {numero_mayor}")

# Otra forma de hacerlo sin usar max()
if numero1 > numero2 and numero1 > numero3:
    print(f"El número mayor es el primero: {numero1}")
elif numero2 > numero1 and numero2 > numero3:
    print(f"El número mayor es el segundo: {numero2}")
else:
    print(f"El número mayor es el tercero: {numero3}")
