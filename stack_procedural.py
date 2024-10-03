stack = []


def push(number):
    stack.append(number)


def pop():
    del stack[-1]


push(1)
push(1)
push(1)
print(stack)
pop()
pop()
pop()
print(stack)
