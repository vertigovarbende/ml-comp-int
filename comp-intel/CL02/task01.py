# (1) Given a variable `a` (containing any value), re-assign the value `"N/A"` if `a` is `None`,
# and leave `a` unchanged otherwise. Use an `if...else...` statement.


a = input("Enter an sth: ")
a = "N/A" if a is None else a
print(a)


# (2) same thing with ternary but i used ternary operator already.

# (3)
"""
Given an credit score `score`, assign a string value to another variable `rating` based on the following scale:

- [0, 580) --> Poor
- [580, 670) --> Fair
- [670, 740) --> Good
- [740, 800) --> Very Good
- [800, 850] --> Excellent
"""


score = int(input("Enter your score: "))
state = ""

if score >= 800:
    state = "Excellent"
elif score >= 740:
    state = "Very Good"
elif score >= 670:
    state = "Good"
elif score >= 580:
    state = "Fair"
elif score >= 0:
    state = "Poor"

print(f"Your state is {state}")


# (4)
"""
Given an `elapsed` time (in seconds), write code to set a variable `magnitude` based on the following conditions:

- if elapsed time is less than 1 minute, `magnitude` --> `'seconds'`
- if elapsed time is more than 1 minute, but less than 1 hour, `magnitude` --> `'minutes'`
- if elapsed time is more than 1 hour, but less than 1 day, `magnitude` --> `'hours'`
- if elapsed time is more than 1 day, but less than 1 week: `magnitude` --> `'days'`
- if elapsed time is more than 1 week, `magnitude` --> '`weeks'`
"""

elapsed = int(input("Elapsed time: "))
magnitude = ""
if elapsed < 60:
    magnitude = "seconds"
else:
    if elapsed >= 60 & elapsed < 3600:
        magnitude = "minutes"
    else:
        if elapsed >= 3600 & elapsed < 86_400:
            magnitude = "hours"
        else:
            if elapsed >= 86_400 & elapsed <  604_800:
                magnitude = "days"
            else:
                magnitude = "weeks"

print(f'{elapsed} ==> {magnitude}')








































