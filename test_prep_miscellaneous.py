# list comprehensions: the if operator, nested comprehensions
c = [i ** 2 for i in range(5)]
print(c)

d = tuple([i for i in range(21) if i % 2 == 0 and i != 0])
print(d)

# Lambdas: defining and using lambdas
e = list(map(lambda x: x * 2, c))
f = list(filter(lambda x: x > 10, d))
print(e)
print(f)


# Closures: meaning, rationale, defining and using
def r():
    a = 1

    def s():
        nonlocal a
        a += 1
        return a * 4

    return s


g = r()
print(g(), g())
