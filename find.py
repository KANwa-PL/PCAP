# Write a function or method called find.
# The function takes two arguments called path and dir.
# The path argument should accept a relative or absolute path to a directory where the search should start.
# The dir argument should be the name of a directory that you want to find in the given path.
# Your program should display the absolute paths if it finds a directory with the given name.
# The directory search should be done recursively.
# This means that the search should also include all subdirectories in the given path.

import os
from os import mkdir


def find(path, file):
    try:
        for root, dirs, files in os.walk(path):

            for d in dirs:
                if d == file:
                    print("".join(("..", root, "/", d)))
            for f in files:
                if f.find(file) == 0:
                    print("".join(("..", root, "/", f)))
    except FileExistsError as e:
        print(e)


def tree_prep():
    counter = 0
    folders = ["./tree",
               "./tree/c",
               "./tree/c/other_courses",
               "./tree/c/other_courses/cpp",
               "./tree/c/other_courses/python",
               "./tree/cpp",
               "./tree/cpp/other_courses",
               "./tree/cpp/other_courses/c",
               "./tree/cpp/other_courses/python",
               "./tree/python",
               "./tree/python/other_courses",
               "./tree/python/other_courses/c",
               "./tree/python/other_courses/cpp"]

    for folder in folders:
        try:
            mkdir(folder)
            counter += 1
            if counter == len(folders):
                break
        except FileExistsError as e:
            pass


tree_prep()
find("./tree", "python")
