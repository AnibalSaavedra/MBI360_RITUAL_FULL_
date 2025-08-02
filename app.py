
import streamlit as st
from modulo_disociacion import ejecutar_test_disociacion
from modulo_epigenetico import ejecutar_test_epigenetico

st.set_page_config(page_title="MBI 360°", page_icon="🌀", layout="centered")

st.title("🌀 MBI 360° – Evaluación Integral del Ser")
st.markdown("""
Bienvenido al sistema **MBI 360°**, una herramienta única para conocer en profundidad tu estado emocional, epigenético, físico y energético.

**Marca:** RITUAL  
**Creador:** Aníbal Saavedra – Biotecnólogo MIB  
""")

st.subheader("Selecciona uno o varios módulos que deseas realizar:")

modulo_disociacion = st.checkbox("Test de disociación o trauma")
modulo_epigenetico = st.checkbox("Estado epigenético emocional (líneas materna/paterna)")

if not modulo_disociacion and not modulo_epigenetico:
    st.warning("Selecciona al menos un módulo para continuar.")
else:
    if modulo_disociacion:
        ejecutar_test_disociacion()

    if modulo_epigenetico:
        ejecutar_test_epigenetico()

st.markdown("---")
st.markdown("📱 ¿Necesitas ayuda o una consulta personalizada? [Contáctame por WhatsApp](https://wa.me/56967010107)")
