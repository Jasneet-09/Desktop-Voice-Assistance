import wikipedia
import pyttsx3 as p

engine = p.init()

def say(text):
    engine.say(text)
    engine.runAndWait()

def get_info(text):
    if "about" in text:
        data = list(text.split(" "))
        ind = data.index("about")
        data = data[ind + 1:]
        if len(data) == 0:
            say("Sorry, I can't understand you")
        else:
            command = " ".join(data)
            try:
                say("searching {} on wikipedia",info)
                info = wikipedia.summary(command, sentences=3)
                print(info)                
            except:
                say("Can you say that again")
    elif "related to" in text:
        data = list(text.split(" "))
        ind = data.index("related")
        data = data[ind + 2:]
        if len(data) == 0:
            say("Sorry, I can't understand you")
        else:
            command = " ".join(data)
            try:
                say("searching {} on wikipedia",info)
                info = wikipedia.summary(command, sentences=3)
                print(info)
                say(info)
                
            except:
                say("Can you say that again")
    else:
        say("Sorry, I can't understand you")


