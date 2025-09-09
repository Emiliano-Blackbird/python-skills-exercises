class Coche:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def descripcion(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"


# Ejemplo de uso
coche1 = Coche("Ferrari", "488 GTB", 2019)
coche2 = Coche("Lamborghini", "Huracán", 2020)
print(coche1.descripcion())
print(coche2.descripcion())

# Convierto a diccionario
print(coche1.__dict__)
print(coche2.__dict__)


# Otra forma sin description
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def __str__(self):
        return f"Coche: {self.marca} {self.modelo}, Año: {self.año}"

    def __repr__(self):
        return f"Coche(marca='{self.marca}', modelo='{self.modelo}', año={self.año})"


# Ejemplo de uso
coche3 = Vehiculo("Porsche", "911", 2021)
coche4 = Vehiculo("Mercedes", "AMG GT", 2022)

print(coche3)   # Usa __str__
print(coche4)

print(coche3.__dict__)  # Diccionario interno
print(coche4.__dict__)
