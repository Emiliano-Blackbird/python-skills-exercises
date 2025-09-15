# RAWG Video Games MySQL Project 🎮

## Descripción
Este proyecto es una **base de datos de videojuegos** obtenida desde la API de [RAWG.io](https://rawg.io/apidocs), diseñada para **practicar Python y MySQL**.  
Permite almacenar información de juegos como: nombre, plataformas, fecha de lanzamiento, rating y géneros.  
Ideal para realizar consultas, rankings y análisis de datos offline, sin depender de la API en tiempo real.

<img src="/sql-skills-exercises/preview-workbench.png" alt="preview">

## Características
1- Trae los **primeros 500 juegos de PS4** desde RAWG usando Python.  
2- Guarda los datos **directamente en MySQL Workbench** en una base de datos local.  
3- Permite realizar consultas de ejemplo:  
  - Top 10 juegos según rating  
  - Juegos por género  
  - Rankings de plataformas  


## Tecnologías
- **Python**: para consumir la API y guardar los datos en MySQL.  
- **MySQL Workbench**: para almacenar y consultar la base de datos.  
- **RAWG API**: fuente de datos real de videojuegos.  
- **Librerías Python**:  
  - `requests` → para consumir la API  
  - `mysql-connector-python` → para conectarse a MySQL  
  - `python-dotenv` → para manejar credenciales de forma segura


## Configuración

### 1. Crear la base de datos en MySQL:

```sql
CREATE DATABASE rawg_db;
USE rawg_db;
```

### 2. Crear archivo .env en la carpeta del proyecto raíz

```
API_KEY=tu_api_key
DB_HOST=localhost
DB_USER=tu_usuario
DB_PASS=tu_contraseña
DB_NAME=rawg_db
```

### 3. Instalar librerías Python:

```
pip install requests mysql-connector-python python-dotenv
```

### 4. Ejecutar script Python import_rawg.py para importar los datos desde RAWG a MySQL.


### 5. Consulta de ejemplo en MySQL

```
-- Ver primeros 10 juegos
SELECT * FROM juegos_ps4 LIMIT 10;

-- Top 10 según rating
SELECT nombre, rating
FROM juegos_ps4
ORDER BY rating DESC
LIMIT 10;

-- Contar juegos por género
SELECT generos, COUNT(*) AS cantidad
FROM juegos_ps4
GROUP BY generos
ORDER BY cantidad DESC;
```
