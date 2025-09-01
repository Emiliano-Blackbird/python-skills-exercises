# Welcome to Python Advanced

from colorama import Fore, Style, init
import time

# Inicializar colorama (para Windows/Linux)
init(autoreset=True)


def bienvenida():
    while True:
        nombre = input("Hola, ¿Cómo te llamas? ").strip()
        if nombre:  # Validamos que no esté vacío
            print(Fore.GREEN + f"\n¡Bienvenido a Python avanzado, {nombre}!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "❌ No puedes dejarlo vacío. Intenta de nuevo." + Style.RESET_ALL)

    # Un efecto con "animación"
    print("\nPreparando tu entorno de Python...")
    for i in range(5, 0, -1):
        print(Fore.CYAN + f"{i}..." + Style.RESET_ALL)
        time.sleep(1)

    print(Fore.MAGENTA + f" ¡Listo, entorno cargado correctamente {nombre}! A programar se ha dicho. ")


if __name__ == "__main__":
    bienvenida()
