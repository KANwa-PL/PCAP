import math

while True:
    try:
        x = float(input("Enter x: "))
        y = math.sqrt(x)
        print("The square root of", x, "equals", round(y, 2))
        break
    except ValueError:
        print("Enter a positive number.")
