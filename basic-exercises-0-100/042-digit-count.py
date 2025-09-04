numero = int(input("Ingresa un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print("La cantidad de dígitos en el número es:", cantidad_digitos)

# Otra forma de hacerlo
numero2 = int(input("Ingresa otro número entero: "))
contador = 0
while numero2 != 0:
    numero2 //= 10
    contador += 1
print("La cantidad de dígitos en el número es:", contador)
