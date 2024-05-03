# import streamlit as st
# from youtube_search import YoutubeSearch
# from pytube import YouTube

# # Función para buscar videos en YouTube
# def search_videos(query):
#     results = YoutubeSearch(query, max_results=5).to_dict()
#     return results

# # Función para descargar el audio de un video en formato MP3
# def download_audio(video_url):
#     yt = YouTube(video_url)
#     audio_stream = yt.streams.filter(only_audio=True).first()
#     audio_stream.download(output_path="downloads", filename=yt.title + ".mp3")

# # Configuración de la aplicación Streamlit
# st.title("YouTube Video Downloader")
# query = st.text_input("Ingrese la palabra clave para buscar videos en YouTube:")

# if query:
#     results = search_videos(query)
#     for result in results:
#         video_title = result["title"]
#         video_url = "https://www.youtube.com" + result["url_suffix"]
#         st.write(f"**Título:** {video_title}")
#         st.write(f"**URL:** {video_url}")
#         if st.button(f"Descargar {video_title} en MP3"):
#             download_audio(video_url)
#             st.success(f"¡{video_title} descargado exitosamente en formato MP3!")

import streamlit as st
from pygame import mixer
import os
from pydub import AudioSegment

def play_mp3(file_path):
    audio = AudioSegment.from_mp3(file_path)
    st.write(f"Reproduciendo: {file_path}")
    mixer.init()
    mixer.music.load(audio.export(format="wav").get_wav_data())
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.quit()

def list_mp3_files(folder_path):
    mp3_files = [f for f in os.listdir(folder_path) if f.endswith('.mp3')]
    return mp3_files

def main():
    st.title("Reproductor de archivos MP3")

    # Obtener la ruta absoluta de la carpeta "downloads"
    folder_path = os.path.abspath("downloads")

    mp3_files = list_mp3_files(folder_path)

    if not mp3_files:
        st.warning("No se encontraron archivos MP3 en la carpeta 'downloads'.")
        return

    st.write("Archivos MP3 disponibles:")
    st.write(mp3_files)

    for mp3_file in mp3_files:
        file_path = os.path.join(folder_path, mp3_file)
        play_mp3(file_path)

    st.success("Reproducción completada.")

if __name__ == "__main__":
    main()
