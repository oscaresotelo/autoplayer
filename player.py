# import os
# import streamlit as st
# from pygame import mixer
# import eyed3

# hide_st_style = """
#             <style>
#             #MainMenu {visibility: hidden;}
#             footer {visibility: hidden;}
#             header {visibility: hidden;}
#                      .container {
#                 display: flex;
#             }
#             .logo-text {
#                 font-weight:700 !important;
#                 font-size:30px !important;
#                 color: black !important;
#                 padding-top: 50px !important;
#             }
#             .logo-img {
#                 float:right;
#             }
#             </style>
#             """
# st.markdown(hide_st_style, unsafe_allow_html=True)

# def local_css(file_name):
#         with open(file_name) as f:
#             st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
# local_css("estilos.css")
# st.image("BANDERA.jpg")
# st.markdown(f"<h1 style='text-align: center; color: black;'> LA GUARIDA DE OSCAR</h1>", unsafe_allow_html=True)


# tab1, tab2 = st.tabs(["Buscar Tu Musica", "Lista de Reproduccion"])
# # Ruta de la carpeta de descargas (ajústala según tu configuración)

# with tab2:

#     downloads_folder = "downloads"

#     # Obtener la lista de archivos mp3 en la carpeta de descargas
#     mp3_files = [f for f in os.listdir(downloads_folder) if f.endswith(".mp3")]

#     # Crear una lista de nombres de archivo para su visualización en el menú desplegable
#     audio_options = ["Seleccionar Cancion"] + mp3_files

#     # Streamlit UI
#     st.title("Reproductor de Musica")

#     # Menú desplegable para seleccionar el archivo de audio
#     selected_audio = st.selectbox("Selecciona la Cancion", audio_options)

    

# # Reproducción de audio seleccionado
#     if selected_audio != "Seleccionar Cancion":

#         audio_path = os.path.join(downloads_folder, selected_audio)
        
#         # Obtener la duración del archivo MP3
#         audio_info = eyed3.load(audio_path)
#         st.audio(audio_path, format="audio/mp3", start_time=0)
#         duration = audio_info.info.time_secs
#         st.write(f"Duración: {duration:.2f} segundos")
#         if st.button("Actualizar Lista"):
#             st.rerun()
        



# with tab1:
#     import streamlit as st
#     from youtube_search import YoutubeSearch
#     from pytube import YouTube

#     # Función para buscar videos en YouTube
#     def search_videos(query):
#         results = YoutubeSearch(query, max_results=20).to_dict()
#         return results

#     # Función para descargar el audio de un video en formato MP3
#     def download_audio(video_url):
#         yt = YouTube(video_url)
#         audio_stream = yt.streams.filter(only_audio=True).first()
#         audio_stream.download(output_path="downloads", filename=yt.title + ".mp3")

#     # Configuración de la aplicación Streamlit
#     st.title("Crea Tu lista de Musica")
#     query = st.text_input("Que queres escuchar:")

#     if query:
#         results = search_videos(query)
#         for result in results:
#             video_title = result["title"]
#             video_url = "https://www.youtube.com" + result["url_suffix"]
            
#             # Obtener la URL de la miniatura del video
#             yt = YouTube(video_url)
#             thumbnail_url = yt.thumbnail_url

#             # Mostrar el título y la imagen del video
#             st.write(f"**Título:** {video_title}")
#             st.image(thumbnail_url, caption="Miniatura del video", use_column_width=True)

#             if st.button(f"Agregar {video_title} a Tu Lista"):
#                 download_audio(video_url)
#                 st.success(f"¡{video_title} Agregado a Tu Lista!")

import os
import streamlit as st
from pygame import mixer
import eyed3

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
                     .container {
                display: flex;
            }
            .logo-text {
                font-weight:700 !important;
                font-size:30px !important;
                color: black !important;
                padding-top: 50px !important;
            }
            .logo-img {
                float:right;
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
local_css("estilos.css")
st.image("BANDERA.jpg")
st.markdown(f"<h1 style='text-align: center; color: black;'> LA GUARIDA DEL OSCAR</h1>", unsafe_allow_html=True)


tab1, tab2 = st.tabs(["Buscar Tu Musica", "Lista de Reproduccion"])

with tab2:
    downloads_folder = "downloads"
    mp3_files = [f for f in os.listdir(downloads_folder) if f.endswith(".mp3")]

    st.title("Reproductor de Musica")
    
    if st.button("Actualizar Lista"):
        st.rerun()
    # Utiliza una lista de botones para mostrar todos los archivos MP3
    for mp3_file in mp3_files:
        audio_path = os.path.join(downloads_folder, mp3_file)
        
        # Obtener la duración del archivo MP3
        audio_info = eyed3.load(audio_path)
        # duration = audio_info.info.time_secs
        
        # Botón para reproducir el audio
        if st.button(f"{mp3_file}"):
            st.audio(audio_path, format="audio/mp3", start_time=0)


with tab1:
    # (código para la pestaña de búsqueda de YouTube)
    import streamlit as st
    from youtube_search import YoutubeSearch
    from pytube import YouTube

    # Función para buscar videos en YouTube
    def search_videos(query):
        results = YoutubeSearch(query, max_results=20).to_dict()
        return results

    # Función para descargar el audio de un video en formato MP3
    def download_audio(video_url):
        yt = YouTube(video_url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        audio_stream.download(output_path="downloads", filename=yt.title + ".mp3")

    # Configuración de la aplicación Streamlit
    st.title("Crea Tu lista de Musica")
    query = st.text_input("Que queres escuchar:")
    with st.spinner("Buscando....."):

        if query:
            results = search_videos(query)
            for result in results:
                video_title = result["title"]
                video_url = "https://www.youtube.com" + result["url_suffix"]
                
                # Obtener la URL de la miniatura del video
                yt = YouTube(video_url)
                thumbnail_url = yt.thumbnail_url

                # Mostrar el título y la imagen del video
                st.write(f"**Título:** {video_title}")
                st.image(thumbnail_url, caption="Miniatura del video", use_column_width=True)
                
                if st.button(f"Agregar {video_title} a Tu Lista"):
                    download_audio(video_url)
                    st.success(f"¡{video_title} Agregado a Tu Lista!")