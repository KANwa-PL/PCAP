# This program is able to simulate the work of a seven-display device

from digits import digit

while True:
    user_input = input("Enter digits... Enter 'Q' to quit... ")
    if user_input == 'Q':
        break
    digit(user_input)
