# Demonstrating the ord() function.

char_1 = 'a'
char_2 = ' '  # space
char_3 = 'ę'
char_4 = 'ź'
char_5 = 'α'

print(char_1, ' = ASCII/UTF-8', ord(char_1), ' = ', bin(ord(char_1))[2:])
print('space = ASCII/UTF-8', ord(char_2), ' = ', bin(ord(char_2))[2:])
print(char_3, ' = ASCII/UTF-8', ord(char_3), ' = ', bin(ord(char_3))[2:])
print(char_4, ' = ASCII/UTF-8', ord(char_4), ' = ', bin(ord(char_4))[2:])
print(char_5, ' = ASCII/UTF-8', ord(char_5), ' = ', bin(ord(char_5))[2:])
