try:
    x = int(input("Enter a number: "))
    y = 1 / x
except ZeroDivisionError:
    print("don't do that")
except ValueError:
    print("Enter digit")
except:
    print("I am not sure what you're trying to do... ")
print("1 / x = ", 1 / x)

try:
    print("alpha"[1 / 0])
except IndexError:
    print("index")
except ZeroDivisionError:
    print("zero")
except:
    print("some")
