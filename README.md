## Stage one complete

This is an overhaul of an already finished project that I currently host and built for lakeshore.

Here is a link to the OG repo:

https://github.com/Catrat6/calc

## Version 1.5    (update 9/7/26)

Updates made to how the calculation runs, object layout, and a new API call for time. 

- **API class and new call**
  - The API class has been modified and completely retooled. It now features a function that simply calls the
     API and returns ALL of the data for the trip.
  - Now individual functions will be used to obtain specific data points by re-using the generic pull 
    function and returning only what is needed.
  - We are now able to calculate the time a trip will take, am individual function has been created to gather 
    that information and the final output now includes how long the trip will take in minutes 
- **Small changes to object layouts, edge smoothing**
- **Changes to how calculation runs**
  - retooled to utilize new functions 
  - process changes 
  - final response now includes time 
- Round Trip
  - The ability to make a trip a "round trip" has been added 


### Whats Next

So the program has been completely re-written in python, It now calculates mileage and automatically decided if 
there are unloaded miles and then calculates them. I use the Google Maps API to calculate this and have a pretty clean
and sharp looking CLI program completed. 

What it does:
 - Finds the mileage from pickup to drop off 
 - Figures out if unloaded miles are needed and if they are it calculates them
 - Figures out the other required charges
 - Adds everything together and gives the total cost
 - Calculates how long a trip will take

Issues to fix:
 - ~~Just realize I need the option to calculate for a round trip, very simple addition just need to add it~~
 - ....

**Building Next:
 - is the trip worth it for us to take? 
 - ~~What will the trip cost us?~~** done

In the process of building this now, the new class exists in trip_cost.py and inherits the OG trip cost class
Almost done writing out the initial class and functions. Will dive into it more once I reach that point 

#### Operating Cost Update 9/7/26

Calculation of the operating cost is complete in its most basic form.

It can def. be fine tuned and does not take in to consideration things like office costs, and other office
related overhead. Although, if you want to exclude those things then I suppose this is a pretty fair
estimate. 

Next I will work on fine tuning the calculation and trim down my code. I def need to rework some of the classes
so that I use less API calls, surely I can rewrite it better and use only one call and just store all the information
in attributes or something. 

