# Create a class called MyCalendar that extends the Calendar class
# Create the count_weekday_in_year method with the year and weekday parameters.
# The weekday parameter should be a value between 0-6, where 0 is Monday and 6 is Sunday.
# The method should return the number of days as an integer;
# In your implementation, use the monthdays2calendar method of the Calendar class.
from calendar import Calendar


class MyCalendar(Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for m in range(12):
            for w in Calendar.monthdays2calendar(self, year=year, month=m + 1):
                for d in w:
                    if d[1] == weekday and d[0] != 0:
                        count += 1
        return count


c = MyCalendar()
print(c.count_weekday_in_year(2019, 0))
print(c.count_weekday_in_year(2020, 5))
print(c.count_weekday_in_year(2000, 6))
