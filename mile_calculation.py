import os
import requests
from lists import yes_words, no_words
from dotenv import load_dotenv

load_dotenv()

class MilesCalculation:
    def __init__(self):
        self.office_address = 'N5806 Co Rd M, Plymouth, WI 53073'
        self.api_key = os.getenv('GOOGLE_MAPS_API_KEY')


    def get_trip_miles(self, pick_up, drop_off):
        url = "https://routes.googleapis.com/directions/v2:computeRoutes"

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
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

    def calculate_unloaded(self, pickup):

        unloaded_pick_up = self.get_trip_miles(self.office_address, pickup)

        if unloaded_pick_up <= 20:
            return 0
        else:
            return unloaded_pick_up

