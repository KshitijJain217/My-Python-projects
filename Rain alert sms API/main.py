
import requests
from twilio.rest import Client

account_sid = ""
auth_token = ""

weather_params = {
    "lat": 19.242439,
    "lon": 73.120193,
    "appid": "",
    "cnt": 4,
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)

# or you can use this
# response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast"
#                             "?lat=22.7179&lon=5.8333&appid=8e2d292b2207458260b065fafeed7741")
response.raise_for_status()

weather_data = response.json()
# print(weather_data)

slot: int
# current_weather = weather_data["list"][slot]["weather"][0]["id"]
# print(current_weather)
will_rain = False

for slot in range(0, 4):
    weather_id = weather_data["list"][slot]["weather"][0]["id"]
    # print(weather_id)
    if weather_id < 700:
        will_rain = True

if will_rain:
    # print("Bring an Umbrella! It might rain today.")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Bring an Umbrella! It might rain today.☔",
        from_="+17144002909",
        to="+91-----"
    )
    # print(message.body)
    print(message.status)

