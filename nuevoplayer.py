import streamlit as st
import os
import base64

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio controls autoplay="true">
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(
            md,
            unsafe_allow_html=True,
        )

# Carpeta donde se encuentran los archivos MP3
mp3_folder = 'downloads'
mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith('.mp3')]

# Lista de archivos MP3
st.header("Lista de archivos MP3:")
selected_file = st.selectbox("Seleccionar archivo MP3:", mp3_files)

# Obtener la URL del archivo seleccionado
if selected_file:
    audio_path = os.path.join(mp3_folder, selected_file)
    autoplay_audio(audio_path)
