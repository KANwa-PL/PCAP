from math import pi

def circumference(radius):
    return round(2 * pi * radius, 2)


def area(radius):
    return round(pi * radius ** 2, 2)

print(circumference(10))
print(area(10))
