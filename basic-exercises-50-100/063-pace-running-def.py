from typing import Literal


def calculate_pace(
    distance_meters: float,
    elapsed_seconds: float,
    unit: Literal["km", "mi"] = "km"
) -> float:
    """
    Calcula el pace (ritmo) de running en minutos por unidad (km o mi).

    El pace es el tiempo que tarda el corredor en completar 1km.
    Ejemplo: 5:00 min/km significa que tarda 5 minutos en recorrer 1 kilómetro.

    Args:
        distance_meters (float): Distancia recorrida en metros.
        elapsed_seconds (float): Tiempo total transcurrido en segundos.
        unit (Literal["km", "mi"], opcional): Unidad para el pace.
            - "km": pace expresado en min/km.
            - "mi": pace expresado en min/mi.
            Por defecto "km".

    Returns:
        float: Pace expresado en minutos por km o por mi.

    Raises:
        ValueError: Si los parámetros no son válidos (distancia o tiempo <= 0).
    """
    if distance_meters <= 0:
        raise ValueError("La distancia debe ser mayor que cero.")
    if elapsed_seconds <= 0:
        raise ValueError("El tiempo debe ser mayor que cero.")

    # Conversión de distancia según unidad
    if unit == "km":
        distance_unit = distance_meters / 1000
    elif unit == "mi":
        distance_unit = distance_meters / 1609.34
    else:
        raise ValueError("Unidad inválida. Usa 'km' o 'mi'.")

    # Pace = tiempo total / distancia recorrida
    pace_minutes = (elapsed_seconds / 60) / distance_unit
    return pace_minutes


def format_pace(pace: float) -> str:
    """
    Formatea el pace en el estilo mm:ss (minutos:segundos por km o mi).

    Args:
        pace (float): Pace en minutos (ej. 5.25 → 5 min 15 s).

    Returns:
        str: Pace formateado como "mm:ss".
    """
    minutes = int(pace)
    seconds = int(round((pace - minutes) * 60))
    # Ajuste en caso de redondeo a 60s
    if seconds == 60:
        minutes += 1
        seconds = 0
    return f"{minutes}:{seconds:02d}"


# Ejemplo de uso
if __name__ == "__main__":
    distance = 10000  # 10 km
    time = 3000       # 50 minutos = 3000 segundos

    pace = calculate_pace(distance, time, unit="km")
    print("Pace:", format_pace(pace), "min/km")
