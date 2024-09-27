line = input('Enter digits separated with spaces... ')
digits = line.split()
sum_of_numbers = 0

for digit in digits:
    try:
        sum_of_numbers += float(digit)
    except ValueError:
        sum_of_numbers += 0

print("Sum of numbers: ", sum_of_numbers)
