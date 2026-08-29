from lists import yes_words, no_words

class TripCost:
    def __init__(self):
        self.base_cost = 35.0
        self.ah_charge = 20.0
        self.per_mile = 2.50
        self.wait_time = 15.0
        self.unload = 1.50


    def calculate_trip_cost(self, after_hours, legs, loaded_miles, unloaded_miles, wait, extra_charge):
        base = (self.base_cost * int(legs)) + (int(loaded_miles) * self.per_mile) + (int(unloaded_miles) * self.unload) + (
                    (int(wait) / 30) * self.wait_time)
        # add after hours charge and extra charge, if any
        if after_hours in yes_words:
            base = base + self.ah_charge
        if float(extra_charge) > 0:
            base = base + float(extra_charge)
        # add processing fee
        fee = int(base) * .04
        # final cost
        trip_cost = base + fee

        return trip_cost