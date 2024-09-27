# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.
#
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent

def anagram(first, other):
    cleanFirst = ""
    cleanOther = ""

    if first == "":
        if other == "":
            return -1

    for ch in first:
        if ch.isalnum():
            cleanFirst += ch.lower()

    for ch in other:
        if ch.isalnum():
            cleanOther += ch.lower()

    if sorted(cleanFirst) == sorted(cleanOther):
        return True
    else:
        return False


first = input("Enter first... ")
other = input("Enter other... ")
print("Anagrams: ", anagram(first, other))
