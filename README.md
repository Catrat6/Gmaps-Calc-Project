## Stage Two (underway) V 0.75

A Beta version of the web app is now available to anyone at lakeshore, please message me 
and I will give you the servers IP as I dont have it tied to a domain yet, you can also find 
it in our slack. I will make it publically available and bind it to a domain when I launch the finished
version. 

In its current state it is a minimum viable product, it works great, has error handling
and I do not personally see any glaring issues.

It uses the same logic and algo that I wrote for V1 but it has now been optimized to run
in the browser. With the help of AI I took my work from V1 and ported it in to a web app 
that runs in the browser. The end user no longer has to fuss with python, dependencies or API keys. 

### Test stack 
- Linode (Ubuntu 26.04)
- NGINX
- Flask
- Gunicorn

From here I will continue to test using this version of the web app while i work at 
cleaning up the code and re-writing some of the changes GPT took liberties with. For instance
I will rework it to follow OOP standards and make it extremely easy to change pricing the same way it
is in the V1 code. 

If you compare app.py to my OG algo found in main.py, mile_calculation.py, and trip_cost.py
you will see what I mean although I must say i am very satisfied with the outcome and even though
it may be a little out of place here i wanted to say THAT is how AI should be used ... you dont have it
create the app for you ... you build a base version of it and lay it all out THEN you bring
in an agent to help you out. It works much better this way as well and gets what you want on the first 
go.

### Next Steps
- Rewrite app.py, web.py and index.html to follow O.O.P and my personal style
  - Fix any issues and bugs 
- Lay out the plan for adding in payer swap and custom profiles as well as other options and settings
  - These options will be something like a drop down menu that will allow you to quickly
    swap between different sets of pricing. There will also be the ability to create your
    own custom pricing models to add to the drop down menu.
- Lay out the plan for user login
  - The main reason behind user login will really be to protect the API key so that we 
    dont need to have the end user deal with it. With user login and profiles we can just
    have everyone share the same key and not have to worry about entering it or securing 
    it.
  - User profiles can also have a few other settings like color themes and stuff.

### Further Steps:
- Find permanent domain
- Plan security for server and domain
- Add on User login and Pricing profiles
- Penetration test
- Fix any found bugs and issues 

Launch V 1.0 Web APP!

Launch date: November 16 2026

# Old updates:

## Stage one complete

This is an overhaul of an already finished project that I currently host and built for lakeshore.

Here is a link to the OG repo:

https://github.com/Catrat6/calc

## Version 0.5    (update 9/7/26)

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

Building Next:
 - is the trip worth it for us to take? 
 - ~~What will the trip cost us?~~ 

In the process of building this now, the new class exists in trip_cost.py and inherits the OG trip cost class
Almost done writing out the initial class and functions. Will dive into it more once I reach that point 

### Ver 0.6 Operating Cost Update 9/7/26

Calculation of the operating cost is complete in its most basic form.

It can def. be fine tuned and does not take in to consideration things like office costs, and other office
related overhead. Although, if you want to exclude those things then I suppose this is a pretty fair
estimate. 

Next I will work on fine tuning the calculation and trim down my code. I def need to rework some of the classes
so that I use less API calls, surely I can rewrite it better and use only one call and just store all the information
in attributes or something. 

Whats Next?:
- Refine operating cost calculation, dial it in and make it more specific 
- sand down the code, remove any repeating portions and work on limiting API calls 
  - Rework class and functions to maybe use just a single API call 
