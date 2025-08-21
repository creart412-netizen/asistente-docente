import streamlit as st
import openai
import os # Necesario para algunas configuraciones si las usas, pero no directamente para st.secrets

# ================= CONFIGURACIÓN DE LA APLICACIÓN =================
# CLAVE DE API DE OPENAI (¡AHORA SE OBTIENE DE FORMA SEGURA CON st.secrets!)
# Para que esto funcione, necesitas tener un archivo .streamlit/secrets.toml en tu repositorio
# con la línea: openai_api_key = "tu_nueva_clave_de_api_aqui"
try:
    openai.api_key = st.secrets["openai_api_key"]
except AttributeError:
    st.error("Error: La clave de API de OpenAI no se encontró en st.secrets.")
    st.warning("Por favor, crea un archivo `.streamlit/secrets.toml` con `openai_api_key = \"tu_clave_aqui\"`.")
    st.stop() # Detener la ejecución si la clave no está configurada
except KeyError:
    st.error("Error: La clave 'openai_api_key' no se encontró en tu archivo `secrets.toml`.")
    st.warning("Asegúrate de que `secrets.toml` contenga `openai_api_key = \"tu_clave_aqui\"`.")
    st.stop() # Detener la ejecución si la clave no está configurada

# LÍNEA DE DEPURACIÓN - ESTO TE MOSTRARÁ LA CLAVE PARCIAL EN LA APLICACIÓN
# ¡ELIMINA ESTA LÍNEA ANTES DE SUBIR A GITHUB PARA DESPLIEGUE FINAL O DE USO PÚBLICO!
st.info(f"DEBUG: API Key cargada (parcial): {openai.api_key[:5]}...{openai.api_key[-5:]}")

# ... el resto de tu código app.py ...
