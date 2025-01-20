# Key Classes in datetime module:
# datetime: A combination of a date and a time.
# date: Represents a date (year, month, day).
# time: Represents a time (hour, minute, second, microsecond).
# timedelta: Represents a time difference.
# timezone: Provides time zone information.
# tzinfo: Base class for dealing with time zone information.

print("----------------------------------------------------------------")
# ommon Operations with datetime
# 1. Getting Current Date and Time
from datetime import datetime

# Current date and time
now = datetime.now()
print("Current date and time:", now)

print("----------------------------------------------------------------")
# 2. Creating a Specific Date and Time
# from datetime import datetime

# Creating a specific datetime
dt = datetime(2025, 1, 20, 14, 30, 45)
print("Specific datetime:", dt)

print("----------------------------------------------------------------")
# 3. Formatting Date and Time
# You can format a datetime object into a string using strftime().
from datetime import datetime

now = datetime.now()

# Formatting the datetime into a string
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time:", formatted_date)

# Common Format Codes:
# %Y: Year (4 digits)
# %m: Month (2 digits)
# %d: Day (2 digits)
# %H: Hour (24-hour format)
# %M: Minute
# %S: Second
print("----------------------------------------------------------------")
# 4. Getting Current Date Only
from datetime import date

# Getting current date
today = date.today()
print("Today's date:", today)

print("----------------------------------------------------------------")
# 5. Getting Current Time Only
from datetime import datetime

# Getting current time
now = datetime.now()
current_time = now.time()
print("Current time:", current_time)


print("----------------------------------------------------------------")
# 6. Time Difference (timedelta)
# You can subtract two datetime objects to get a timedelta object, which represents the difference between them.
from datetime import datetime, timedelta

# Two dates
dt1 = datetime(2025, 1, 1)
dt2 = datetime(2025, 1, 20)

# Time difference
delta = dt2 - dt1
print("Time difference:", delta)


print("----------------------------------------------------------------")
# 7. Adding or Subtracting Time (timedelta)
# You can add or subtract time intervals (days, hours, etc.) from a datetime object.
from datetime import datetime, timedelta

# Current date and time
now = datetime.now()

# Adding 5 days to the current date
new_date = now + timedelta(days=5)
print("Date after 5 days:", new_date)

# Subtracting 2 days from the current date
new_date = now - timedelta(days=2)
print("Date before 2 days:", new_date)

print("----------------------------------------------------------------")
# 8. Parsing Strings to datetime Objects
# You can use strptime() to convert a string into a datetime object.

from datetime import datetime

date_string = "2025-01-20 14:30:45"
dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", dt)


print("----------------------------------------------------------------")
# 9. Working with Time Zones (timezone)
# You can create time zone-aware datetime objects using the timezone class.

from datetime import datetime, timezone, timedelta

# Creating a timezone with a 5-hour offset
tz = timezone(timedelta(hours=5))

# Current time in UTC+5
now_with_tz = datetime.now(tz)
print("Current time with timezone:", now_with_tz)

print("----------------------------------------------------------------")
# Calculating Age
# You can calculate someone's age by subtracting their birthdate from today's date.
from datetime import date

# Birthdate
birthdate = date(2002, 1, 10)

# Current date
today = date.today()

# Calculating age
age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
print("Age:", age)


print("----------------------------------------------------------------")
# Summary:
# The datetime module provides tools for working with date and time.
# You can format, parse, and perform arithmetic with dates and times.
# The module includes classes like datetime, date, time, and timedelta for flexible date/time manipulation.