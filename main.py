from lists import yes_words, no_words


# base cost per leg
base_cost = 35.0
# after hours charge
ah_charge = 20.0
# per milage rate
per_mile = 2.50
# wait time is $15 per 30 min interval
wait_time = 15.0
# unloaded miles
unload = 1.50

def user_query():
    trip_cost = 0.0

    a = input('Is this trip after hours, between 5PM and 7AM? (yes or no)\n').lower()

    b = input('How many legs does the trip have?\n')

    c = input('how many loaded miles\n')

    d = input('how many unloaded miles\n')

    e = input('how much wait time? (30 min intervals only)\n')

    f = input('add any other random dollar amount (if none enter 0):\n')

    base = (base_cost * int(b)) + (int(c) * per_mile) + (int(d) * unload) + ((int(e) / 30) * wait_time)

    if a in yes_words:
        base = base + 20
    if float(f) > 0:
        base = base + float(f)

    fee = int(base) * .04
    trip_cost = base + fee

    print(trip_cost)

user_query()