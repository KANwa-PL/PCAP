def outer(parameter):
    local = parameter

    def inner():
        return local

    return inner


fun = outer(2)
print(fun())
