import requests
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()

api_key = os.environ.get("API_KEY")
app_id = os.environ.get("APP_ID")
post_workout = os.environ.get("POST_WORKOUT_ENDPOINT")
print(api_key, app_id)

trackapi_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = f"https://api.sheety.co/{post_workout}"

header = {
    "x-app-id": app_id,
    "x-app-key": api_key
}

params = {
    "query": input("What exercises you did?"),
    "weight_kg": 52,
    "height_cm": 163,
    "age": 41
}

date = datetime.now()

response = requests.post(url=trackapi_endpoint, json=params, headers=header)
result = response.json()['exercises']
workout_data = [{"date": date.strftime("%d.%m.%Y"),
                 "time": date.strftime("%H:%M:%S"),
                 "exercise": item['name'],
                 "duration": item['duration_min'],
                 "calories": item['nf_calories']} for item in result]
# print(workout_data)

sheety_headers = {
    "Authorization": os.environ.get("SHEETY_AUTH")
}
for workout in workout_data:
    workout_json = {"workout": workout}
    sheety_response = requests.post(url=sheety_endpoint, json=workout_json, headers=sheety_headers)
    print(sheety_response.text)



