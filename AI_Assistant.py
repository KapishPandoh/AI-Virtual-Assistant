# Import Modules

import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
from playsound import playsound
import random
import requests
import json
from PIL import Image
from PIL import ImageGrab
import pyautogui 
import smtplib
import psutil
import pyjokes


# Functions for API

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
voiceRate = 150
engine.setProperty('rate',voiceRate)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def Edith_Intro():
    speak("I am Edith")
    speak("Even Death I Am The Hero")
    
    
def curr_date():
    now  = datetime.now()
    date = now.strftime("%B %d , %Y")
    print("Today's Date : " , date)
    speak("Today's Date ")
    speak(date)
    
    
def curr_time():
    now  = datetime.now()
    time = now.strftime("%H:%M:%S")
    print("Current Time : ",time)
    speak('Current Time ')
    speak(time)
    
    
def wishMe():
    hour = int(datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good Morning Sir")
        
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir")
        
    else:
        speak("Good Evening Sir")
        
    
    Edith_Intro()
    curr_date()
    curr_time()
    speak("Welcome to my service How may I help you")
    
    

    
def takecommand():
   
    r = sr.Recognizer()
    
    with sr.Microphone() as source:                        
        print("Listening.....")
        r.pause_threshold = 1                             
        audio = r.listen(source)
        
    
    try :
        print("Recognizing...")
        query = r.recognize_google(audio,language="en-in")
        print(f"User said : {query}\n")
    
    except Exception as ex:
        print("Say that again please....")
        return "None"                                   
    
    return query




# Tasks to Perform

    
def wiki(query):
    if 'wikipedia' in query:
            speak("Searching Wikipedia......")
            
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences=2)
            
            speak("According to wikipedia : \n")
            print(result)
            speak(result)
            

def browser():
    speak("Opening") 
    speak("GOOGLE CHROME") 
    print(".") 
    print(".") 
    os.system("chrome")
    
    
def PlayMusic(): 
    music_dir = r'C:\Users\Music\All Songs\My Fav Songs'
    songs = os.listdir(music_dir)
    
    print("Tell your choice")
    speak("Tell your choice")
    print("1st Normal")
    speak("1st Normal")
    print("2nd Shuffle")
    speak("2nd Shuffle")

    ch = takecommand().lower()
    
    
    
    if ('1' in ch) or ("normal" in ch) or ("first" in ch) :
        for i in range(len(songs)) :
            song = os.path.join(music_dir ,songs[i])
            chk = songs[i].split('.')[1]
    
            if chk=="mp3":
                print('Current song : ',songs[i].split('.')[0])
                playsound(song)
            
            
    
   
    
    
    elif ('2' in ch) or ("shuffle" in ch) or ("second" in ch):
        while True :
            i = random.randint(0,len(songs)+1)
            song = os.path.join(music_dir ,songs[i])
            chk = songs[i].split('.')[1]
    
            if chk=="mp3":
                print('Current song : ',songs[i].split('.')[0])
                playsound(song)
            
      
    
            
    else:
        print("Invalid Choice")
        speak("Invalid Choice")
    
    
    
def notepad():
    speak("Opening")
    speak("NOTEPAD") 
    print(".") 
    print(".") 
    os.system("Notepad") 
    
    
def vlc():
    speak("Opening") 
    speak("VLC PLAYER") 
    print(".") 
    print(".") 
    os.system("VLC") 
    
    
def take_screenshot(): 
        print("Taking Screenshot..")
        speak("Taking Screenshot")
        
        path = ""
        img_name = str(datetime.now())
        img = pyautogui.screenshot()
        img.save(path+img_name)
        
        print("Screenshot Taken..")
        speak("Screenshot Taken")
        
        
        
def send_Mail(to_whom ,content):
    
    server = smtplib.SMTP('smtp.gmail.com' ,587)
    server.ehlo()
    server.starttls()
    
    server.login("enter your email id" ,"enter password")
    server.sendmail(sender_email ,to_whom ,content)
    
    print("Successfully sent email")
    speak("Successfully sent email")
    
    server.close()
    
    
    
def cpu_battery():
    usage = str(psutil.cpu_percent())
    speak("CPU is at " + usage)
    
    battery = psutil.sensors_battery.percent
    soeak("Battery is at " + battery)
    
    
    
def tell_jokes():
    joke = pyjokes.get_joke()
    speak(joke)
    
    
    
# Main Functions

if __name__=="__main__":
    wishMe()
    
    while True:
        
        query = takecommand().lower()
        
        # Search something on wikipedia
        if 'wikipedia' in query:
            wiki(query)
            
        
        # Open YouTube
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        
        # Open Google
        elif ('open google' in query) or ("search" in query) or ("web browser" in query) or ("chrome" in query) or ("browser" in query) :
            webbrowser.open("google.com")
            
    
        # Open StackOverFlow
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
            
        
        # PlayMusic
        elif 'play music' in query:
            PlayMusic()
        
        
        # Current time
        elif 'current time' in query:
            curr_time()
            
            
        # Current date
        elif "todays's date" in query:
            curr_date()
        
        
        # Visual studio
        elif "open visual studio" in query:
            path = r"C:\Users\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(path)
            
            
        # open notepad
        elif "open notepad" in query:
            notepad()
              
                
        # vlc player
        elif ("vlc player" in query) or ("video player" in query):
            vlc()
        
        
        
        # take screen shot
        elif ("screenshot" in query) or ("take screenshot" in query):
            take_screenshot()
            
            
        
        # send email 
        elif ('send mail' in query) or ('send email' in query):
            try:
                speak("Say the content of mail ")
                content = takecommand()
                
                print("Repeating the content again for your conformatiom")
                speak("Repeating the content again for your conformatiom")
                
                speak("To continue with this mail say send otherwise say exit")
                
                flag = takecommand()
                if(send in flag):
                    to = 'abc@mail.com'
                    send_Mail(to,content)
                else:
                    speak("Make changes to mail's content")
                

            
            except Exception as ex:
                speak(ex)
                speak("Unable to send mail")
                print("Unable to send mail")
            
            
        
        # Logout user from system
        elif ("logout" in query):
            os.system("shutdown - l")
        
        
        # restart the system
        elif ("restart" in query):
            os.system("shutdown /r /t 1")
        
        
        # shutdown the system
        elif ("shutdown" in query):
            os.system("shutdown /s /t 1")
        
        
        # Remember Function
        elif ("remember" in query):
            speak("What should I remember?")
            data = takecommand()
            
            speak("You said me to remember that "+ data)
            with open("data.txt" ,"w") as fp:
                fp.write(data)
        
        elif ("do you remember" in query):
            speak("Yes ,I remember what you said me")
            with open("data.txt" ,"r") as fp:
                speak(fp.read())
         
        
        
        #  CPU & Battery Update
        elif ("cpu" in query) or ("battery" in query):
            cpu_battery()
        
        
        # Jokes Function
        elif ("joke" in query):
            tell_jokes()
        
        
        # close the program
        elif ('exit' in query) or ('quit' in query) or ("stop" in query):
            speak("Okay sir , Have a nice day")
            break
        
            
        else:
            speak("Sorry , this is not available or may be i cant find it")
