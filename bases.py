class Super():
    pass


class SuperSuper():
    pass


class Subclass(Super, SuperSuper):
    pass


def print_bases(cls):
    for i in cls.__bases__:
        print(i.__name__)


print_bases(Super)
print_bases(SuperSuper)
print_bases(Subclass)
