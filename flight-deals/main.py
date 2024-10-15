#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from datetime import date, timedelta
from dotenv import load_dotenv
from pprint import pprint
import time
import os
from flight_search import FlightSearch
from data_manager import DataManager
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

load_dotenv()

ORIGIN_CITY_IATA = "LON"

flight_search = FlightSearch()
data_manager = DataManager()
notification_manager = NotificationManager()

#------Update data in Google Sheet (IATA Codes)-------------
sheety_data = data_manager.get_destination_data()

for item in sheety_data:
    if item['iataCode'] == '':
        item['iataCode'] = flight_search.get_destination_code(city_name=item['city'])
        data_manager.update_destination_code(item['iataCode'], item['id'])
        time.sleep(2)

#--------------Find Cheapest Flight------------------------------
depart_date = date.today() + timedelta(days=7)
return_date = date.today() + timedelta(days=14)


for destination in sheety_data:
    print(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        depart_city=ORIGIN_CITY_IATA,
        destination_city=destination['iataCode'],
        depart_date=depart_date,
        return_date=return_date,
        max_price=destination['lowestPrice'])

    if flights is None or not flights['data']:
        flights = flight_search.check_flights(
            depart_city=ORIGIN_CITY_IATA,
            destination_city=destination['iataCode'],
            depart_date=depart_date,
            return_date=return_date,
            max_price=destination['lowestPrice'],
            connection_number=2)

    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight:
        msg = f"Low price alert! Only GBP {cheapest_flight.price} to fly "\
                f"from {cheapest_flight.origin} to {cheapest_flight.destination}, "\
                f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."\
                f"stops: {cheapest_flight.stops}"

        notification_manager.send_message(message_body=msg)

        users_data = data_manager.get_user_emails()
        emails = [user['email'] for user in users_data]
        message_body = f"Subject:Cheap Flights\n\n{msg}"

        for email in emails:
            notification_manager.send_email(email, message_body)
    # Slowing down requests to avoid rate limit
    time.sleep(2)



