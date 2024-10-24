# The following logic is applied to question numbers:
# Question: {question_number}/{test_number}

# Question: 1/1
# What is the output of the following snippet of code?


class A:
    var = 100

    def __init__(self):
        pass


a = A()
print(a.__dict__)  # prints out {}


# Question 2/1
# What is the output of the following snippet of code?


def func(a):
    print(a)


# func() returns TypeError: func() missing 1 required positional argument: 'a'


# Question 3/1
# Which of the following is the correct way to open a file in read mode? (Select 2 Answers)

a = open('histogram.txt')
b = open('histogram.txt', 'r')


# Question 4/1
# Given the following snippet of code:

class A:
    pass


class B(A):
    pass


# How are the two classes, A and B, related? (Select 2 Answers)
# A is super class of B
# B is sub class of A

# Question 5/1
# What is the output of the following snippet of code?

c = "ab cd"
print('*'.join(c.split()))  # splits on whitespace, discards empty strings, joins with '*', so ab*cd

# Question 6/1
# What is true about string comparison in Python? (Select 3 Answers)
# Numbers have lower code point than capital letters
# Comparison ends when a character with higher code point is found as compared to the code point value of character at same index in the second string
# Strings are compared character by character from left to right

# Question 7/1
# What is the output of the following snippet of code?

import math as m

print(m.ceil(-2.3) + m.factorial(3))

# Question 8/1
# What is the output of the following code snippet? (Select 2 Answers)

print(ord('c'))
# The output is a Unicode code point
# The output will be an integer

# Question 9/1
# What is the output of the following snippet of code:

d = "refrigerator"
print(d.find('e'))

# Question 10/1
# file = open('abc.txt', 'w')
# file.close()
file = open('abc.txt')
print(file.read())
file.close()


# Question 11/1
# If the following piece of code resides inside the abc.py file, what is the output when the file is run?

class A:
    pass


print(A.__module__)

# Question 12/1
# The fact that the following snippet of code throws an Attribute error depicts which phenomena of OOP?
# Encapsulation

# Question 13/1
# Correct way to import

# Question 14/1
# Output?

e = "abc"

for i in e:
    e += 'z'

print(e)

# Question 15/1
# What is the output of the following snippet of code:

f = "television"
print(f.find('Vision'))  # prints -1.


# Question 16/1
class A:
    def func(self):
        return "A"


class B:
    def func(self):
        return "B"


class C(B, A):
    pass


c = C().func()
print(c)

# Question 17/1
# Which of the following is a valid string?
# print("Looks can be /"deceiving/"") # This is incorrect. Escape character requires '\' instead of '/'.
# print(""""""")
print('Hi, "Friend" is this valid?')


# Question 18/1
class MyException(Exception):
    pass


try:
    raise MyException("A", "B")
except MyException as e:
    print(e.args)  # Returns a tuple whose len is 2.


# Question 19/1
# What is true about __init__.py file? (Select 2 Answers)
# __init__.py allows you to define any variable at package level
# Files named __init__.py are used to mark directories on disk as Python package directories

# Question 20/1
# Which of the following is a true statement? (Select 2 Answers)
# ASCII is a subset of UTF-8
# ASCII stands for American Standard Code for Information Exchange

# Question 21/1
# What is True about the following snippet?

class A:
    var = 10

    def __init__(self, a=1):
        self.__var = a


a = A(5)
print(a._A__var)  # Outputs 5. This is true for all private properties of class objects.
print(A.var)  # Accessing class variable

# Question 22/1
# What is the output of the following snippet of code in abc.py file?

file = open('abc.txt')
print(file.read(4))

# Question 23/1
file = open('abc.txt')
g = [i for i in file]
print(g)  # Prints out ['abc\n', 'def\n', 'ghi']


# Question 24/1
# Which are true?

class A:
    var = 1

    def __init__(self):
        self.x = 1


class B(A):
    def __init__(self):
        super().__init__()


b = B()

print(hasattr(b, '__init__'))
print(hasattr(B, '__init__'))


# Question 25/1
class A:
    pass


class B(A):
    pass


class C(B):
    pass


c = C()
print("isInstance:", isinstance(c, A))

# Question 26/1
h = "abcdef"
# h[1] = 'x' # TypeError: 'str' object does not support item assignment
print(h)

# Question 27/1
# Which of the following evaluates to True? (Select 2 Answers)
print("abc" > "Abc")
print("abc" < "abcd")

# Question 28/1
# Expected output is?
# Answer: 1.0 SAFE DONE ERROR DONE
for i in range(1, -1, -1):
    try:
        print(1 / i, end=' ')
    except:
        print("ERROR", end=' ')
    else:
        print("SAFE", end=' ')
    finally:
        print("DONE", end=' ')

# Question 29/1
# Which of the following lines of code can be used to get the python version being used?
import platform as p

print(p.python_version())

# Question 30/1
a = "abcdef"
b = a[-3:-1]
print(b)

# Question 31/1
print("2223".isdecimal())
print("23".isdigit())


