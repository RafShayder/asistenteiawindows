import pyttsx3

# Crear un objeto del motor de pyttsx3
engine = pyttsx3.init()
rate = engine.getProperty('rate')   # Obtener la tasa actual
engine.setProperty('rate', rate - 20)  # Disminuir la velocidad

# Establ-ecer el idioma y la voz a utilizar (en este caso, español)
voices = engine.getProperty('voices')
for voice in voices:
    if "spanish" in voice.languages:
        engine.setProperty('voice', voice.id)
        break

# Establecer el texto que se convertirá en voz

def hablar(texto):
    engine.say(texto)
    # Esperar a que termine de hablar
    engine.runAndWait()
