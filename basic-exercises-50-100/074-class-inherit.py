# Clase padre
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."


# Clase hija que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)  # reutilizamos el init de Persona.
        self.carrera = carrera          # agrego un atributo extra.

    def presentarse(self):  # Sobrescribimos el método
        return f"Hola, soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}."


# Clase hija que hereda de Persona
class Profesor(Persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)
        self.materia = materia

    def presentarse(self):
        return f"Buenas, soy el profe {self.nombre}, tengo {self.edad} años y enseño {self.materia}."


# Uso
p1 = Persona("Carlos", 40)
e1 = Estudiante("Ana", 20, "Ingeniería")
pr1 = Profesor("Luis", 50, "Matemáticas")

print(p1.presentarse())   # Hola, soy Carlos y tengo 40 años.
print(e1.presentarse())   # Hola, soy Ana, tengo 20 años y estudio Ingeniería.
print(pr1.presentarse())  # Buenas, soy el profe Luis, tengo 50 años y enseño Matemáticas.
