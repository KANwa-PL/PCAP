# except, except:-except, except:-else:, except (e1, e2)
# Self-defined exceptions

class MyException(BaseException):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


try:
    print("This part can raise 'IOError' exception and we want to catch it.")
except IOError as e:
    print("IOError Exception")
else:
    try:
        print("This 'else' will be executed only if there's no error in #4")
        raise MyException("MyException")
    except MyException as e:
        print("Exception: ", e)
finally:
    print("This will always be executed!")
