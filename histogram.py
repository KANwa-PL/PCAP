# Your task is to write a program which:
#
# asks the user for the input file's name;
# reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
# prints a simple histogram in alphabetical order (only non-zero counts should be presented)
from audioop import reverse
from os import strerror

characters = {}
file = ""

try:
    file = input("Enter file name: ")
    stream = open(file, 'r')
    line = stream.readline()
    while line > "":
        for ch in line:
            if not ch.isalpha():
                continue
            ch = ch.lower()
            if ch in characters.keys():
                characters[ch] += 1
            else:
                characters.update({f'{ch}': 1})
        line = stream.readline()
    stream.close()
except IOError as e:
    print("Error occurred while opening file: ", strerror(e.errno))

try:
    stream = open(f'{file}.hist', 'wt')
    sorted_characters = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    for key, value in sorted_characters.items():
        stream.write(f'{key} --> {value} \n')
    stream.close()
except IOError as e:
    print("Error occurred while opening file: ", strerror(e.errno))
