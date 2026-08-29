## Stage one complete

This is an overhaul of an already finished project that I currently host and built for lakeshore.

Here is a link to the OG repo:

https://github.com/Catrat6/calc

### Whats Next

So the program has been completely re-written in python, It now calculates mileage and automatically decided if 
there are unloaded miles and then calculates them. I use the Google Maps API to calculate this and have a pretty clean
and sharp looking CLI program completed. 

What it does:
 - Finds the mileage from pickup to drop off 
 - Figures out if unloaded miles are needed and if they are it calculates them
 - Figures out the other required charges
 - Adds everything together and gives the total cost

Issues to fix:
 - Just realize I need the option to calculate for a round trip, very simple addition just need to add it
 - will add more as i find them

Building Next:
 - is the trip worth it for us to take?
 - What will the trip cost us? 

Now comes the big part ... we need to come up with an algo that can calculate if it is worth it or not for us to take
the trip and deliver that along with the cost. 