# It's just a text to speech function..
def saySomething(somethingToSay):
    engine.say(somethingToSay)
    engine.runAndWait()


while True:
    something = input("Something to say? ")
    print("Saying something with speakers..")
    saySomething(something)

from gtts import gTTS
import os


# It's just a text to speech function..
def saySomething(somethingToSay):
    myobj = gTTS(text=somethingToSay, lang="es", slow=False)
    myobj.save("somethingToSay.mp3")
    os.system("mpg321 somethingToSay.mp3")


while True:
    something = input("Something to say? ")
    print("Saying something with speakers..")
    saySomething(something)


import speech_recognition as sr


        def main():

            r = sr.Recognizer()

            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)

                audio = r.listen(source)

                try:

                    print(r.recognize_google(audio))

                except Exception as e:
                    print("Error :  " + str(e))


                with open("recorded.wav", "wb") as f:
                    f.write(audio.get_wav_data())


        if __name__ == "__main__":
            main()