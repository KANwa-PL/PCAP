class X:
    counter = 0

    def __init__(self):
        print("New object instance created")
        X.counter += 1


for i in range(5):
    a = X()
    print("Instance count:", X.counter)
