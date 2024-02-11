import requests


api_add = "https://api.openweathermap.org/data/2.5/weather?q=Kanpur&appid=bae3d4c184218985e305f0b396590b7e"
json_data = requests.get(api_add).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature 

def des():
    description = json_data["weather"][0]["description"]
    return description

