import requests
from dotenv import load_dotenv
import os
from twilio.rest import Client

load_dotenv()
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')

api_key = os.environ.get('OMW_API_KEY')
my_lat = 55.703830
my_lon = 21.137861

params = {
    "lat": my_lat,
    "lon": my_lon,
    "appid": api_key,
    "cnt": 4
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params)
response.raise_for_status()
weather_data = response.json()
description = weather_data["list"][0]["weather"][0]['description']
weather_ids = [item["weather"][0]["id"] for item in weather_data["list"]]

if any(weather_id < 700 for weather_id in weather_ids):
    client = Client(account_sid, auth_token)
    send_from = os.environ.get('FROM_TWILIO_WHATSAPP_NUMBER')
    send_to = os.environ.get('TO_TWILIO_WHATSAPP_NUMBER')
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It will rain today.Bring an ☔️!",
        to="whatsapp:+380971861014",
    )
    print(message.status)





