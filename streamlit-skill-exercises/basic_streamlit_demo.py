import streamlit as st

st.write("Slider Example")

x = st.slider("Select a value")  # 👈 this is a slider widget
st.write(x, "squared is", x * x)
