class Libro:
    def __init__(self, titulo, autor, year):
        self.titulo = titulo
        self.autor = autor
        self.year = year

    def descripcion(self):
        return f"'{self.titulo}' de {self.autor} fue publicado en {self.year}."


# Ejemplo de uso
libro1 = Libro("The way of kings", "Brandon Sanderson", 2010)

print(libro1.descripcion())

# Ejemplo convertir a diccionario
libro2 = Libro("The final empire", "Brandon Sanderson", 2006)

print(libro2.__dict__)
