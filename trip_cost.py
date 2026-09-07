from lists import yes_words, no_words
from main import mile_calculator
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

        base = (self.base_cost * int(legs)) + (int(true_loaded) * self.per_mile) + (int(unloaded_miles) * self.unload) + (
                    (int(wait) / 30) * self.wait_time)



        if after_hours in yes_words:
            base = base + self.ah_charge
        if float(extra_charge) > 0:
            base = base + float(extra_charge)

        fee = int(base) * .04

        trip_cost = base + fee

        return trip_cost

# Unfinished Class

class OperatingCost(TripCost):
    def __init__(self, base_cost, ah_charge, per_mile, wait_time, unload):
        super().__init__(base_cost, ah_charge, per_mile, wait_time, unload)

        self.mpg = 18
        self.driver_cost = 20.0
        self.gas_price = 3.75  # per gallon
        self.load_time = 10
        self.wear_n_tear = .20  # cents per mile


    def find_operating_costs(self, pick_up, drop_off):

        mile_calculator = MilesCalculation()

        miles = mile_calculator.get_trip_miles(pick_up, drop_off)

        unloaded = mile_calculator.calculate_unloaded(pick_up)

        time = mile_calculator.get_trip_time(pick_up, drop_off)

        gazzerleen_cost = round((miles + unloaded) / self.mpg) * self.gas_price

        drivers_pay = (self.drivers_cost / 60) * time














