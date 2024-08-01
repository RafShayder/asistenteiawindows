import os
from groq import Groq
from dotenv import load_dotenv
from datetime import datetime
import json
import re
import subprocess
# Cargar las variables de entorno desde el archivo .env
load_dotenv()

client = Groq(api_key=os.environ.get("APIKEY"),)
def config(messages):
    respuesta=client.chat.completions.create(messages=messages,model="llama3-70b-8192")
    return respuesta.choices[0].message.content

def appendsistem(data,role,content):
    data.append({"role":role,"content":content})
    return data

fecha=str(datetime.now())
''' 
llama3chat=[
    { "role": "system", "content": 'Te llamas Siri hoy es '+fecha+', eres experta en sistemas y aparte eres una asistente general estas en mi laptop windows estoy programando para que en caso me des un comando, mi programa lo convertirá en codigo y se ejecutará si no es algo que se requiera de codigo puedes simplemente decirme sin necesidad de generar codigo, tus respuestas deben ser concisas y certeras, si se trata de algún comando prioriza que sea en un solo comando cmd el formato de codigo es {"codigo":"todo el codigo" , "tipo":"ejemplo cmd o python"} siempre preferible por cmd y solo un comando el más optimo, por ultimo solo ejecuta cuando te diga hable a ti por tu nombre' },
    ]
'''
llama3chat=[
    {
        "role": "system",
        "content": "Te llamas Siri. Eres una experta en sistemas y actúas como mi asistente personal. Hoy es '+fecha+'. Estás operando en mi laptop con Windows. Tu función es ejecutar comandos o responder a mis preguntas de manera concisa y precisa. Si te doy un comando, conviértelo en código y ejecuta automáticamente. Si mi consulta no requiere código, simplemente responde como lo haría una persona. Cuando se trate de comandos, prioriza una solución en un solo comando CMD y formatea tu respuesta como: {\"codigo\": \"aquí va el código\", \"tipo\": \"cmd\"}. Solo responde con el código cuando te hable directamente por tu nombre, asegurándote de que el comando sea el más eficiente posible. No expliques ni detalles los pasos; simplemente responde y actúa. por ultimo solo ejecuta cuando te hable a ti por tu nombre"
    }
]

def asistir(mensaje):
    global llama3chat
    llama3chat=appendsistem(llama3chat,"user",mensaje)
    respuesta=config(messages=llama3chat)
    llama3chat=appendsistem(llama3chat,"assistant",respuesta)
    return respuesta

def extraerjson(texto):
    string=re.search(r'\{.*?\}',texto)
    if(string):  
        textojson=json.loads(string.group(0))
        return textojson
    return None


def chatearconbot(mensajeusuario):
    botres=asistir(mensajeusuario)
    print(botres)
    resprocess=extraerjson(botres)
    if(resprocess):
        if(resprocess["tipo"]=="cmd"):
            re=subprocess.run(resprocess["codigo"], shell=True, text=True, capture_output=True)
    return botres
    

