import streamlit as st
from pytube import Search
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio
import requests
from io import BytesIO

# Inicializar el estado de la sesión
if 'resultados' not in st.session_state:
    st.session_state.resultados = []

def reproducir_audio(url):
    try:
        video = Search(url).results[0]
        audio_url = video.streams.filter(only_audio=True).first().url

        # Descargar el audio utilizando requests
        response = requests.get(audio_url)
        audio = AudioSegment.from_file(BytesIO(response.content))

        # Reproducir el audio en streaming
        _play_with_simpleaudio(audio)

    except Exception as e:
        st.write(f"Error al reproducir el audio: {e}")

def buscar_videos_en_youtube(palabra_clave, max_resultados=5):
    try:
        # Crear un objeto de búsqueda
        search_query = Search(palabra_clave)
        
        # Obtener los primeros 'max_resultados' resultados de la búsqueda
        st.session_state.resultados = search_query.results[:max_resultados]

        # Mostrar los títulos y enlaces de los videos encontrados
        if st.session_state.resultados:
            for video in st.session_state.resultados:
                video_url = f"https://www.youtube.com/watch?v={video.video_id}"
                st.write(f"Título: {video.title}")
                st.write(f"URL: {video_url}")

                # Botón para reproducir el audio
                if st.button(f"Reproducir Audio de '{video.title}'", key=video_url):
                    reproducir_audio(video_url)
                    st.write("Reproduciendo audio...\n")
        else:
            st.write("No se encontraron resultados para la búsqueda.")

    except Exception as e:
        st.write(f"Ocurrió un error: {e}")

# Interfaz de usuario con Streamlit
st.title("Buscador de Videos en YouTube")
palabra_clave = st.text_input("Ingrese la palabra clave para buscar en YouTube:")
max_resultados = st.slider("Número máximo de resultados a mostrar", 1, 20, 5)

# Botón para realizar la búsqueda
if palabra_clave:
    buscar_videos_en_youtube(palabra_clave, max_resultados)
