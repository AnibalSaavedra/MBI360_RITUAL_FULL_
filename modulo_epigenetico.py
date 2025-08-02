
import streamlit as st

def ejecutar_test_epigenetico():
    st.header("🧬 Estado Epigenético Emocional")
    st.write("Evalúa qué tan activas están las memorias emocionales heredadas de tus líneas materna y paterna.")

    preguntas = [
        ("Me identifico con emociones que sé que también vivió mi madre.", "Indica herencia emocional materna."),
        ("Repito patrones de abandono o control como los de mi padre.", "Señala epigenética de línea paterna."),
        ("Siento emociones que no entiendo y vienen desde mi infancia.", "Puede ser memoria epigenética temprana."),
        ("Me cuesta liberar la culpa, como si no fuera solo mía.", "Frecuente en linajes con traumas familiares."),
        ("Siento lealtades inconscientes que me impiden avanzar.", "Puede reflejar transmisión transgeneracional.")
    ]

    respuestas = []
    for i, (pregunta, explicacion) in enumerate(preguntas):
        col1, col2 = st.columns([6, 1])
        with col1:
            resp = st.slider(f"{i+1}. {pregunta}", 1, 5, 3, key=f"epi_{i}")
        with col2:
            if st.button("❓", key=f"exp_epi_{i}"):
                st.info(explicacion)
        respuestas.append(resp)

    if st.button("Ver resultados", key="ver_epigenetico"):
        total = sum(respuestas)
        estado = "sin signos"
        if total >= 15 and total < 20:
            estado = "activo"
        elif total >= 20:
            estado = "muy activo"

        st.subheader("Resultado del Módulo Epigenético")
        st.success(f"Estado epigenético emocional: **{estado.upper()}** (puntaje: {total})")

        if estado == "muy activo":
            st.warning("🔺 Se recomienda un proceso de liberación epigenética con enfoque transgeneracional.")
        elif estado == "activo":
            st.info("🔹 Se evidencian memorias emocionales heredadas en curso.")
        else:
            st.success("✅ No se evidencian signos relevantes de epigenética emocional heredada.")
