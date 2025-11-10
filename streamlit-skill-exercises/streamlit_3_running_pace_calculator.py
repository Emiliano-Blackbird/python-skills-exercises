"""
Comparador de corredores por pace.
Ejecutar: streamlit run streamlit_3_running_pace_calculator.py
"""

import numpy as np
import pandas as pd
import streamlit as st


def generar_tiempos(pace_min_km, distancia_km):
    """
    Dado un pace (min/km) y una distancia (km),
    devuelve un array de distancias y otro de tiempos acumulados en minutos.
    """
    kms = np.arange(0, distancia_km + 0.1, 0.1)  # pasos de 100 metros
    tiempos = kms * pace_min_km  # tiempo total en minutos para cada punto
    return kms, tiempos


def format_tiempo(min_total):
    """
    Convierte minutos totales en formato hh:mm:ss.
    """
    segundos = int(min_total * 60)
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = segundos % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def main():
    st.title("Comparador de Running por Pace")
    st.markdown("Compara el tiempo estimado de dos corredores en una misma distancia.")

    st.subheader("Parámetros")

    distancia = st.number_input("Distancia (km)", min_value=1.0, max_value=120.0, value=10.0, step=1.0)

    col1, col2 = st.columns(2)

    with col1:
        pace1 = st.number_input("Pace corredor 1 (min/km)", min_value=2.0, max_value=15.0, value=5.0, step=0.1)

    with col2:
        pace2 = st.number_input("Pace corredor 2 (min/km)", min_value=2.0, max_value=15.0, value=6.0, step=0.1)

    kms1, tiempos1 = generar_tiempos(pace1, distancia)
    kms2, tiempos2 = generar_tiempos(pace2, distancia)

    tiempo_final_1 = tiempos1[-1]
    tiempo_final_2 = tiempos2[-1]

    st.subheader("Resultados")
    st.write(f"**Corredor 1:** {format_tiempo(tiempo_final_1)}")
    st.write(f"**Corredor 2:** {format_tiempo(tiempo_final_2)}")

    st.subheader("Curva de Progreso (Tiempo Acumulado)")
    df = pd.DataFrame({
        "Corredor 1 (min)": tiempos1,
        "Corredor 2 (min)": tiempos2
    }, index=pd.Index(np.round(kms1, 2), name="Kilómetros"))

    st.line_chart(df)


if __name__ == "__main__":
    main()
