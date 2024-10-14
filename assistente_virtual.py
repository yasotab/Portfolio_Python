import speech_recognition as sr
import webbrowser
import wikipedia
import pyttsx3

def takeCommand():
    """
    Captura a voz do usuário e retorna como texto.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            print("Recognizing...")
            Query = r.recognize_google(audio, language='pt-br')
            print("the command is printed=", Query)
            return Query
        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

def speak(audio):
    """
    Converte texto em voz.
    """
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(audio)
    engine.runAndWait()

def tellDay():
    """
    Informa o dia da semana.
    """
    day = datetime.datetime.today().weekday() + 1
    Day_dict = {1: 'Segunda', 2: 'Terça', 3: 'Quarta', 4: 'Quinta', 5: 'Sexta', 6: 'Sábado', 7: 'Domingo'}
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("O dia é " + day_of_the_week)

def tellTime():
    """
    Informa a hora atual.
    """
    time = str(datetime.datetime.now())
    print(time)
    hour = time[11:13]
    min = time[14:16]
    speak("A hora é " + hour + " horas e " + min + " minutos")

def Hello():
    """
    Saudação inicial do assistente.
    """
    speak("Olá, eu sou seu assistente de pesquisa. Diga como posso ajudá-lo.")

def Take_query():
    """
    Captura a voz do usuário e realiza a pesquisa.
    """
    Hello()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Pesquisando no Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("Segundo o Wikipedia...")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("Abrindo o YouTube...")
            webbrowser.open("youtube.com")
        elif "open google" in query:
            speak("Abrindo o Google...")
            webbrowser.open("google.com")
        elif "tell me the time" in query:
            tellTime()
        elif "tell me the day" in query:
            tellDay()
        elif "bye" in query:
            speak("Tchau! Até mais!")
            exit()
        else:
            speak("Não entendi. Pode repetir?")

if __name__ == "__main__":
    Take_query()