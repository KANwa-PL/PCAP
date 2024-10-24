class C():
    pass


class A(C):
    def __init__(self):
        self.__a = 1
        self.c = 1

    def set_a(self, a):
        self.__a = a


def update(class_variable):
    B.class_variable = class_variable


class B(A):
    class_variable = ""

    def __init__(self):
        super().__init__()
        self.instance_variable = "INSTANCE VARIABLE"
        B.class_variable += "CLASS VARIABLE"
        local_method_variable = "LOCAL METHOD VARIABLE"
        print(local_method_variable)


b = B()
a = A()
print(B.__dict__)
print(b.__dict__)
b.set_a(4)
b.c = 5
print(b.__dict__)
update("NEW VALUE")
print(B.__dict__)
print(b.__dict__)
print(hasattr(a, "__a"))
print(B.__bases__)
print(B.__module__)
print(A.__bases__)
print(A.__module__)
