#JARVIS ARTIFICIAL INTELLIGENT
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import random



# Intializing the Microsoft speech API for text to speech conversion.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)

# creating function for Audio input
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# creating wishme function for AI to wish me as good morning, good afternoon and
#  good evening by self recognaising the time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>0 and hour <12:
        speak("Good Morning sir!")
    elif hour >=12 and hour<18:
        speak("Good Afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I am Jarvis.....How may I help you?")   

# creating the take command function for AI to take command from me so that 
# we can make any command which is programmed to it
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        
            
    except Exception as e:
        #print(e)
        print("Please say that again...")
        return "None"
    return query

         
if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        query = query.replace("jarvis","")

# This help to search the wikipedia query which is given to is as command
        if 'wikipedia' in query:
            speak('Searching wikipedia..')    
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query,sentences=1)
            print(results)
            speak("According to wikipedia ")
            speak(results)

# This help to search any thing in youtube it will open youtube and search your query
        elif 'youtube' in query:
            query = query.replace("youtube", "")
            speak("searching sir.." + query)
            pywhatkit.playonyt(query)

# This help to search any thing in google it will open google and search your query
        elif 'open google' in query:
            speak("opening sir..")
            webbrowser.open("google.com")

# This help to paly the music randomly from your system as music list path is given to it
        elif 'music' in query:
            music_dir = "C:\\Users\\HP\Music\\All songs\\hindi songs"
            songs = os.listdir(music_dir)
            rand = random.randint(0, 100)
            #print(songs)
            os.startfile(os.path.join(music_dir, songs[rand]))

# It will help you to get a actual time, date, AI will tell you what the date is today.
        elif 'time' in query:
            strtime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"sir, the current time is {strtime}")
            print(strtime)

        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("Opening sir....Please wait for a momment!")
            os.startfile(codePath)

# It will help to indroduce jarvis whever someone tell jarvis introduce yourself it will introduce it.
        elif 'yourself' in query:
            speak("Hello sir, I am jarvis an special Artificial Intelligent.. which is created by my boss Pradeep Rauniyar.. and I am programmed to performed several task..sir tell me how may I help you?")

        elif 'google' in query:
            query = query.replace("google","")
            from googlesearch import search
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'exit' in query:
            speak("Okay sir..")
            break


