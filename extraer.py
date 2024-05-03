# import speech_recognition as sr

# def extraer_texto_desde_mp3(archivo_mp3):
#     # Inicializar el reconocedor
#     reconocedor = sr.Recognizer()

#     # Abrir el archivo MP3
#     with sr.AudioFile(archivo_mp3) as fuente_audio:
#         # Escuchar el contenido del archivo
#         audio = reconocedor.record(fuente_audio)
        
#         try:
#             # Utilizar el reconocedor de voz para transcribir el audio a texto
#             texto = reconocedor.recognize_google(audio, language='es-ES') # Puedes ajustar el idioma según tus necesidades
#             return texto
#         except sr.UnknownValueError:
#             return "No se pudo entender el audio"
#         except sr.RequestError as e:
#             return f"Error en la solicitud al servicio de reconocimiento de voz; {e}"

# # Ruta al archivo MP3
# archivo_mp3 = "Crazy.mp3"

# # Extraer texto del archivo MP3
# texto_extraido = extraer_texto_desde_mp3(archivo_mp3)

# # Imprimir el texto extraído
# print(texto_extraido)
import streamlit as st
import speech_recognition as sr
from pydub import AudioSegment
import io

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


st.title("Traductor Universal.oscar inc.")

uploaded_file = st.file_uploader("Cargar archivo MP3", type=["mp3"])

if uploaded_file:
    st.audio(uploaded_file)

    audio_bytes = io.BytesIO(uploaded_file.read())
    audio_segment = AudioSegment.from_file(audio_bytes, format="mp3")

    wav_audio = io.BytesIO()
    audio_segment.export(wav_audio, format="wav")

    wav_audio.seek(0)

    r = sr.Recognizer()
    with sr.AudioFile(wav_audio) as source:
        audio_text = r.record(source)
    try:
        text = r.recognize_google(audio_text, language="es-ES")  # Cambia el idioma según sea necesario
        st.write("Texto transcrit:", text)
    except sr.UnknownValueError:
        st.write("No se pudo reconocer el audio")
    except sr.RequestError as e:
        st.write(f"Error en la solicitud al servicio de reconocimiento de voz; {e}")
