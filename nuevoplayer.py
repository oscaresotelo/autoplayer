import os
import streamlit as st
import base64

def autoplay_audio(file_path: str, prev_audio=None, next_audio=None):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <div style="width: 100%; background-color: #f0f0f0; padding: 10px; border-radius: 5px; margin-bottom: 10px;">
                <audio id="audioPlayer" controls autoplay="true">
                    <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
                </audio>
                <div style="display: flex; justify-content: space-between; margin-top: 5px;">
                    <button {'disabled' if prev_audio is None else ''} onclick="changeAudio('{prev_audio}')">Anterior</button>
                    <button {'disabled' if next_audio is None else ''} onclick="changeAudio('{next_audio}')">Siguiente</button>
                </div>
            </div>
            <script>
                function changeAudio(audioSrc) {
                    var audio = document.getElementById('audioPlayer');
                    audio.src = audioSrc;
                    audio.play();
                }
            </script>
            """
        st.markdown(md, unsafe_allow_html=True)

downloads_folder = "downloads"
mp3_files = [f for f in os.listdir(downloads_folder) if f.endswith(".mp3")]
mp3_files_sorted = sorted(mp3_files)

st.title("Reproductor de Música")

# Utiliza una lista de botones para mostrar todos los archivos MP3
for i, mp3_file in enumerate(mp3_files_sorted):
    audio_path = os.path.join(downloads_folder, mp3_file)
    prev_audio = os.path.join(downloads_folder, mp3_files_sorted[i - 1]) if i > 0 else None
    next_audio = os.path.join(downloads_folder, mp3_files_sorted[i + 1]) if i < len(mp3_files_sorted) - 1 else None
    
    # Botón para reproducir el audio
    if st.button(f"{mp3_file}"):
        autoplay_audio(audio_path, prev_audio, next_audio)
