import requests
import datetime

response1 = requests.get(url="http://api.open-notify.org/iss-now.json")
data1 = response1.json()
print(f"The current position of the ISS is, Latitude: {data1["iss_position"]["latitude"]} Longitude: {data1["iss_position"]["longitude"]}")

# Portugal
parameters = {
    "lat": 39.399872,
    "lng": -8.224454,
    "formatted": 0
}

response2 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
data2 = response2.json()
items_sunrise = data2["results"]["sunrise"].split("T")
items_sunset = data2["results"]["sunset"].split("T")
time_sunrise = items_sunrise[1].split("+")
time_sunset = items_sunset[1].split("+")
print(f"Sunrise time in PT: {time_sunrise[0]}")
print(f"Sunset time in PT: {time_sunset[0]}")
print(f"Current time in PT: {str(datetime.datetime.now().time()).split(".")[0]}")