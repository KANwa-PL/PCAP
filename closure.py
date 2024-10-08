def outer(parameter):
    local = parameter

    def inner():
        return local

    return inner

    
var = 2
fun = outer(var)
print(fun())
