days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']


class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        if day in days_of_week:
            self.day = day
        else:
            raise WeekDayError

    def __str__(self):
        return self.day

    def add_days(self, n):
        index = days_of_week.index(self.day)
        shift = n % 7
        self.day = days_of_week[index + shift]

    def subtract_days(self, n):
        index = days_of_week.index(self.day)
        shift = n % 7
        self.day = days_of_week[index - shift]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    error = WeekDayError("Wrong Value")
    print(error)
