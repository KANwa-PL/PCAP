from time import time as timestamptime
from datetime import date, timedelta, time

today = date.today()
yesterday = date.today() - timedelta(days=1)
daybeforeyesterday = yesterday - timedelta(days=1)

timestamp = timestamptime()
datefromtimestamp = date.fromtimestamp(timestamp)

iso = date.fromisoformat('2014-10-18')

print(today == yesterday)
print(yesterday)
print(daybeforeyesterday)
print(datefromtimestamp)
print(iso)
print(iso.isoweekday())
print(iso.replace(2014, 10, 23).isoweekday())

t = time(14, 53, 20, 1)

print("Time:", t)
print("Hour:", t.hour)
print("Minute:", t.minute)
print("Second:", t.second)
print("Microsecond:", t.microsecond)
