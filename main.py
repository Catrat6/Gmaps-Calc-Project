import os
import requests
from lists import yes_words, no_words
from dotenv import load_dotenv
from trip_cost import TripCost

load_dotenv()

api_key = os.getenv("GOOGLE_MAPS_API_KEY")

OFFICE_ADDRESS = 'N5806 Co Rd M, Plymouth, WI 53073'

def get_trip_miles(pick_up, drop_off):

    url = "https://routes.googleapis.com/directions/v2:computeRoutes"

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": "routes.distanceMeters"
    }

    body = {
        "origin": {
            "address": pick_up
        },
        "destination": {
            "address": drop_off
        },
        "travelMode": "DRIVE"
    }

    response = requests.post(
        url,
        headers=headers,
        json=body
    )

    data = response.json()

    rounded_miles = round(data['routes'][0]['distanceMeters'] / 1609.344)

    return rounded_miles

def calculate_unloaded(office, pick_up):

    unloaded_pick_up = get_trip_miles(office, pick_up)

    if unloaded_pick_up <= 20:
        return 0
    else:
        return unloaded_pick_up

while True:

    pick_up_address = input('What is your pick up address?\n')

    drop_off_address = input('What is your drop off address?\n')

    a = input('Is this trip after hours, between 5PM and 7AM? (yes or no)\n').lower()

    b = input('How many legs does the trip have?\n')

    c = get_trip_miles(pick_up_address, drop_off_address)

    d = calculate_unloaded(OFFICE_ADDRESS, pick_up_address)

    e = input('how much wait time? (30 min intervals only)\n')

    f = input('add any other random dollar amount (if none enter 0):\n')

    calculate_cost = TripCost()

    cost = calculate_cost.calculate_trip_cost(a, b, c, d, e, f)

    print(cost)

    repeat = input('Would you like to calculate another trips cost?\n')

    if repeat in yes_words:
        continue
    else:
        break


