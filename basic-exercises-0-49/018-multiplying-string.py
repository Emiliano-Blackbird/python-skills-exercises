# Multiplicar una cadena
shop = "Zapatos"
resultado = shop * 3

# Con espacios
print((shop + " ") * 3)

# Con guiones
print(" - ".join([shop] * 3))

# Con enumeración
for i in range(1, 4):
    print(f"{i}. {shop}")
