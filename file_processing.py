from os import strerror

# Safe approach, cause you're reading just one character at a time.
# Character-by-character file processing...
try:
    s = open("./tzop.txt", "r", encoding="utf-8")
    counter = 0
    ch = s.read(1)
    while ch != "":
        print(ch, end='')
        counter += 1
        ch = s.read(1)
    print("Total characters: ", counter)
    s.close()
except IOError as e:
    print("Exception occurred:", strerror(e.errno))

# Risky approach if you don't know the file size
# Processing a file as a whole / loading the whole file into the buffer:
try:
    s = open('tzop.txt', "r")
    contents = s.read()
    counter = 0
    for ch in contents:
        print(ch, end="")
        counter += 1
    print("Total Characters: ", counter)
    s.close()
except IOError as exc:
    print("Exception occurred: ", strerror(exc.errno))

# Another approach is reading a file line by line.
try:
    print("\nReading a text file line by line:")
    stream = open("tzop.txt", "rt")
    line = stream.readline()
    lines = 0
    characters = 0
    while line != "":
        lines += 1
        for ch in line:
            print(ch, end='')
            characters += 1
        line = stream.readline()
    stream.close()
    print("Total lines read: ", lines)
    print("Total characters read: ", characters)
except UnicodeDecodeError as another_exception:
    print("UnicodeDecodeError")
except IOError as my_exception:
    print("Exception occurred: ", strerror(my_exception.errno))

# Showing that open method actually returns an iterable object...
try:
    print("\nStream is an iterable:")
    for line in open("tzop.txt", "rt"):
        for ch in line:
            print(ch, end='')
except IOError as e:
    print("Exception occurred: ", strerror(e.errno))
