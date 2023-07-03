import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_whatsapp_message
import pyttsx3
import speech_recognition as sr
import time
from time import ctime
from datetime import datetime
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from random import choice
from utils import opening_text
from pprint import pprint
from tkinter import *
from PIL import ImageTk,Image


USERNAME='Manohar'
BOTNAME='FRIDAY'

print("It's me Friday")
r = sr.Recognizer()
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 190)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def greet_user():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")


def take_user_input(ask = False):
    
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        query=""
    try:
        query = r.recognize_google(audio,language='en-in')
        print('Recognizer voice :'+ query)
        speak(choice(opening_text))
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

class Widget:
    def __init__(self):
        root = Tk()
        root.title('Friday')
        root.geometry('1000x500')
        img = ImageTk.PhotoImage(Image.open('Friday_pic2.jpg'))
        panel = Label(root, image=img)
        panel.pack(side='right', fill='both', expand='no')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Friday', font=('Railways', 24,'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='black',fg='white')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'),bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10,'bold'), bg='yellow', fg='black', command=root.destroy).pack(fill='x', expand='no')
        root.mainloop()

    def clicked(self):
        print("Listening....")
        query = take_user_input().lower()
        if 'open notepad' in query:
            open_notepad()

        elif 'open discord' in query:
            open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            open_cmd()

        elif 'open camera' in query:
            open_camera()

        elif 'open calculator' in query:
            open_calculator()

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)

        elif 'youtube' in query or 'play me a song' in query:
            speak('What do you want to play on Youtube, sir?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'google' in query:
            speak('What do you want to search on Google, sir?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif 'what is the time' in query:
                speak("sir the time is:" + ctime())

        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            pprint(advice)

        elif 'news' in query:
            speak(f"I'm reading out the latest news headlines, sir")
            speak(get_latest_news())
            speak("For your convenience, I am printing it on the screen sir.")
            print(*get_latest_news(), sep='\n')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")

        elif 'exit' in query:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()

if __name__ == '__main__':
    greet_user()
    widget= Widget()
time.sleep(1)

    


        