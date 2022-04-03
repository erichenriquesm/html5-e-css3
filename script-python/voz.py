import pyttsx3
engine = pyttsx3.init()
while True:
    c = str(input('O quer que eu fale?: '))
    engine.say(c)
    engine.runAndWait()
