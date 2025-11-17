import streamlit as st

st.set_page_config(page_title="Rehab de Ale", page_icon="🧠", layout="wide")

st.title("Tareas de Ale 🧠") # (Un título corto y simple)

st.markdown("---")

# --- BOTONERA VISUAL ---
# (Streamlit agarra el emoji del "page_icon" del archivo de la página)
# (Y el "label" es el texto GRANDE del botón)

st.page_link(
    "pages/1_gimnasio_facial.py", 
    label="1. GIMNASIO FACIAL",  # (Texto simple y numerado)
    icon="💪"                  # (¡El icono!)
)

# (Aquí pondremos los que siguen, la próxima semana)
# st.page_link(
#     "pages/2_fonemas_vocales.py", 
#     label="2. VOCALES (BOCAS)", 
#     icon="👄"
# )

# st.page_link(
#     "pages/3_gesticulaciones.py", 
#     label="3. CONSONANTES (BOCAS)", 
#     icon="👅"
# )


# --- Este CSS hace los botones GIGANTES ---
st.markdown("""
<style>
    [data-testid="page-link"] button {
        height: 150px; /* ¡Más alto! */
        width: 100%;
        font-size: 40px; /* ¡Más grande! */
        font-weight: bold;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)