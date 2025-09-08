def tasa_desempleo(poblacion_activa: int, desempleados: int) -> float:
    """
    Calcula la tasa de desempleo.

    Args:
        poblacion_activa (int): Total de personas en la población activa.
        desempleados (int): Número de personas desempleadas.

    Returns:
        float: Tasa de desempleo como un porcentaje.

    Raises:
        ValueError: Si la población activa es cero o negativa.
    """
    if poblacion_activa <= 0:
        raise ValueError("La población activa debe ser mayor que cero.")

    tasa = (desempleados / poblacion_activa) * 100
    return tasa


# Ejemplo de uso
poblacion_activa = int(input("Ingrese la población activa: "))
desempleados = int(input("Ingrese el número de desempleados: "))

tasa = tasa_desempleo(poblacion_activa, desempleados)
print(f"La tasa de desempleo es del {tasa:.2f}%.")
