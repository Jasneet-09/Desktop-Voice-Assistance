import webbrowser
import pyttsx3 as p

engine = p.init() 
def say(text):
    engine.say(text)
    engine.runAndWait()

def play_music(text):
    if len(text)==0:
        say("Sorry, I can't understand you")
    else:
        query = f"play {text} on YouTube"
        search_url = f"https://www.youtube.com/results?search_query={text}"
        webbrowser.open(search_url)
