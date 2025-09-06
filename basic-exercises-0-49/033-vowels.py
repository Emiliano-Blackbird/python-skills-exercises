letra = input("Introduce una letra: ")

if letra.lower() in "aeiou":
    print("Es una vocal")
else:
    print("No es una vocal")

# Segunda forma
caracter = input("Introduce un caracter: ")
vocales = ["a", "e", "i", "o", "u"]
if caracter.lower() in vocales:
    print("Es una vocal")
else:
    print("No es una vocal")
