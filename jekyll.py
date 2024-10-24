# asks the user for Prof. Jekyll's file name;
# reads the file contents and counts the sum of the received points for each student;
# prints a simple (but sorted) report
from os import strerror

file = ""
students = {}

try:
    file = input("Enter file name: ")
    stream = open(file, 'r')
    line = stream.readline()
    while line > "":
        name, surname, score = line.split('\t')
        student = f'{name} {surname}'
        if student in students.keys():
            students[student] += float(score)
        else:
            students.update({f'{student}': float(score)})
        line = stream.readline()
    stream.close()
except IOError as e:
    print("Error occurred while opening file: ", strerror(e.errno))
    exit()

print(dict(sorted(students.items(), key=lambda item: item[0])))
