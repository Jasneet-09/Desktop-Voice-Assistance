import requests

api_address = "https://newsapi.org/v2/top-headlines?country=us&apiKey=" + "421125731eb84e108def5518322fa78f"
json_data = requests.get(api_address).json()

arr = []
def news():
    for i in range(3):
        arr.append("Number " + str(i+1) + " " + json_data["articles"][i]["title"] + ".")
    return arr

