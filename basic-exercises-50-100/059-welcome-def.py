def welcome_message(name: str, gender: str = None) -> None:
    """Muestra un mensaje de bienvenida personalizado.

    Args:
        name (str): El nombre del usuario.
        gender (str, opcional): Género del usuario. Puede ser 'male', 'female' o None.
    """
    if gender == "male":
        print(f"¡Bienvenido, caballero {name}!")
    elif gender == "female":
        print(f"¡Bienvenida, dama {name}!")
    else:
        print(f"¡Bienvenido/a {name}!")


name = input("Por favor, introduce tu nombre: ")
gender = input("¿Cuál es tu género? (male/female/otro): ").lower()

welcome_message(name, gender if gender in ["male", "female"] else None)
