"""
    Demo de interacción básica de un slider en Streamlit.
    Se utilizan buenas prácticas y diseño limpio.
"""
import streamlit as st
# A partir de Python 3.9 no es necesario import Dict si uso dict directamente


def multiplication_table(n: int, up_to: int = 10) -> list[dict[str, int]]:
    """Genera una tabla de multiplicar para un número dado.

    Parameters:
        n (int): Número base de la tabla.
        up_to (int): Límite hasta el cual se multiplica.
    Returns:
        list[dict[str, int]]: Una lista de diccionarios con claves:
            - "numero": multiplicador
            - "producto": resultado del producto
    """
    if n < 0:
        n = 0  # Validación buenas prácticas (con slider no es necesario)
    if up_to < 1:
        up_to = 1  # Validación buenas prácticas (con slider no es necesario)
    return [
        {
            "numero": f"{n} x {i} ---->",  # numero: i
            "producto": f"{n * i}"  # string para mejor visualización en tabla
        }
        for i in range(1, up_to + 1)
    ]


st.title("Tabla de multiplicar con slider")
st.write("Selecciona un número y el rango para ver su tabla de multiplicar.")

# value=5 valor por defecto al recargar, step=1 incrementos del slider en 1
x = st.slider("Número a calcular", min_value=0, max_value=10, value=5, step=1)
upto = st.slider("Multiplicador:", min_value=1, max_value=10, value=5, step=1)

# Subheader y tabla de multiplicar
st.subheader(f"Tabla del {x} (hasta {upto})")
st.table(multiplication_table(x, upto))
