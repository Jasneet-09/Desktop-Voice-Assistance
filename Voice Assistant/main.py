import pyttsx3 as p
import speech_recognition as sr
from wikipedia_web import get_info
from youtube_music import play_music
from news import news
import randfacts
from jokes import joke
from weather import *
import datetime
import random

engine = p.init() # Use to initiate the pyttsx3

rate = engine.getProperty('rate') # Provide the speed of the voice
engine.setProperty('rate',180) # Set the rate at 180 speed

voices = engine.getProperty('voices') # get the voice
engine.setProperty('voice', voices[0].id) # Set the voice 

def say(text):
    engine.say(text) # First statement of the Voice 
    engine.runAndWait() # We want it to run and then wait for the voice

def listen():
    r = sr.Recognizer() # instance of recognizer class in other words it help us to retrieve add from our microphone
    with sr.Microphone() as source:
        r.energy_threshold = 10000 
        r.adjust_for_ambient_noise(source,1.2) 
        r.pause_threshold = 1
        print("listening...")
        try:
            audio = r.listen(source, timeout=5) 
            text = r.recognize_google(audio)
            print(text)
            return text
        except Exception as e:
            say("unable to understand you")
            print("unable to understand you")
            return None

            
greetings = ["It's my pleasure", "You're welcome", "Glad I could help you"]

#--------------------------------------------DATE-TIME-----------------------------------------------------
today_date = datetime.datetime.now()
say("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B"))
print("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B"))

#-------------------------------------------INTRODUCTION---------------------------------------------------
print("Hello, I'm your voice assistant.")
say("Hello, I'm your voice assistant.")

#-----------------------------------------ASKING WHAT YOUR WELL BEING--------------------------------------
say("How are You??")
text = listen()
#------------------------------------------REPLYING RELATED TO IT'S WELL BEING-----------------------------
if "what" and "about" and "you" in text:
    say("I am good")
print("what can I do for you?")
say("what can I do for you?")



#------------------------------------LOOP TO INITIATE THE CONVERSATION-------------------------------------
while(True):
    text = listen()
    if text==None:
        say("Bye Bye!!")
        print("Bye Bye!!")
        break
    elif "information" in text or "about" in text or "i want to know" in text:
        get_info(text)
        break
    elif "play" in text or "video" in text or "music" in text:
        say("you want me to play which video?")
        vid = listen()
        print("Playing {} on youtube".format(vid))
        say("Playing {} on youtube".format(vid))
        play_music(vid)
        break
    elif "news" in text:
        arr = news()
        for i in arr:
            print(i)
            say(i)
    elif "fact" in text or "facts" in text:
        say("Sure")
        x = randfacts.get_fact()
        print(x)
        say("Did you know that, " + x)
    elif "joke" in text:
        data = joke()
        print(data[0])
        say(data[0]+", ")
        print(data[1])
        say(data[1])
    elif "thank" in text or "you" in text:
        say(random.choice(greetings))
        break
    elif "weather" in text or "temperature" in text:
        t = str(temp())
        d = str(des())
        print("Today's temperature is " + t + "deg C" +"and with" + d)
        say("Today's temperature is " + t + "deg C" +"and with" + d)
    elif "what's" in text and "time" in text:
        today_date = datetime.datetime.now()
        say("Today is " + today_date.strftime("%d") + " of " + today_date.strftime("%B") + " And its currently " + (today_date.strftime("%I")) + (today_date.strftime("%H")) + (today_date.strftime("%D")))
    else:
        say("Unable to understand you")
        say("Please Try again")
