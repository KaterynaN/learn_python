from datetime import date, timedelta

OUT_DATE_START = (date.today() + timedelta(days=1)).strftime("%Y-%m-%d")
OUT_DATE_END = (date.today() + timedelta(days=181)).strftime("%Y-%m-%d")


#This class is responsible for structuring the flight data.

class FlightData:
    def __init__(self, price, origin, destination, out_date, return_date, stops):
        self.price = price,
        self.origin = origin,
        self.destination = destination,
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(data):
    if data is None or not data['data']:
        print("No flight data")
        return None

    # Data from the first flight in the json
    first_flight = data['data'][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    stops = len(first_flight["itineraries"][0]["segments"]) - 1
    destination = first_flight["itineraries"][0]["segments"][stops]["arrival"]["iataCode"]
    out_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
    return_date = first_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date, stops)

    for flight in data['data']:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            # destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            stops = len(flight["itineraries"][0]["segments"])-1
            destination = flight["itineraries"][0]["segments"][stops]["arrival"]["iataCode"]
            out_date = flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            return_date = flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    print(f"Lowest price from {cheapest_flight.origin} to {cheapest_flight.destination}, from {cheapest_flight.out_date} to {cheapest_flight.return_date} with {cheapest_flight.stops} stops is £{cheapest_flight.price}")

    return cheapest_flight
