class S:
    __var = 12
    var = 13

    def __init__(self):
        self.__var = 10
        self.var = 11
        __var = 9
        print("Local variable", __var)

    def get_var(self):
        return self.__var


s = S()

print("Private instance variable", s._S__var)
print("Regular instance variable", s.var)
print("Private class variable", S._S__var)
print("Regular class variable", S.var)
print("Instance variable", s.get_var())
