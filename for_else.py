list = [1, 2, 3]

for i in range(len(list)):
    if i == list[i] - 1:
        print(i - 1)
        break
    else:
        print(i)
else:
    print("No break")
