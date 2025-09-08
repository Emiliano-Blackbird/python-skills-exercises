def celsius_to_fahrenheit(celsius: float) -> float:
    """Convierte grados Celsius a Fahrenheit.

    Args:
        celsius (float): La temperatura en grados Celsius.

    Returns:
        float: La temperatura en grados Fahrenheit.
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convierte grados Fahrenheit a Celsius.

    Args:
        fahrenheit (float): La temperatura en grados Fahrenheit.

    Returns:
        float: La temperatura en grados Celsius.
    """
    return (fahrenheit - 32) * 5/9


def main():
    print("¿Qué conversión quieres hacer?")
    print("1 - Celsius a Fahrenheit")
    print("2 - Fahrenheit a Celsius")

    opcion = input("Ingresa 1 o 2: ").strip()

    if opcion == "1":
        celsius = input("Ingrese la temperatura en grados Celsius: ")
        try:
            celsius = float(celsius)
            print(f"{celsius}°C son {celsius_to_fahrenheit(celsius):.2f}°F")
        except ValueError:
            print("⚠️ Por favor, ingrese un número válido.")
    elif opcion == "2":
        fahrenheit = input("Ingrese la temperatura en grados Fahrenheit: ")
        try:
            fahrenheit = float(fahrenheit)
            print(f"{fahrenheit}°F son {fahrenheit_to_celsius(fahrenheit):.2f}°C")
        except ValueError:
            print("⚠️ Por favor, ingrese un número válido.")
    else:
        print("⚠️ Opción inválida. Por favor, ejecuta el programa de nuevo e ingresa 1 o 2.")


if __name__ == "__main__":
    main()
