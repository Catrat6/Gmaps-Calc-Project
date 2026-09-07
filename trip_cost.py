from lists import yes_words, no_words
from mile_calculation import MilesCalculation

# OPERATING COSTS
# MPG = 18
# DRIVER_COST = 20.00
# GAS_PRICE = 3.75
# LOAD_TIME = 10


class TripCost:
    def __init__(self):
        self.base_cost = 35.0
        self.ah_charge = 20.0
        self.per_mile = 2.50
        self.wait_time = 15.0
        self.unload = 1.50


    def calculate_trip_cost(self, after_hours, legs, round_trip, loaded_miles, unloaded_miles, wait, extra_charge):
        true_loaded = loaded_miles

        if round_trip in yes_words:
            true_loaded = loaded_miles * 2

        base = (self.base_cost * legs) + (true_loaded * self.per_mile) + (unloaded_miles * self.unload) + ((wait / 30) * self.wait_time)


        if after_hours in yes_words:
            base = base + self.ah_charge
        if float(extra_charge) > 0:
            base = base + float(extra_charge)

        fee = base * .04

        trip_cost = round(base + fee, 2)

        return trip_cost


class OperatingCost():
    def __init__(self):
        self.mpg = 18
        self.driver_cost = 20.0
        self.gas_price = 3.75  # per gallon
        self.load_time = 10
        self.wear_n_tear = .20  # $0.20/mile


    def find_operating_costs(self, pick_up, drop_off):

        mile_calculator = MilesCalculation()
        miles = mile_calculator.get_trip_miles(pick_up, drop_off)
        unloaded = mile_calculator.calculate_unloaded(pick_up, drop_off)
        time = mile_calculator.get_trip_time(pick_up, drop_off)
        extra_time, extra_miles = mile_calculator.unloaded_operating_extra(pick_up, drop_off)

        gazzerleen_cost = round((miles + unloaded + extra_miles) / self.mpg * self.gas_price, 2)

        drivers_pay = round((self.driver_cost / 60) * (time + extra_time), 2)

        wear = round(self.wear_n_tear * (miles + unloaded + extra_miles), 2)

        return gazzerleen_cost + drivers_pay + wear


















