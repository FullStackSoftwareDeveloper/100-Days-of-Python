import requests
from twilio.rest import Client

# fictional data used for demonstration purposes

# coordinates for Portugal, Lisbon
parameters = {
    "lat": 38.707008,
    "lon": -9.135640,
    "appid": "your_api_token",
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
data = response.json()

is_raining = False
for i in data["list"]:
    if int(i["weather"][0]["id"]) < 700:
        is_raining = True

if is_raining:
    client = Client("your_twilio_SID", "your_twilio_token")
    message = client.messages \
        .create(
        body="It's going to rain today, bring an umbrella!",
        from_="your_twilio_number",
        to="your_verified_number"
    )
    print(message.status)