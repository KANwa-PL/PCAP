# Your task is to write a program which answers the following question:
# Are the characters comprising the first string hidden inside the second string?
#
# For example:
# if first string is 'dog'
# if the second string is given as "vcxzxduybfdsobywuefgas", the answer is yes;
# if the second string is "vcxzxdcybfdstbywuefsas", the answer is no (as there are neither the letters "d", "o", or "g", in this order)

def word_search(first, second):
    second = second.lower()
    first = first.lower()
    for ch in first:
        if second.find(ch) == -1:
            return 'No'
    return 'Yes'


first = input("First word... ")
second = input("Second word... ")
print(word_search(first, second))
