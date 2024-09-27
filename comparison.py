# Sorting strings is done lexicographically, which means you compare character-wise from the beginning.
# The reason why '11' > '8' yields False is based on the per-character comparison:
# 1 has a smaller ASCII value than 8, so the following characters are ignored.
# If these characters happen to be equal, the next characters are compared.
# In this special case, where one is the beginning (prefix) of the other, the shorter one is considered "smaller".
# ('foot' < 'football').

# '11' has no single ASCII value, since it is composed of two characters:
# '1' (ASCII value 49) and '1' (ASCII value 49).


jeden = '1'
osiem = '8'

print(jeden == osiem)  # False
print(jeden != osiem)  # True
print(jeden < osiem)  # True
print(jeden > osiem)  # False
print(jeden <= osiem)  # True
print(jeden >= osiem)  # False
print()

jedenaście = '11'

print(jedenaście == osiem)  # False
print(jedenaście != osiem)  # True
print(jedenaście < osiem)  # True
print(jedenaście > osiem)  # False
print(jedenaście <= osiem)  # True
print(jedenaście >= osiem)  # False
