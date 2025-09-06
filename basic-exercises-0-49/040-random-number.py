import random

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (1-10): "))
    intentos += 1
    if intento == numero_secreto:
        adivinado = True
    else:
        print("Intenta de nuevo.")

print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
