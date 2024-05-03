import streamlit as st
import os

# Carpeta donde se encuentran los archivos MP3
mp3_folder = 'downloads'
mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith('.mp3')]

# Lista de archivos MP3
st.header("Lista de archivos MP3:")
selected_file = st.selectbox("Seleccionar archivo MP3:", mp3_files)

# Obtener la URL del archivo seleccionado
if selected_file:
    audio_path = os.path.join(mp3_folder, selected_file)
    audio_url = f"/{audio_path}"

    # Cargar código JavaScript para controlar la reproducción automática del audio
    js_code = f"""
    <script>
    var audioElement = new Audio("{audio_url}");
    audioElement.autoplay = true;
    audioElement.load();
    </script>
    """

    # Mostrar el reproductor de audio
    st.markdown(js_code, unsafe_allow_html=True)
