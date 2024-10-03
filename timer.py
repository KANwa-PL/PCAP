# Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from range [0..23]
# We will be using the military time), minutes (from range [0..59]) and seconds (from range [0..59]).
#
# Zero is the default value for all of the above parameters.
# There is no need to perform any validation checks.
#
# The class itself should provide the following facilities:
#
# Objects of the class should be "printable"
# They should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss",
# with leading zeros added when any of the values is less than 10;

# The class should be equipped with parameterless methods called next_second() and previous_second()
# Incrementing the time stored inside objects by +1/-1 second respectively.


def stringify_timer_object(class_object):
    time = ""
    for name in class_object.__dict__.keys():
        value = str(getattr(class_object, name)).zfill(2)
        time += value
        time += ":"
    return time[:-1]


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return stringify_timer_object(self)

    def next_second(self):
        if self.__seconds == 59:
            self.__seconds = 0
            self.__minutes += 1
        else:
            self.__seconds += 1

        if self.__minutes == 60:
            self.__minutes = 0
            self.__hours += 1

        if self.__hours == 24:
            self.__hours = 0

    def prev_second(self):
        if self.__seconds == 0:
            self.__seconds = 59
            self.__minutes -= 1
        else:
            self.__seconds -= 1

        if self.__minutes == -1:
            self.__minutes = 59
            self.__hours -= 1

        if self.__hours == -1:
            self.__hours = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
