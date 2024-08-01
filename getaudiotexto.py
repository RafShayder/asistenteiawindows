import speech_recognition as sr
from llama3 import chatearconbot
from voz import hablar
# Crear un objeto de reconocimiento
recognizer = sr.Recognizer()

def transcribe_audio():
    with sr.Microphone() as source:
        print("...")
        recognizer.adjust_for_ambient_noise(source)  # Ajustar el nivel de ruido
        print("🔈")

        while True:
            try:
                # Escuchar el audio continuamente
                audio = recognizer.listen(source)
                # Convertir el audio a texto en español
                text = recognizer.recognize_google(audio, language='es-ES')
                
                print("Texto reconocido: --" + text +"--")
                if(str(text).find("oye siri")>0):
                    print("°..")
                    voz=chatearconbot(text)
                    hablar(voz)
            except sr.UnknownValueError:
                # Error si no se puede entender el audio
                pass
            except sr.RequestError:
                # Error en la conexión al servicio de reconocimiento
                print("Error al conectar con el servicio de reconocimiento")
                break

if __name__ == "__main__":
    try:
        transcribe_audio()
    except KeyboardInterrupt:
        print("\n Hasta Luego.")
