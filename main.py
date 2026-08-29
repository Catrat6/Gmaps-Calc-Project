import os
import requests
from lists import yes_words, no_words
from trip_cost import TripCost
from mile_calculation import MilesCalculation


while True:

    mile_calculator = MilesCalculation()

    pick_up_address = input('What is your pick up address?\n')

    drop_off_address = input('What is your drop off address?\n')

    a = input('Is this trip after hours, between 5PM and 7AM? (yes or no)\n').lower()

    b = input('How many legs does the trip have?\n')

    c = mile_calculator.get_trip_miles(pick_up_address, drop_off_address)

    d = mile_calculator.calculate_unloaded(pick_up_address)

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


