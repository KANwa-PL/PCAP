import math as m
import sys
from math import sqrt
from random import choice, random, seed, randint, sample
import platform as p

# Functions: ceil(), floor(), trunc(), factorial(), hypot(), sqrt()

print(m.ceil(5 / 2))  # Return the ceiling of x.
print(m.ceil(-2.3))
print(m.floor(5 / 2))  # Return the floor of x.
print(m.trunc(10 / 6))  # Truncates the Real x to the nearest Integral toward 0
print(m.factorial(5))  # x!
print(m.hypot(3, 4))  # Find the hypotenuse of a right-angled triangle where perpendicular and base are known.
print(sqrt(4))  # Find the square root


# The dir() function

class A:
    A = 0

    def __init__(self, v):
        self.__v = v


a = A(2)
print(dir(A))  # Returns the class's attributes.
print(dir("This is a Sting class representative"))  # Returns the class's attributes.
print(dir(a))  # Returns the class object's attributes.
print(dir(m))  # Returns the module's attributes.

# the sys.path variable
print(sys.path)  # A list of strings that specifies the search path for modules

# Functions: random(), seed(), choice(), sample(), randint()
seed()
print(choice((1, 5, 10)))
print(m.ceil(random() * 10))  # random() -> x in the interval [0, 1).
print(randint(0, 10))
print(sample(range(10), 4))

# Functions: platform(), machine(), processor(), system(), version(), python_implementation(), python_version_tuple()
print(p.machine())  # Returns the machine type, e. g. 'i386'
print(p.processor())  # Returns the (true) processor name
print(p.system())  # Returns the system / OS name, e. g. 'Linux', 'Windows' or 'Java'.
print(p.version())  # Returns the system's release version
print(p.python_implementation())
print(p.python_version_tuple())

# The __name__ variable
print(__name__)
