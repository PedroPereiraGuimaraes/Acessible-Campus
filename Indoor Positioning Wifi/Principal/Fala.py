import pyttsx3

def falar(frase):
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    engine.say(frase)
    engine.runAndWait()
