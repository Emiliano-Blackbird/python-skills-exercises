numero = int(input("Introduce un número: "))

if 0 < numero < 100:
    print("El número está entre 0 y 100")
elif numero in (0, 100):
    print("El número es 0 o 100")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es mayor que 100")


# numero = int(input("Introduce un número: "))

# if numero < 0:
#     print("El número es negativo")
# elif 0 <= numero <= 100:
#     if numero in (0, 100):
#         print("El número es 0 o 100")
#     else:
#         print("El número está entre 0 y 100")
# else:
#     print("El número es mayor que 100")
