import pyttsx3
import os
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib
import googlesearch
import bs4 as bs

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Ashish")

    elif hour>=12 and hour<18:
        speak("Good Evening Ashish")

    else:
        speak("Good Afternoon Ashish")

    speak("I am vision and this is my partner natasha. Please tell how may we help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pausethreshhold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query

def sendEmail(to, content):
    server =  smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anujashish16024@gmail.com', 'ay11rm11')
    server.sendmail('anujashish16024@gmail.com', to, content)
    server.close()

    
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'vision' in query:
            engine.setProperty('voice', voices[0].id)

            if 'in wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                query=query.replace('vision search', '')
                query=query.replace('in',"")
                Results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia ")
                print(Results)
                speak(Results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open my website' in query:
                webbrowser.open("ashtheaibot.000webhostapp.com")

            elif 'play music' in query:
                music_dir = 'D:\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time Sir is {strTime}")
                speak(f"The time Sir is {strTime}")

            elif 'open vs code' in query:
                codePath = "C:\\Users\\Ashish Yadav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open chrome' in query:
                charmPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(charmPath)

            elif 'play movie' in query:
                moviePath = "D:\\Chak De India 2007 Hindi  Www.MoviesBay.in  480p BluRay 450MB.mkv"
                os.startfile(moviePath)

            elif 'play fifa' in query:
                gamePath = "D:\\FIFA 2K18\\FIFA18.exe"
                os.startfile(gamePath)

            elif 'mail to daddy' in query:
                try:
                    speak('what should i say?')
                    content = takeCommand()
                    to = "asy732144@gmail.com"
                    sendEmail(to, content)
                    speak('email has been sent')
                except Exception as e:
                    print(e)
                    speak("Something went wrong, so sorry")

            elif 'mail to bhaiya' in query:
                try:
                    speak('what should i say?')
                    content = takeCommand()
                    to = "ashutoshy.and01@gmail.com"
                    sendEmail(to, content)
                    speak('email has been sent')
                except Exception as e:
                    print(e)
                    speak("Something went wrong, so sorry") 


            elif 'tell me about you' in query:
                speak('My name as you know is Vision. I am an android with the mind of JARVIS the personnal AI of tony stark, i had a vibranium body made from Ultron currently in posession of the U S government')

            elif 'quit' in query:
                speak("Goodbye Sir!!")
                exit()  

        elif 'natasha' in query:
            engine.setProperty('voice', voices[1].id)

            if 'in wikipedia' in query:
                speak("Searching Wikipedia...")
                query = query.replace("wikipedia", "")
                query=query.replace('natasha search', '')
                query=query.replace('in',"")
                Results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia ")
                print(Results)
                speak(Results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
            
            elif 'open google' in query:
                webbrowser.open("google.com")

            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")

            elif 'open my website' in query:
                speak("Uhhhh...I don't have the permission to access that site. Do you want me to call vision for this Sir?")
                webcom = takeCommand()
                if 'yes' in webcom:
                    engine.setProperty('voice', voices[0].id)
                    speak("I presume its your website that natasha needs help with!, here it is")
                    webbrowser.open('ashtheaibot.000webhostapp.com')
                    speak('Natasha I am done')
                    engine.setProperty('voice', voices[1].id)
                    speak('Thanks for the help')
 
            elif 'play music' in query:
                music_dir = 'D:\\Music'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                print(f"The time Sir is {strTime}")
                speak(f"The time Sir is {strTime}")

            elif 'open vs code' in query:
                codePath = "C:\\Users\\Ashish Yadav\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)

            elif 'open chrome' in query:
                charmPath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(charmPath)

            elif 'play movie' in query:
                moviePath = "D:\\Chak De India 2007 Hindi  Www.MoviesBay.in  480p BluRay 450MB.mkv"
                os.startfile(moviePath)

            elif 'play fifa' in query:
                gamePath = "D:\\FIFA 2K18\\FIFA18.exe"
                os.startfile(gamePath)

            elif 'mail to daddy' in query:
                try:
                    speak('what should i say?')
                    content = takeCommand()
                    to = "asy732144@gmail.com"
                    sendEmail(to, content)
                    speak('email has been sent')
                except Exception as e:
                    print(e)
                    speak("Something went wrong, so sorry")

            elif 'mail to bhaiya' in query:
                try:
                    speak('what should i say?')
                    content = takeCommand()
                    to = "ashutoshy.and01@gmail.com"
                    sendEmail(to, content)
                    speak('email has been sent')
                except Exception as e:
                    print(e)
                    speak("Something went wrong, so sorry")

            elif 'tell me about you' in query:
                speak('My name as you know is Natasha. I am a natural language user interface build by Aashish Yaaadav. Right i am only trained to do basic stuffs only.....but hey i evolve.')

            elif 'quit' in query:
                speak('Goodbye Sir!!')
                exit()    