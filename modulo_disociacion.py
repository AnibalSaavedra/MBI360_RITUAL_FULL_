
import streamlit as st

def ejecutar_test_disociacion():
    st.header("🧠 Test de Disociación o Trauma")
    st.write("Responde del 1 (nada) al 5 (totalmente de acuerdo) según cómo te identificas con cada afirmación.")

    preguntas = [
        ("Siento que a veces no soy yo quien actúa, como si algo dentro de mí tomara el control.", "Cuando experimentas una sensación de desconexión de tus acciones."),
        ("Hay momentos donde me cuesta recordar lo que hice o dije.", "Señal de lagunas disociativas relacionadas a trauma."),
        ("Me siento como si observara mi vida desde afuera, como una película.", "Indicador común de disociación perceptual."),
        ("Tengo emociones intensas que aparecen sin razón aparente.", "Puede ser memoria emocional no integrada."),
        ("Siento que tengo varias partes dentro de mí que a veces se contradicen.", "Refleja fragmentación interna del yo.")
    ]

    respuestas = []
    for i, (pregunta, explicacion) in enumerate(preguntas):
        col1, col2 = st.columns([6, 1])
        with col1:
            resp = st.slider(f"{i+1}. {pregunta}", 1, 5, 3, key=f"dis_{i}")
        with col2:
            if st.button("❓", key=f"info_{i}"):
                st.info(explicacion)
        respuestas.append(resp)

    if st.button("Ver resultados", key="ver_disociacion"):
        total = sum(respuestas)
        intensidad = "baja"
        if total >= 15 and total < 20:
            intensidad = "moderada"
        elif total >= 20:
            intensidad = "alta"

        st.subheader("Resultado del Test")
        st.success(f"Nivel de disociación: **{intensidad.upper()}** (puntaje total: {total})")

        if intensidad == "alta":
            st.warning("🔺 Se recomienda iniciar un proceso terapéutico de integración emocional.")
        elif intensidad == "moderada":
            st.info("🔹 Observa tus patrones disociativos y trabaja en reconexión emocional.")
        else:
            st.success("✅ No se evidencian síntomas significativos de disociación.")
