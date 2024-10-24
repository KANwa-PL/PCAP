from os import strerror
from random import randint

bytes_of_numbers = bytearray(10)

for number in range(len(bytes_of_numbers)):
    bytes_of_numbers[number] = 10 + randint(0, number)

try:
    stream = open('file.bin', 'wb')
    stream.write(bytes_of_numbers)
    stream.close()
except IOError as e:
    print("Error occurred:", strerror(e.errno))

try:
    bf = open('file.bin', 'rb')
    bytes = bf.read(10)
    print(bytes)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
