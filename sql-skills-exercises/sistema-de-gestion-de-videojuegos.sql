-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS blackbird_games_pc_db;

-- Usar la base de datos
USE blackbird_games_pc_db;

-- Crear tabla 'juegos'
CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255) NOT NULL,
    plataformas TEXT,
    fecha_lanzamiento DATE,
    rating FLOAT,
    generos TEXT,
    jugado TINYINT(1) DEFAULT 0  -- 0 = No jugado, 1 = Jugado
);
-- Selecciona todos los juegos y todas sus columnas
USE blackbird_games_pc_db;

SELECT 
    id,
    nombre,
    plataformas,
    fecha_lanzamiento,
    rating,
    generos,
    jugado
FROM games
ORDER BY rating desc;  -- opcional: ordena alfabéticamente
