def tiempo_viaje():
    """
    Calcula el tiempo de viaje dado la distancia y la velocidad.

    Args:
        distancia (float): Distancia del viaje en kilómetros.
        velocidad (float): Velocidad en kilómetros por hora.

    Returns:
        float: Tiempo de viaje en horas.

    Raises:
        ValueError: Si la distancia o velocidad son menores o iguales a cero.
    """
    distancia = float(input("Ingrese la distancia del viaje en kilómetros: "))
    velocidad = float(input("Ingrese la velocidad en kilómetros por hora: "))

    if distancia <= 0:
        raise ValueError("La distancia debe ser mayor que cero.")
    if velocidad <= 0:
        raise ValueError("La velocidad debe ser mayor que cero.")

    tiempo = distancia / velocidad
    return tiempo


resultado = tiempo_viaje()
print(f"El tiempo de viaje es de {resultado:.2f} horas.")
