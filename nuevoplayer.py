import streamlit as st
import os

# Carpeta donde se encuentran los archivos MP3
mp3_folder = 'downloads'
mp3_files = [f for f in os.listdir(mp3_folder) if f.endswith('.mp3')]

# Lista de archivos MP3
st.header("Lista de archivos MP3:")
selected_file = st.selectbox("Seleccionar archivo MP3:", mp3_files)

# Mostrar el reproductor de audio
if selected_file:
    audio_path = os.path.join(mp3_folder, selected_file)
    audio_file = open(audio_path, 'rb').read()
    st.audio(audio_file, format='audio/mp3', start_time=0)

    # Cargar código JavaScript para controlar la reproducción automática del audio
    js_code = f"""
    <script>
    document.addEventListener('DOMContentLoaded', function() {{
        var audioElement = document.querySelector('audio');
        audioElement.play();
    }});
    </script>
    """
    st.markdown(js_code, unsafe_allow_html=True)
