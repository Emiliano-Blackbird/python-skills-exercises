# Función para escribir contenido en un archivo
def escribir_en_archivo(nombre_archivo, contenido):
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(contenido)


escribir_en_archivo('nuevo_archivo.txt', 'Este archivo fué creado con una función en el ejercicio 093 y su conmtenido fue escrito con la función del ejercicio 094.')