# Question 32/1
# What is true about the variable 'var' in the following class? (Select 2 Answers)
class A:
    var = 10

    def __init__(self):
        pass


# Question 33/1
# What is true about __pycache__? (Select 2 Answers)

# Question 34/1
# Prints first three characters from the first line as '3' acts as a 'limit' parameter.
file = open('abc.txt')
print(file.readline(3))

# Question 35/1
# What is the output of the following snippet of code?

a = [1, 2, 3, 4, 5, 6]
b = list(filter(lambda x: x % 2 == 0, a))
print(b)

# Question 36/1
import random as r

print(r.choice([1, 2, 3]))

# Question 37/1
# What is the output of the following snippet of code?
print(C.__bases__)  # prints out a TUPLE of superclasses in order

# Question 38/1
# dir function?
print(dir(m))  # prints a LIST of all entries


# Question 39/1
# What is the output of the following snippet of code?

def Z(a):
    b = a ** 2
    print("Outer 'b':", b)

    def X(b):
        print("Inner 'b':", b)
        return b + 3

    return X


x = Z(3)
print(x(2))

# Question 40/1
# Which of the following statements are correct about the sys.path variable? (Select 2 Answers)
# The sys.path variable is mutable
# The sys.path variable is a list of strings


# Question 3/2
# r.seed(0)
# Note: If you use the same seed value twice you will get the same random number twice. See example:

r.seed(0)
print("LOOP SEED:")
for i in range(4):
    print(r.random())

r.seed(0)
print("OUTSIDE LOOP SEED:")
print(r.random())
print(r.random())
print(r.random())
print(r.random())


# Question 4/2
# What is the expected output?

class R:
    def __init__(self):
        self.__r = 100

    def get_r(self):
        return self.__r


rrr = R()
rrr.__r = 10  # Instance variable
print(rrr.get_r())  # Private instance variable
print(rrr._R__r)  # Private instance variable
print(rrr.__r)

# Queston 5/2
# What is the expected output?
try:
    pass
    # print(1 / 0) # Unhandled ZeroDivisionError exception
except TypeError as e:
    print("Hi!", end=" ")
finally:
    print("Bye!")

# Question 8/2
file = open('xyz.txt', 'w')
a = [1, 2, 3, 4, 5]
for i in a:
    file.write(str(f'{i}\n'))


# Question 14/2
def A(a):
    b = a ** 3
    print("Outer 'b':", b)

    def B():
        print("Inner 'b':", b)
        return b + 2

    return B


x = A(2)
print(x())


def Z(a):
    b = a ** 2
    print("Outer 'b':", b)

    def X(b):
        print("Inner 'b':", b)
        return b + 3

    return X


x = Z(3)
print(x(2))

# Question 16/2
# What is the output of the following snippet of code?

a = "abcdef"
b = a[-1:-4]
c = a[-1:-4:-1]
print(b)  # 'b' is set to an empty string, because there's no 'step' parameter in the slice.
print(c)  # 'c' is set to 'fed' string, because of the negative 'step'

# Question 18/2
# Both file1.py and file2.py are in the same directory.
# Content of file1.py is:
# print(__name__)
# Content of file2.py is:
# import file1
# What is the output when file2.py is run?

# The output is 'file1'.
# The '__name__' variable gets its value depending on how we execute the file.
# It's either file name, like 'file1' (import) or '__main__' (simple run).

# Question 27/2
file = open('abc.txt')
print(file.read(5))  # This read method reads 5 bytes of data, so the first four characters and '\n'.
file.close()


# Question 29/2
# __dict__ method exists on class and instance levels.
# A.__dict__ returns a non-empty dictionary with all the items assigned to the class
# n.__dict__ returns an empty dictionary as there's nothing assigned in the constructor
class A:
    pass


n = A()
print(A.__dict__)
print(n.__dict__)


# Question 31/2
# What is the output of the following snippet of code?

class T:
    pass


class R(T):
    pass


class S(R):
    pass


s = S()
print(isinstance(s, (R, A, T,
                     B)))  # Returns 'True' if the object specified in first argument is an instance of the class or tuple of classes specified in the second argument.
# The check is an 'OR' relation NOT an 'AND' relation

# Question 36/2
# What is the output?

stringsy = "abcd"


# del stringsy[1] TypeError: 'str' object doesn't support item deletion as 'string' is immutable


# Question 40/2
class V:
    def func():
        print("Hello from class 'V'!")


v = V()
# v.func() # TypeError: func() takes 0 positional arguments but 1 was given
V.func()


# Question 6/3
# What is true about '__Test' in the following snippet of code?
# It's a private method.

class A:
    def __init__(self):
        pass

    def __Test(self):
        pass


# Question 8/3
a = "television"
# print(a.index('Vision'))  # ValueError: substring not found
print(a.find('Vision'))  # returns -1

# Question 23/3
# sample() returns a list.
import random as r

print(r.sample([1, 2, 3], 1))  # Chooses k unique random elements from a population sequence or set.

# Question 33/3
mm = "zxkoa"
mmm = sorted(mm)
