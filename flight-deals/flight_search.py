from dotenv import load_dotenv
import requests
from urllib.parse import urlencode
from requests.auth import HTTPBasicAuth
import os

load_dotenv()


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.environ.get("AMADEUS_API_KEY")
        self._api_secret = os.environ.get("AMADEUS_API_SECRET")
        self._token = self._get_new_token()

    def _get_new_token(self):
        header = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret
        }

        encoded_body = urlencode(body)

        token_endpoint = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        response = requests.post(url=token_endpoint, data=body, headers=header)
        print(f"Your token is {response.json()['access_token']}")
        print(f"Your token expires in {response.json()['expires_in']} seconds")
        return response.json()['access_token']

    def get_destination_code(self, city_name):
        city_code_endpoint = 'https://test.api.amadeus.com/v1/reference-data/locations/cities'

        header = {
            'Authorization': f'Bearer {self._token}'
        }

        params = {
            'keyword': city_name.upper(),
            'max': '2',
            'include': 'AIRPORTS'
        }
        response = requests.get(url=city_code_endpoint, params=params, headers=header)

        try:
            code = response.json()["data"][0]['iataCode']
        except IndexError:
            print(f"IndexError: No airport code found for {city_name}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No airport code found for {city_name}.")
            return "Not Found"

        return code

    def check_flights(self, depart_city, destination_city, depart_date, return_date, max_price, connection_number=0):
        flight_search_endpoint = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
        header = {
            'Authorization': f'Bearer {self._token}',
            'X-HTTP-Method-Override': 'POST'
        }

        getFlightOffersBody = {
            "currencyCode": "GBP",
            "originDestinations": [
                {
                    "id": "1",
                    "originLocationCode": depart_city,
                    "destinationLocationCode": destination_city,
                    "departureDateTimeRange": {
                        "date": depart_date.strftime("%Y-%m-%d"),
                        "dateWindow": "P3D"
                    }
                },
                {
                    "id": "2",
                    "originLocationCode": depart_city,
                    "destinationLocationCode": destination_city,
                    "arrivalDateTimeRange": {
                        "date": return_date.strftime("%Y-%m-%d"),
                        "dateWindow": "I3D"
                    }
                }
            ],
            "travelers": [
                {
                    "id": "1",
                    "travelerType": "ADULT"
                }
            ],
            "sources": [
                "GDS"
            ],
            "searchCriteria": {
                "maxFlightOffers": 10,
                "maxPrice": max_price,
                "flightFilters": {
                    "connectionRestriction": {
                        "maxNumberOfConnections": connection_number
                    }
                }
            }
        }

        search_data = {
            "getFlightOffersBody": getFlightOffersBody
        }

        response = requests.post(url=flight_search_endpoint, json=getFlightOffersBody, headers=header)
        if response.status_code != 200:
            print(f"check_flights() response code: {response.status_code}")
            print("There was a problem with the flight search.\n"
                  "For details on status codes, check the API documentation:\n"
                  "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                  "-reference")
            print("Response body:", response.text)
            return None

        return response.json()
