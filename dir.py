import os
from os import strerror

# Function called system executes a command passed to it as a string:

try:
    returned_value = os.system("mkdir my_first_directory")
    print(returned_value)
except IOError as e:
    print("Error!", strerror(e.errno))
