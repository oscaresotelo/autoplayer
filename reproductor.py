import streamlit as st
import yt_dlp
import requests
from pydub import AudioSegment
import io

def buscar_videos(query):
    try:
        ydl = yt_dlp.YoutubeDL({'format': 'bestaudio'})
        search_results = ydl.extract_info(f"ytsearch:{query}", download=False)
        videos = search_results.get('entries', [])
        return videos
    except Exception as e:
        st.error(f"Error al buscar videos: {e}")
        return []

def reproducir_audio(video):
    try:
        audio_data = io.BytesIO()
        audio_stream_url = video['formats'][0]['url']
        audio_data.write(requests.get(audio_stream_url).content)
        audio_data.seek(0)
        audio = AudioSegment.from_file(audio_data, format="webm")
        return audio
    except Exception as e:
        st.error(f"Error al reproducir audio: {e}")
        return None

def main():
    st.title("Buscador de Videos de YouTube")

    # Entrada para ingresar palabras clave de búsqueda
    query = st.text_input("Ingrese palabras clave de búsqueda:")

    if st.button("Buscar"):
        if query:
            videos = buscar_videos(query)
            if videos:
                st.success(f"Se encontraron {len(videos)} videos.")
                for i, video in enumerate(videos):
                    st.write(f"**Video {i + 1}:** {video['title']}")
                    audio = reproducir_audio(video)
                    if audio:
                        st.audio(audio.export(format="mp3").read(), format="audio/mp3", start_time=0)
            else:
                st.warning("No se encontraron videos.")

if __name__ == "__main__":
    main()
