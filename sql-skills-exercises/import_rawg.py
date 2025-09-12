# import_rawg.py
import os
import requests
import mysql.connector
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()  # lee el archivo .env

API_KEY = os.getenv("API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# Conectar a MySQL
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USER,
    password=DB_PASS,
    database=DB_NAME
)
cursor = conn.cursor()

# Crear tabla para PS4
cursor.execute("""
CREATE TABLE IF NOT EXISTS juegos_ps4 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(255),
    fecha_lanzamiento DATE,
    rating FLOAT,
    generos TEXT,
    plataformas TEXT
)
""")

# Descargar 500 juegos de PS4
for page in range(1, 26):  # 25 páginas x 20 juegos = 500
    url = f"https://api.rawg.io/api/games?key={API_KEY}&platforms=18&page_size=20&page={page}"
    response = requests.get(url)
    data = response.json()

    print(data)

    for game in data["results"]:
        nombre = game.get("name")
        fecha = game.get("released", None)
        rating = game.get("rating", None)
        generos = ", ".join([g["name"] for g in game.get("genres", [])])
        plataformas = ", ".join([p["platform"]["name"] for p in game.get("platforms", [])])

        cursor.execute("""
            INSERT INTO juegos_ps4 (nombre, fecha_lanzamiento, rating, generos, plataformas)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, fecha, rating, generos, plataformas))

    print(f"✅ Página {page} importada")

# Guardar cambios y cerrar conexión
conn.commit()
cursor.close()
conn.close()

print("🎮 ¡Top 500 juegos de PS4 guardados en MySQL con éxito!")
