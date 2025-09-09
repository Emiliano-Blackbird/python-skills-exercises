class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def es_mayor_de_edad(self):
        if self.edad >= 18:
            return True
        return False

    def descripcion(self):
        return f"{self.nombre} tiene {self.edad} años y su DNI es {self.dni}."


# Ejemplo de uso
persona1 = Persona("Alice", 30, "12345678A")
print(persona1.descripcion())
if persona1.es_mayor_de_edad():
    print(f"{persona1.nombre} es mayor de edad.")
else:
    print(f"{persona1.nombre} no es mayor de edad.")
