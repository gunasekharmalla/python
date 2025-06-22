import datetime

now = datetime.datetime.now()
print("Current date and time:", now)

future = now + datetime.timedelta(days=5)
print("Date after 5 days:", future)

dob = datetime.datetime(2000, 6, 15)
age = now.year - dob.year
print("Age (rough):", age)

Output:
        Current date and time: 2025-06-22 04:13:40.179269
        Date after 5 days: 2025-06-27 04:13:40.179269
        Age (rough): 25
-----------------------------------------------------------------------------
