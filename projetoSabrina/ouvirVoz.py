import speech_recognition as sr  # pip install SpeechRecognition

rr = sr.Recognizer()

mic = sr.Microphone()

with mic as fonte:
    #4rr.adjust_for_ambiente_noise(fonte)
    print("Diga alguma")
    audio = rr.listen(fonte)
    print("Enviando para reconhecimento")
    try:
        text = rr.recognize_google(audio, language="pt-BR")
        print("Você disse: {}".format(text))
    except:
        print("Não entendi oque você disse")