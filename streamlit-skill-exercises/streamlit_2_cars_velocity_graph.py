"""
Aplicación Streamlit para comparar la aceleración de dos coches.
Ejecutar:
    streamlit run streamlit_2_cars_velocity_graph.py
"""

import re
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

from src.data_loader import load_cars_data


def perf_to_points(performance):
    """
    Convierte un dict de performance con claves tipo '0_100_kmh': tiempo_s
    en una lista de puntos (tiempo_s, velocidad_kmh), comenzando en (0, 0).

    Ejemplo:
    {"0_100_kmh": 3.2, "0_200_kmh": 9.1}
    -> [(0.0, 0.0), (3.2, 100.0), (9.1, 200.0)]
    """
    points = [(0.0, 0.0)]

    for key, value in performance.items():
        match = re.search(r"0_(\d+)_kmh", key)
        if not match:
            continue

        speed = float(match.group(1))
        time_s = float(value)
        points.append((time_s, speed))

    # Ordenamos por tiempo ascendente para la interpolación correcta
    points.sort(key=lambda x: x[0])
    return points


def speed_profile(performance, times):
    """
    Genera la velocidad en km/h a lo largo del tiempo con interpolación lineal.
    """
    points = perf_to_points(performance)
    time_points = np.array([p[0] for p in points])
    speed_points = np.array([p[1] for p in points])

    # Interpolación lineal. Para tiempos mayores al último punto,
    # mantiene la última velocidad conocida.
    speeds = np.interp(times, time_points, speed_points, left=0.0, right=speed_points[-1])
    return speeds


def main():
    cars = load_cars_data()
    names = list(cars.keys())

    st.title("Comparador de aceleración entre coches")
    st.markdown("Selecciona dos coches para comparar su de aceleración.")

    if not names:
        st.error("No se encontraron datos de coches.")
        return

    idx1 = st.slider("Coche 1 (índice)", 0, len(names) - 1, 0)
    idx2 = st.slider("Coche 2 (índice)", 0, len(names) - 1, min(1, len(names) - 1))

    car1 = names[idx1]
    car2 = names[idx2]

    col1, col2 = st.columns(2)

    # Mostrar información del coche 1
    with col1:
        st.markdown(f"**Coche 1:** {car1}")
        logo = cars[car1].get("logo")
        if logo and Path(logo).exists():
            st.image(logo, width=120)
        st.table(cars[car1].get("performance", {}))

    # Mostrar información del coche 2
    with col2:
        st.markdown(f"**Coche 2:** {car2}")
        logo = cars[car2].get("logo")
        if logo and Path(logo).exists():
            st.image(logo, width=120)
        st.table(cars[car2].get("performance", {}))

    # Obtener perfiles de velocidad
    perf1 = cars[car1].get("performance", {})
    perf2 = cars[car2].get("performance", {})

    max_time = max(
        perf_to_points(perf1)[-1][0] if perf_to_points(perf1) else 1.0,
        perf_to_points(perf2)[-1][0] if perf_to_points(perf2) else 1.0,
    )

    times = np.arange(0.0, max_time + 0.1, 0.1)
    speeds1 = speed_profile(perf1, times)
    speeds2 = speed_profile(perf2, times)

    df = pd.DataFrame({car1: speeds1, car2: speeds2}, index=pd.Index(times, name="Tiempo (s)"))

    st.subheader("Curva: Velocidad vs Tiempo")
    st.line_chart(df)


if __name__ == "__main__":
    main()
