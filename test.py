import streamlit as st
import speech_recognition as sr

def main():
    st.title("Transcripción de Audio a Texto")

    # Cargar archivo MP3
    uploaded_file = st.file_uploader("Cargar archivo MP3", type=["mp3"])

    if uploaded_file:
        # Crear un objeto de reconocimiento de voz
        recognizer = sr.Recognizer()

        # Leer el contenido del archivo MP3
        audio = sr.AudioFile(uploaded_file)
        with audio as source:
            audio_data = recognizer.record(source)

        # Realizar la transcripción
        try:
            text = recognizer.recognize_google(audio_data, language="es-ES")
            st.subheader("Texto transcribido:")
            st.write(text)
        except sr.UnknownValueError:
            st.write("No se pudo transcribir el audio. ¿El archivo contiene voz clara?")
        except sr.RequestError:
            st.write("Error al conectarse al servicio de reconocimiento de voz. Inténtalo más tarde.")

if __name__ == "__main__":
    main()
