#SOLTI ARTIFICIAL INTELLIGENT
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pywhatkit
import random
import smtplib
import time
import geocoder




# Intializing the Microsoft speech API for text to speech conversion.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
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
        speak("Good Evening sir!..")
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



#Generating the live location...
def get_current_location():
    g = geocoder.ip('me')
    return g.latlng


# Generating the Diet chart 
def generate_diet_chart(heart_rate, step_count):
    if heart_rate > 100 and step_count < 5000:
        return "Diet Chart:\n- Increase intake of fruits and vegetables.\n- Reduce consumption of processed foods.\n- Drink plenty of water."

    if heart_rate <= 100 and step_count >= 5000:
        return "Diet Chart:\n- Focus on a balanced diet with lean proteins, whole grains, and healthy fats.\n- Include a variety of fruits and vegetables.\n- Stay hydrated and limit sugary drinks."

    if heart_rate > 100 and step_count >= 5000:
        return "Diet Chart:\n- Reduce intake of sugary and processed foods.\n- Increase consumption of lean proteins, whole grains, fruits, and vegetables.\n- Incorporate regular exercise into your routine.\n- Stay hydrated with water."

    return "No specific diet recommendations based on the provided heart rate and step count."



#for sending email in emergency situation and location..
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your_email_id', 'email_password')
    server.sendmail('your_email_id', to, content)
    server.close()





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


#This will change the voice of the AI
        elif 'activate' in query:
            speak("Ok sir.....Activating friday....done")
            engine.setProperty('voice', voices[1].id)
            speak("Hello sir.....Sir I am friday how may I help you....")

        elif 'return' in query:
            speak("Ok sir.....Activating jarvis back again....Activation done")
            engine.setProperty('voice', voices[0].id)
            speak("Hello sir.....Sir I am return back... how can I help you....")

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
            # music_dir = "C:\\Users\\HP\Music\\All songs\\hindi songs"
            music_dir = "C:\\Users\\PRADEEP\\Music\\Playlists\\songs"
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



# It will help to indroduce solti whever someone tell solti introduce yourself it will introduce it.
        elif 'yourself' in query:
            speak("Hello sir, I am solti an special Artificial Intelligence... and I am programmed to performed several task..sir tell me how may I help you?")



# This will tell the purpose of solti...
        elif 'boss' in query:
            speak('Mr. Pradeep Rauniyar is my Boss......He created and designed me for his self purpose assistant...you can read about him on google....')
            from googlesearch import search
            pquery = "Pradeep Rauniyar"
            for url in search(pquery, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % pquery)





# This funcion will detect the accident and perform the wakeup alarm, and fail to wakeup for sometime then send email...to emergency services...
        
        elif 'boom' in query:
            # try:
            #     speak("Sir, Please wake up..., wake up.. wake up... Are you ok sir...., Sir please response..wake up sir....Sir please response.. are you ok sir.... Sir Please wakeup...I am going to send an email to emergency services with current location.... in 10......9......8......7......6......5.....4.....3......2......1")

            #     speak("Email and Location send successfully...")
            #     print("")

            #     location = get_current_location()
            #     content = "Help Help it's an Emergency....My current location is.."
            #     print(content)
            #     print(location)

            # except Exception as e:
            #     print(e)
            #     speak("Sorry unable to send the email..")  
            
            try:
                location = get_current_location()
                content = f"Help Help it's an Emergency....My current location is..{location}"
                to = "other_emai_id@gmail.com"    
                sendEmail(to, content)
                print("Email has been sent")
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry unable to send the email..")  

            # Example usage
        elif 'diet' in query:
            speak("Enter your heart rate..")
            heart_rate = int(input("Enter your heart rate: "))
            speak("Enter your step count..")
            step_count = int(input("Enter your step count: "))

            speak("Your diet chart is...")
            diet_chart = generate_diet_chart(heart_rate, step_count)
            print(diet_chart)
            speak(diet_chart)


# for google search of any keyword....
        elif 'google' in query:
            query = query.replace("google","")
            from googlesearch import search
            for url in search(query, tld="co.in", num=1, stop = 1, pause = 2):
                webbrowser.open("https://google.com/search?q=%s" % query)

        elif 'exit' in query:
            speak("Okay sir..")
            break


