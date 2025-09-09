class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie
        self.nombre = nombre

    def hacer_sonido(self):
        if self.especie.lower() == "perro":
            return "Guau"
        elif self.especie.lower() == "gato":
            return "Miau"
        else:
            return "Sonido desconocido"


# Ejemplo de uso
perro_1 = Animal("Perro", "Rex")
gato_1 = Animal("Gato", "Michi")

print(f"{perro_1.nombre} dice: {perro_1.hacer_sonido()}")
print(f"{gato_1.nombre} dice: {gato_1.hacer_sonido()}")
