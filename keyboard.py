from time import sleep

try:
    a = 0
    while True:
        a += 1
        print(a)
        sleep(1)
except KeyboardInterrupt:
    print("Interrupted with keyboard break...")
