# Indexing strings.

the_string = 'silly walks'

for ix in range(len(the_string)):
    print(the_string[ix], end=' ')

print()

for ix in range(len(the_string) - 1, -1, -1):
    print(the_string[ix], end=' ')

print()

for ix in range(len(the_string)):
    print(ix, end=' ')
