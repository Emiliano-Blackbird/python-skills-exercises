def multiply_numbers(a: int, b: int) -> int:
    """Devuelve el producto de dos números enteros.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: Producto de a y b.
    """
    return a * b


def main():
    # Esta función maneja la interacción con el usuario.
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        resultado = multiply_numbers(num1, num2)
        print(f"El resultado de {num1} x {num2} es: {resultado}")
    except ValueError:
        print("⚠️ Error: Debes ingresar solo números enteros.")


if __name__ == "__main__":
    # Solo se ejecuta si corremos este archivo directamente.
    main()


# Version simple
def sumar(num1, num2):
    return num1 + num2


print(f"La suma de 5 y 3 es: {sumar(5, 3)}")  # Output: 8
