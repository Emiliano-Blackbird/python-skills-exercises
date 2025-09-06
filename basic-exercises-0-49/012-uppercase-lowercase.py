# Paso una cadena a mayúsculas y minúsculas
texto = "Hola, Mundo!"

print(f"Texto original: {texto}")
print(f"Texto en mayúsculas: {texto.upper()}")
print(f"Texto en minúsculas: {texto.lower()}")

# O también puedo usar el método swapcase()
print(f"Texto con mayúsculas y minúsculas intercambiadas: {texto.swapcase()}")

# Otra forma de hacerlo
texto2 = "PYTHON"
texto_min = texto2.lower()
print(f"Texto en minúsculas segunda forma: {texto_min}")
