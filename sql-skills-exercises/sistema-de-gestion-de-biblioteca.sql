# Sistema de gestión de biblioteca 

# CREACION DE TABLAS ************************************************************
CREATE DATABASE libros_bd;
USE libros_bd;
CREATE TABLE libros (
	id INT AUTO_INCREMENT PRIMARY KEY , # Identificador único ( clave primaria) 
    titulo VARCHAR(100) NOT NULL ,
    autor VARCHAR(100) NOT NULL,
    año INT CHECK (año > 1800) , # Validacion básica ( libros de años validos) 
    disponible BOOLEAN DEFAULT TRUE
);

CREATE TABLE  usuarios (
	id INT AUTO_INCREMENT PRIMARY KEY, 
    nombre VARCHAR(100) NOT NULL ,
    email VARCHAR(100) UNIQUE # único
);

#relacionar la tabla libros con usuarios (relaciones clase 5 ) 
CREATE TABLE prestamos(
	id INT AUTO_INCREMENT PRIMARY KEY,
    libro_id INT,
    usuario_id INT,
    fecha_prestamo DATE DEFAULT (CURRENT_DATE),
    fecha_devolucion DATE,
    FOREIGN KEY (libro_id) REFERENCES libros(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
# LIBROS (1) <- (N) PRESTAMOS (N) -> (1) USUARIOS
# POBLADO DE DATOS  ************************************************************

INSERT INTO libros (titulo, autor,año) VALUES 
('Cien años de soledad', 'Gabriel Garcia Marquéz', 1967),
('1984', 'George Orwell', 1949),
('El principito','Antonie de Saint Exupéry',1943 ),
('Harry Potter y la piedra filosofal','J.K. Rowling',1997 ),
('La sombra del viento','Carlos Ruiz Zafón',2001);

INSERT INTO usuarios (nombre,email)VALUES
('Ana Rodriguez','ana@gmail.com'),
('Marcelo Gorriti','marcelo@gmail.com'),
('Juan Caballero','juan@gmail.com');

INSERT INTO prestamos(libro_id, usuario_id) VALUES
(1,1), # Ana tiene el primer libro 
(3,2) ; # Marcelo tiene el principito usuario_idusuario_idusuario_idlibro_idlibro_idusuario_idfecha_prestamoid

UPDATE libros SET disponible = FALSE WHERE id IN (1,3);
#Explorar libros: SELECT * FROM libros;
#Explorar prestamos : SELECT * FROM prestamos;

# CONSULTAS  ************************************************************
#Libros disponibles 
 SELECT titulo, autor,año  FROM libros
 WHERE disponible = TRUE
 ORDER BY año DESC;

# Ver quien tiene que libro prestado (JOIN) 
SELECT 
	u.nombre AS usuario,
    l.titulo AS libro,
    p.fecha_prestamo AS "fecha de préstamo",
    DATEDIFF(CURRENT_DATE, p.fecha_prestamo) AS "días prestado"
FROM prestamos p 
JOIN libros l ON p.libro_id = l.id #Relación libro-prestamo
JOIN usuarios u ON p.usuario_id = u.id  #Relación usuario-prestamo
WHERE p.fecha_devolucion IS NULL;

# INDICES - OPTIMIZACION  ************************************************************
#INDEXAR libros por titulo  BUSQUEDA POR CATALOGO
CREATE INDEX idx_libros_titulo ON libros(titulo);

#INDEXAR prestamos por usuarios HISTORIAL DE PRESTAMOS DE UN USUARIO
CREATE INDEX idx_pr3estamos_usuario ON prestamos(usuario_id);
