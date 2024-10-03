class Stack:
    def __init__(self):
        self.__stack = []

    def get_stack(self):
        return self.__stack

    def push(self, number):
        self.__stack.append(number)

    def pop(self):
        value = self.__stack[-1]
        del self.__stack[-1]
        return value


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum_of_values = 0

    def get_sum_of_values(self):
        return self.__sum_of_values

    def push(self, number):
        self.__sum_of_values += number
        Stack.push(self, number)

    def pop(self):
        value = Stack.pop(self)
        self.__sum_of_values -= value
        return value


my_stack = AddingStack()
print("Current stack:", my_stack.get_sum_of_values())
my_stack.push(6)
print("Current stack:", my_stack.get_sum_of_values())
my_stack.push(5)
print("Current stack:", my_stack.get_sum_of_values())
my_stack.push(4)
print("Current stack:", my_stack.get_sum_of_values())
my_stack.pop()
my_stack.pop()
print("Current stack:", my_stack.get_sum_of_values())
