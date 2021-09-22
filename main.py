import pyttsx3 as p
import speech_recognition  as sr
import selenium_web as sl
import YT_audio as yt
import tiempo as tt
import rasa as rs
import time



engine = p.init()
engine.setProperty('rate', 150)
engine.setProperty('voice', 'spanish')
engine.setProperty('volume', 3)

def speak(text):
    engine.say(text)
    engine.runAndWait()

r = sr.Recognizer()
r.energy_threshold=10000

text=""

speak('Hola, soy tu asistente de voz. Me llamo Cristina la fina. ¿Cómo estás?')
speak("Qué puedo hacer por ti?")
def escuchar():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,1.2) 
        print("Escuchando!")  
        audio = r.listen(source)
        

    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        text= r.recognize_google(audio,language='es')
        print(text)
        return text

    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
texto=escuchar()

while texto != 'finalizar':
    if texto != None:
        respuesta=rs.rasa(texto)
        if len(respuesta) == 0:
            speak("No tengo la información que me pides")
        else:
            speak(respuesta[0])
    texto=escuchar()

speak("adios, que tengas un buen día")
    
# if "cómo" and 'tú' in texto:
#     speak("Yo estoy bien, gracias por preguntar")
# elif "buscar" and "información" in texto:
#     speak("que quieres buscar")
#     texto2=escuchar()
#     speak("buscando informacion sobre "+ texto2+ " en wikipedia")
#     assis=sl.infow()
#     dato=assis.get_info(texto2)
#     speak(dato)
# elif "vídeo" or "YouTube" in texto:
#     speak("que video quieres buscar")
#     texto3=escuchar()
#     speak("buscando video sobre "+ texto3+ " en youtube")

#     video=yt.music()
#     video.play(texto3)

# elif "tiempo" in texto:
#     temp,desc = tt.temp()
#     speak("La temperatura en Madrid es de "+temp +"grados.")
#     speak("el día es "+ desc )

    
#     resp1='sí'
#     while ('no' not in resp1):
#         speak("¿quieres conocer el tiempo en otra ciudad?")
#         resp1=escuchar()
#         print("resp1 "+resp1)
#         if "no" in resp1:
#             speak("gracias por preguntar")
#         else:
#             speak("¿De qué ciudad quieres conocer el tiempo?")
#             resp2=escuchar()
#             temp,desc = tt.temp(resp2)
#             speak("La temperatura en "+resp2+ " es de "+temp +"grados.")
#             speak("el día es "+ desc )

        




