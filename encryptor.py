word = input("Enter a word to be encrypted... ")
encrypted = ""

for ch in word:
    encrypted += chr(ord(ch) + 1)

print(encrypted)
