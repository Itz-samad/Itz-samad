from cgitb import text
from email.mime import audio
from re import search
import requests
from bs4 import BeautifulSoup
import pyttsx3
import datetime
import speech_recognition as sr 
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Greetings():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning Abdulsamad")
    elif hour>=12 and hour<4:
        speak("Good afternoon ABdulsamad")
    else:
        speak("Good Evening Abdulsamad")

    speak("I am your Assistant, Zky Bot")
    
def takeCommand():
    # takes my command from microphone and gives text
    r =sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print("user : ", query)
    except Exception as e:
        print(e)
        speak("Sorry Abdulsamad, can you repeat that again?")
        return "none"
    return query

WAKE = "hi"

if __name__ == "__main__":



    while True:
            Greetings()

            speak("How can i help you?")
            query = takeCommand().lower()
            if 'search in wikipedia' in query:
                speak("searching in wikipedia")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences = 2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                speak("youtube is opened")
            
            elif 'open google' in query:
                webbrowser.open("google.com")
                speak("google is opened")
            elif 'open gmail' in query:
                webbrowser.open("gmail.com")
                speak("gmail is opened")
            # elif 'play music' in query:
            #     music_dir = 'D:\\music'
            #     songs = os.listdir(music_dir)
            #     print(songs)
            #     os.startfile(os.path.join(music_dir, songs[0]))
            #      speak("music is being played") 
            elif 'time' in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")
            elif 'weather' in query:
                user_api = 'ad4631fdce7f16ab242950729d24bd69'
                speak("Please input the name of the city or country")
                location = input("Enter the citie's name: ")

                complete_weather_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api

                api_link = requests.get(complete_weather_api_link)
                api_data = api_link.json()

                if api_data['cod'] == '404':
                     speak("invalid city: {}, please check your cities name".format(location))
                else:
                     temp_city = ((api_data['main']['temp']) - 273.15)
                     weather_description = api_data['weather'][0]['description']
                     humidity = api_data['main']['humidity']
                     wind_speed = api_data['wind']['speed']
                     date_time = datetime.datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
                     speak("the weather stats for - {} || {}".format(location.upper(), date_time))
                     print("---------------------------------------------------------------------")
                     speak("The current temperature is {:.2f} degree Celsius".format(temp_city))
                     print("The current temperature is {:.2f} deg C".format(temp_city))
                     print("---------------------------------------------------------------------")
                     speak("The weather is a" +weather_description)
                     print("The weather is a" +weather_description)
                     print("---------------------------------------------------------------------")
                     speak("The current humidity is {} percentage" .format(humidity))
                     print("The current humidity is {} percentage" .format(humidity))
                     print("---------------------------------------------------------------------")
                     speak("The current wind speed is {} kmph".format(wind_speed))
                     print("The current wind speed is {} kmph".format(wind_speed))
                     print("---------------------------------------------------------------------")
            elif 'open unity' in query:
                codepath = "C:\\Users\\Smartboy\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(codepath)
            elif 'stop' in query:
                speak("see you soon smartboy")
                exit()
            else :
                if(query != "none"):
                    webbrowser.open(query)
      
