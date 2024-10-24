# Write a program that creates a datetime object for November 4, 2020 , 14:53:00.
# The object created should call the strftime method with the appropriate format to display the following result:
#
# 2020/11/04 14:53:00
# 20/November/04 14:53:00 PM
# Wed, 2020 Nov 04
# Wednesday, 2020 November 04
# Weekday: 3
# Day of the year: 309
# Week number of the year: 44

from datetime import datetime

d = datetime(2020, 11, 4, 14, 53)
print(d.strftime("%Y/%m/%d %H:%M:%S"))
print(d.strftime("%y/%B/%d %H:%M:%S %p"))
print(d.strftime("%a, %Y %b %d"))
print(d.strftime("%A, %Y %B %d"))
print("Weekday", d.isoweekday())
print("Day of the year:", d.strftime("%j"))
print("Week number of the year:", d.strftime("%U"))

from datetime import time

t = time(14, 53)
print(t.strftime("%H:%M:%S"))
