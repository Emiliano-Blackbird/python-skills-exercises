class Persona:

    def __init__(self, nombre=None, edad=None):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        self._edad = nueva_edad

    def mostrar_detalles(self):
        print(self.__dict__)

    def es_mayor_de_edad(self):
        if self._edad >= 18:
            return True
        else:
            return False


persona1 = Persona("Alice", 30)
persona1.mostrar_detalles()
if persona1.es_mayor_de_edad():
    print(f"{persona1.nombre} es mayor de edad.")
else:
    print(f"{persona1.nombre} no es mayor de edad.")
