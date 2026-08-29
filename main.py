import os
from lists import yes_words, no_words
from dotenv import load_dotenv
from trip_cost import TripCost

load_dotenv()

api_key = os.getenv("GOOGLE_MAPS_API_KEY")


while True:

    a = input('Is this trip after hours, between 5PM and 7AM? (yes or no)\n').lower()

    b = input('How many legs does the trip have?\n')

    c = input('how many loaded miles\n')

    d = input('how many unloaded miles\n')

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


