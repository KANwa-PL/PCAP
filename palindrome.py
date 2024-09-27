# assume that an empty string isn't a palindrome;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check - treat them as non-existent;
# there are more than a few correct solutions - try to find more than one.

def isPalindrome(pld):
    cleanPld = ""

    for ch in pld:
        if ch.isalnum():
            cleanPld += ch.lower()
        else:
            continue
    if cleanPld == "":
        return False
    return cleanPld == cleanPld[::-1]


palindrome = input("Enter palindrome... ")
print("isPalindrome: ", isPalindrome(palindrome))
