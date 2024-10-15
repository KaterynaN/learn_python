import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth
from pprint import pprint

#This class is responsible for talking to the Google Sheet.

load_dotenv()
SHEETY_GOOGLE_SHEET = os.environ.get("SHEETY_GOOGLE_SHEET")

class DataManager:
    def __init__(self):
        self.destination_data = {}
        self.users_data = {}
        self._prices_endpoint = f'https://api.sheety.co/{SHEETY_GOOGLE_SHEET}/flightDeals/prices'
        self._users_endpoint = f'https://api.sheety.co/{SHEETY_GOOGLE_SHEET}/flightDeals/users'
        self._header = {"Authorization": os.environ.get("SHEETY_AUTH")
}

    def get_destination_data(self):
        # GET all the data in that sheet and print it out.
        response = requests.get(url=self._prices_endpoint, headers=self._header)
        data = response.json()['prices']
        self.destination_data = data
        pprint(data)
        return self.destination_data

    def update_destination_code(self, code, id):
        new_data = {
            'price': {
                'iataCode': code
            }
        }
        response = requests.put(url=f'{SHEETY_PRICES_ENDPOINT}/{id}', json=new_data, headers=sheety_headers)
        print(response.text)

    def get_user_emails(self):
        response = requests.get(url=self._users_endpoint, headers=self._header)
        data = response.json()['users']
        self.users_data = data
        return self.users_data
