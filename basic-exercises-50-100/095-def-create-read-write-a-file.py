# Función para crear, leer, escribir y modificar un archivo
class Archivo:

    def __init__(self):
        self.nombre_archivo = ""
        self.contenido = ""

    def set_nombre_archivo(self, nombre):
        self.nombre_archivo = nombre

    def set_contenido(self, contenido):
        self.contenido = contenido

    def crear_archivo(self):
        with open(self.nombre_archivo, 'w'):
            pass

    def escribir_archivo(self):
        with open(self.nombre_archivo, 'w') as archivo:
            archivo.write(self.contenido)

    def leer_archivo(self):
        with open(self.nombre_archivo, 'r') as archivo:
            informacion = archivo.read()
        return informacion


file = Archivo()
file.set_nombre_archivo("nuevo_archivo_segunda_parte.txt")
file.set_contenido("Este contenido se ha creado y escrito con la función del ejercicio 95.")
file.crear_archivo()
file.escribir_archivo()
print(file.leer_archivo())
