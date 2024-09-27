# Ask the user for one line of text to encrypt;
# Ask the user for a shift value (an integer number from the range 1..25
# You should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
# Print out the encoded text

strings = input("Enter code... ")
encrypted = ""

while True:
    shift = int(input("Enter shift... "))
    if 0 < shift < 26:
        break

for i in range(len(strings)):
    asciiCode = ord(strings[i])
    if asciiCode == 32 or 48 <= asciiCode <= 57:
        encrypted += strings[i]
    elif 65 <= asciiCode <= 90:
        if asciiCode + shift > 90:
            encrypted += chr(ord("A") + (ord("Z") - asciiCode))
        else:
            encrypted += chr(asciiCode + shift)
    elif 97 <= asciiCode <= 122:
        if asciiCode + shift > 122:
            encrypted += chr(ord("a") + (ord("z") - asciiCode))
        else:
            encrypted += chr(asciiCode + shift)

print("Password: ", strings)
print("Encrypted: ", encrypted)
