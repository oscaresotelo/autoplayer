import streamlit as st
import os

# Carpeta donde se encuentran los archivos MP3
mp3_folder = 'downloads'
mp3_files = [os.path.join(mp3_folder, f) for f in os.listdir(mp3_folder) if f.endswith('.mp3')]

st.header("Lista de archivos MP3:")
for mp3_file in mp3_files:
    st.audio(mp3_file, format='audio/mp3')

autoplay_script = """
<script>
document.addEventListener("DOMContentLoaded", function(event) {
    var audioElements = document.getElementsByTagName("audio");
    if (audioElements.length > 0) {
        audioElements[0].autoplay = true;
    }
});
</script>
"""

# Mostrar el código JavaScript en la página
st.markdown(autoplay_script, unsafe_allow_html=True)
