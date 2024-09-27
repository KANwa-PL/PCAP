# Ask the user her/his birthday (in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY)
# Outputs the Digit of Life for the date.


def get_digit_of_life(string_of_digits):
    digit_of_life = 0
    auxiliary = 0

    for digit in string_of_digits:
        digit_of_life += int(digit)

    while True:
        if digit_of_life > 9:
            for digit in str(digit_of_life):
                auxiliary += int(digit)
            digit_of_life = auxiliary
            auxiliary = 0
        else:
            break

    return digit_of_life


while True:
    birthdate = input("Enter your birthday in the format YYYYMMDD, or YYYYDDMM, or MMDDYYYY... ")
    if birthdate == 'Q':
        break
    print("Digit of life: ", get_digit_of_life(birthdate))
    print("Enter 'Q' to quit...")
