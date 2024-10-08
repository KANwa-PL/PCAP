from os import strerror

try:
    entry_stream = open('file.bin', 'rb')
except IOError as error:
    print('Error:', strerror(error.errno))
    exit(error.errno)

try:
    exit_stream = open('another_file.bin', 'wb')
except IOError as error:
    print('Error:', strerror(error.errno))
    exit(error.errno)

buffer = bytearray(8)

try:
    readin = entry_stream.readinto(buffer)
    loops = 0
    while readin > 0:
        loops += 1
        exit_stream.write(buffer[:readin])
        readin = entry_stream.readinto(buffer)
    print("Loops:", loops)
except IOError as error:
    print("Error: ", error.errno)

entry_stream.close()
exit_stream.close()
