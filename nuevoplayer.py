import streamlit as st
import os

# Carpeta donde se encuentran los archivos MP3
mp3_folder = 'downloads'
mp3_files = [os.path.join(mp3_folder, f) for f in os.listdir(mp3_folder) if f.endswith('.mp3')]

# Lista de archivos MP3
st.header("Lista de archivos MP3:")
selected_file = st.selectbox("Seleccionar archivo MP3:", mp3_files)

# Mostrar el reproductor de audio
if selected_file:
    audio_element = st.audio(selected_file, format='audio/mp3', start_time=0)

# Cargar código JavaScript para controlar la reproducción y detención del audio
js_code = f"""
<script>
let audioElement = document.querySelector('audio');
let playButton = document.createElement('button');
let stopButton = document.createElement('button');

playButton.textContent = 'Play';
stopButton.textContent = 'Stop';

playButton.onclick = function() {{
    audioElement.play();
}};

stopButton.onclick = function() {{
    audioElement.pause();
    audioElement.currentTime = 0;
}};

document.body.appendChild(playButton);
document.body.appendChild(stopButton);
</script>
"""

# Mostrar los botones de reproducción y detención
if selected_file:
    st.markdown(js_code, unsafe_allow_html=True)
