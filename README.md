# Clock-In-Out
A web application that allows teachers to clock-in and clock-out from work.

## How it works

- The admin is the only user that can create teacher accounts. 
- The admin username is "admin" and password is "terriblepassword1". 
- Teachers can use the homepage form to select their name from a list, and clock-in or clock-out.
- To view clock events, click the link on the home-page. This will ask for an admin log-in, since the admin is hte only user who should be viewing clock events.

## How it can be improved (a non-exhaustive list)
- Teachers type their name, and their input is validated against the data-base (instead of being presented a list). 
- The Clock model can be sub-classed into Clock-In and Clock-Out classes. These can store more specific information, such as the reason for clocking-out early or the reason for clocking-in late. 
- Only allow a clock-out if the database current holds a clock-in event from the same day. Also, allow users to retroactively clock-in or clock-out with a user inputted time (in case they forgot to do so earlier, or had something urgent to attend to).
- Include permissions for visiting the list-events URL directly. 
