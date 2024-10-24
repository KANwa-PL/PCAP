# I/O modes
# • predefined streams
# • handles vs. streams
# • text vs. binary modes
from os import strerror

d = {}

try:
    stream = open('histogram.txt', 'rt')
    for line in stream:
        for ch in line:
            if ch.isalpha():
                if ch in d.keys():
                    d[ch] += 1
                else:
                    d.update({f'{ch}': 1})
    stream.close()
except IOError as e:
    print("Error while opening file: ", strerror(e.errno))
finally:
    print(sorted(d.items()))
