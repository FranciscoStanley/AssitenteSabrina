import pyttsx3 # pip install pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('rate', 150) # velocidade 120 = lento

for indice, vozes in enumerate(voices): # listar vozes
    print(indice, vozes.name)

voz = 0
engine.setProperty('voice', voices[voz].id)

engine.say("Olá, meu nome é Sabrina. Sou sua assistente virtual!")
engine.say("Oque posso fazer por você ?")

engine.runAndWait()

engine.stop()