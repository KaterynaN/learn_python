import requests
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    print(f"{iss_latitude}, {iss_longitude}")

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5 and MY_LAT - 5 <= iss_longitude <= MY_LAT + 5:
        print("Look at the sky!")
        return True
    else:
        print("Not today")
        return False

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if sunset <= time_now or sunrise >= time_now:
        return True

if is_iss_overhead() and is_night():
    print(f"It's time to look at the sky (sent reminder) Time: {time_now}")

#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
