'''Some of the methods offered by strings are:

capitalize() – changes all string letters to capitals;
center() – centers the string inside the field of a known length;
count() – counts the occurrences of a given character;
join() – joins all items of a tuple/list into one string;
lower() – converts all the string's letters into lower-case letters;
lstrip() – removes the white characters from the beginning of the string;
replace() – replaces a given substring with another;
rfind() – finds a substring starting from the end of the string;
rstrip() – removes the trailing white spaces from the end of the string;
split() – splits the string into a substring using a given delimiter;
strip() – removes the leading and trailing white spaces;
swapcase() – swaps the letters' cases (lower to upper and vice versa)
title() – makes the first letter in each word upper-case;
upper() – converts all the string's letter into upper-case letters.

2. String content can be determined using the following methods (all of them return Boolean values):

endswith() – does the string end with a given substring?
isalnum() – does the string consist only of letters and digits?
isalpha() – does the string consist only of letters?
islower() – does the string consists only of lower-case letters?
isspace() – does the string consists only of white spaces?
isupper() – does the string consists only of upper-case letters?
startswith() – does the string begin with a given substring?
'''

alphabet = "bcdefghijklmnopqrstuvwxy"

print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)

# We're copying the contents of 'alphabet' into a new variable here:
alphabet = 'a' + alphabet
alphabet = alphabet + 'z'
alphabet = alphabet + 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# The following lines print 'A' and 'z' respective to their ASCII codes:
print(min(alphabet))
print(max(alphabet))

# Demonstrating the index() method. It returns the index of the first occurrence of the argument:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Demonstrating the find() method:
# It returns the index or -1.
print("Finding TA in ETA: ", "Eta".find("Eta"))
print("Finding MMMA in ETA: ", "Eta".find("mma"))

# Demonstrating the list() function:
print(list("abcabc"))

# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demonstrating the capitalize() method.
# It capitalizes the first character (if possible) and lowers the case of the remaining characters:
print('aBcD'.capitalize())
print('12aBcD'.capitalize())
print('BaBcD'.capitalize())

# Demonstrating the center() method:
print('[' + 'alpha'.center(11) + ']')

# Demonstrating the endswith() method:
if "epsilon".endswith("sil"):
    print("yes")
else:
    print("no")

# Demonstrating the isalnum() method:
print("Demonstrating the isalnum() method:")
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
print(' '.isalnum())
t = 'Six lambdas'
print(t.isalnum())
t = 'ΑβΓδ'
print(t.isalnum())
t = '20E1'
print(t.isalnum())

# Demonstrating the isalpha() method:
print("Demonstrating the isalpha() method:")
print("Moooo".isalpha())
print('Mu40'.isalpha())

# Demonstrating the isdigit() method:
print("Demonstrating the isdigit() method:")
print('2018'.isdigit())
print("Year2019".isdigit())

# Demonstrating the islower() method:
print("Demonstrating the islower() method:")
print("Moooo".islower())
print('moooo'.islower())

# Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

# Demonstrating the join() method:
print("Demonstrating the join() method:")
print(" new ".join(["omicron", "pi", "rho"]))

# Demonstrating the lower() method:
print("SiGmA=60".lower())

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
print("www.cCisco.com".lstrip("w.c"))

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# alphabet.append('A') results in AttributeError: 'str' object has no attribute 'append'
# alphabet.insert(0, 'A') results in AttributeError: 'str' object has no attribute 'insert'

# del alphabet[0] results in TypeError as 'str' object doesn't support item deletion...
del alphabet  # is fine though. It just removes the whole string.
