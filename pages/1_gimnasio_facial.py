import streamlit as st
import os

# ¡El icono "💪" que usará el botón de la portada!
st.set_page_config(page_title="Gimnasio Facial", page_icon="💪", layout="wide")

# --- ¡LA RUTA CORRECTA! ---
RUTA_BASE = "recursos/material_semana_1_Ale/gimnasia_facial" 

# --- ¡LA LISTA DE NOMBRES CORRECTA CON LA EXTENSIÓN CORRECTA (.jpg)! ---
# (Basada 100% en tu captura image_0f627c.png y tu confirmación)
ejercicios_imgs = [
    "1_empuja_y_sonrie.jpg",
    "2_saca_la_lengua.jpg",
    "3_masaje_cachetes.jpg",
    "4_inflar_cachete_un_lado.jpg",
    "5_haz_la_cara_de_pez.jpg",
    "6_inflar_ambos_cachetes.jpg",
    "7_lado_derecha_izquierda.jpg",
    "8_con_la_mano_cachetes_hacia_abajo.jpg",
    "9_.jpg",  # (El archivo que se llama "9_.jpg")
    "10_ambos_cachetes.jpg"
]

# --- Título simple con Emojis ---
st.info("💪 TAREA 1: GIMNASIO FACIAL 💪", icon="🔥") 

# --- Mostrar las Fotos como una Galería Grande ---
# (Tres fotos por fila)
columnas = st.columns(3) # 3 fotos por fila

for i, img_nombre in enumerate(ejercicios_imgs):
    # (i % 3) alterna entre 0, 1, 2 (columna 1, 2, 3)
    col_actual = columnas[i % 3] 
    
    with col_actual:
        try:
            ruta_completa = os.path.join(RUTA_BASE, img_nombre)
            
            # --- ¡LA CORRECCIÓN #2! ---
            # (¡Ya usa "use_container_width"!)
            st.image(ruta_completa, use_container_width=True)
            
            # (Título numérico que SÍ entiende)
            st.subheader(f"Ejercicio #{i+1}")
            st.markdown("---") # Separador

        except Exception as e:
            # (Error por si la cagamos en un nombre OTRA VEZ)
            st.error(f"¡Jimmy! No encuentro: {img_nombre}")
            st.warning(f"Error: {e}") # Imprime el error real

st.success("🎉 ¡Repite 3 veces! 🎉") # (¡Emoji de victoria!)