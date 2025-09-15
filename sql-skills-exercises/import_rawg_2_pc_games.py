"""
Este script obtiene TODOS los juegos de PC disponibles en RAWG
y los inserta en una base de datos MySQL en la tabla 'blackbird_games_pc_db'.

Requisitos previos:
- Archivo .env con API_KEY, DB_HOST, DB_USER, DB_PASS, DB_NAME.
- Tabla 'blackbird_games_pc_db' creada en tu base de datos con las columnas:
  id (INT AUTO_INCREMENT), nombre, plataformas, fecha_lanzamiento, rating, generos.
"""

import os
import requests
import mysql.connector
from dotenv import load_dotenv
from time import sleep

# Cargar variables de entorno (.env)
load_dotenv()

API_KEY = os.getenv("API_KEY")
DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")

# Conectar a la base de datos MySQL
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    cursor = conn.cursor()
    print("✅ Conectado a MySQL correctamente.")
except mysql.connector.Error as err:
    print(f"❌ Error al conectar a MySQL: {err}")
    exit(1)

# Configurar parámetros RAWG
PLATFORM_ID_PC = 4        # PC es plataforma ID=4 en RAWG
PAGE_SIZE = 40            # Máximo permitido por RAWG
MAX_PAGES = 300           # Ajusta según quieras (30x40=1200 juegos aprox.)


# Función para insertar un juego en la base de datos
def insertar_juego(nombre, plataformas, fecha_lanzamiento, rating, generos):
    """
    Inserta un juego en la tabla 'blackbird_games_pc_db'.
    """
    try:
        cursor.execute("""
            INSERT INTO games (nombre, plataformas, fecha_lanzamiento, rating, generos)
            VALUES (%s, %s, %s, %s, %s)
        """, (nombre, plataformas, fecha_lanzamiento, rating, generos))
    except mysql.connector.Error as err:
        print(f"❌ Error insertando juego '{nombre}': {err}")


# Bucle para recorrer todas las páginas y obtener los juegos de PC
for page in range(1, MAX_PAGES + 1):
    url = (
        f"https://api.rawg.io/api/games"
        f"?key={API_KEY}"
        f"&platforms={PLATFORM_ID_PC}"
        f"&page_size={PAGE_SIZE}"
        f"&page={page}"
    )
    print(f"📥 Descargando página {page}...")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"❌ Error al solicitar la API en la página {page}: {response.status_code}")
        break

    data = response.json()

    # Si no hay resultados, salir del bucle
    if "results" not in data or not data["results"]:
        print("⚠️ No hay más juegos disponibles.")
        break

    # Recorrer cada juego y guardarlo
    for game in data["results"]:
        nombre = game["name"]
        plataformas = ", ".join([p["platform"]["name"] for p in game.get("platforms", [])])
        fecha_lanzamiento = game.get("released")
        rating = game.get("rating")
        generos = ", ".join([g["name"] for g in game.get("genres", [])])

        insertar_juego(nombre, plataformas, fecha_lanzamiento, rating, generos)

    # Confirmar cambios después de cada página
    conn.commit()
    print(f"✅ Página {page} insertada correctamente.")
    sleep(1)  # Pausa ligera para no saturar la API

# 6️⃣ Cerrar conexión
cursor.close()
conn.close()
print("🎉 Todos los juegos de PC han sido importados correctamente.")
