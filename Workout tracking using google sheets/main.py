import requests
from datetime import datetime

API_ID = "f4eb0f46"
API_KEY = ""

WEIGHT_KG = 67
HEIGHT_CM = 193
AGE = 22

sheet_endpoint = "https://api.sheety.co/6b3eb34361778c58f64ba85166f47590/copyOfMyWorkouts/workouts"
BEARER_TOKEN = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_query = input("What exercise did you do today? : ")

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY
}

# uses NLP of nutritionX to determine the exercise time,calories,etc.
NLP_parameters = {
    "query": exercise_query,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=exercise_endpoint, json=NLP_parameters, headers=headers)
result = response.json()
# print(result)

today = datetime.now()

bearer_headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # To use without authentication:
    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)
    # print(sheet_response.text)

    sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs, headers=bearer_headers)

# acess the sheet using https://docs.google.com/spreadsheets/d/1
