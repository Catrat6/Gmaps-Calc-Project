from lists import yes_words, no_words

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