class MyRange:
    def __init__(self, mm):
        self.__i = -1
        self.__m = mm

    def __iter__(self):
        return self

    def __next__(self):
        self.__i += 1
        if self.__i >= self.__m:
            raise StopIteration
        if self.__i == 0:
            return 0
        ret = self.__i
        return ret


for i in MyRange(10):
    print(i)
