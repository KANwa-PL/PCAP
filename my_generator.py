# This generator produces the first n powers of 2:

def power_of_2_generator(nn: int):
    try:
        for ii in range(int(nn)):
            yield 2 ** ii
    except ValueError:
        print("Use integer value!")


for i in power_of_2_generator(12):
    print(i)
