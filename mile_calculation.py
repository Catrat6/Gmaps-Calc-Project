import os
import requests
from lists import yes_words, no_words
from dotenv import load_dotenv

load_dotenv()

class MilesCalculation:
    def __init__(self):
        self.office_address = 'N5806 Co Rd M, Plymouth, WI 53073'
        self.api_key = os.getenv('GOOGLE_MAPS_API_KEY')


    def get_trip_info(self, pick_up, drop_off):
        url = "https://routes.googleapis.com/directions/v2:computeRoutes"

        headers = {
            "Content-Type": "application/json",
            "X-Goog-Api-Key": self.api_key,
            "X-Goog-FieldMask": "routes.distanceMeters,routes.duration"
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

        return data

    def get_trip_miles(self, pick_up, drop_off):

        trip_info = self.get_trip_info(pick_up, drop_off)

        return round(trip_info['routes'][0]['distanceMeters'] / 1609.344)

    def get_trip_time(self, pick_up, drop_off):

        trip_info = self.get_trip_info(pick_up, drop_off)

        time_seconds = trip_info['routes'][0]['duration'].replace('s', '')

        return round(int(time_seconds) / 60)


    def calculate_unloaded(self, pick_up, drop_off):

        unloaded_pick_up = self.get_trip_miles(self.office_address, pick_up)
        unloaded_drop_off = self.get_trip_miles(self.office_address, drop_off)

        if unloaded_pick_up <= 20:
            unloaded_pick_up = 0
        if unloaded_drop_off <= 20:
            unloaded_drop_off = 0

        return unloaded_pick_up + unloaded_drop_off

    def unloaded_operating_extra(self, pick_up, drop_off):

        unloaded_a_m = self.get_trip_miles(self.office_address, pick_up)

        if unloaded_a_m < 20:
            unloaded_a_m = 0

        unloaded_a_t = self.get_trip_time(self.office_address, pick_up)

        unloaded_b_m = self.get_trip_miles(self.office_address, drop_off)

        if unloaded_b_m < 20:
            unloaded_b_m = 0

        unloaded_b_t = self.get_trip_time(self.office_address, drop_off)

        total_miles = unloaded_a_m + unloaded_b_m
        total_time = unloaded_a_t + unloaded_b_t

        return total_miles, total_time