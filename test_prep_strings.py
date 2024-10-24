# Functions: ord(), chr()

print(chr(ord('A') + 10))

# Methods: .isxxx(), .join(), .split()

chain = "123abcXYZ"
abc = "abc"
words = "This is a sentence"
numbers = [1, 5, 9, 14, 2, 9, 8]
print(chain.isalnum())
print(abc.isalpha())
print(abc.islower())
print("-".join(chain + abc))  # Concatenate any number of strings.
print(words.split(" "))

# METHODS .sort(), sorted()
print(sorted(chain))  # STRING method returns sorted string, does not change the original
print(numbers)
numbers.sort()  # LIST method returns NONE, sorts the original numbers variable
print(numbers)

# METHODS .index(), .find(), .rfind()
print(words.index('is'))  # Returns the lowest index in S where substring sub is found
print(words.find('sentence'))  # Returns the lowest index in S where substring sub is found
print(words.rfind('is'))  # Returns the lowest index in S where substring sub is found
