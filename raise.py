# if the user enters a string that is not an integer value,
# the function should emit the message Error: wrong input, and ask the user to input the value again;

def read_int(prompt, min, max):
    while True:
        try:
            value = int(input(prompt))
            if min <= value <= max:
                return value
            else:
                print("Error: the value is not within permitted range (min..max)")
        except ValueError:
            print("Error: wrong input")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
