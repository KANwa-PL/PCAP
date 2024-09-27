# Your task is to write your own function:
# it should return a list of words created from the string,
# the string should be divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;


def mysplit(s):
    '''
    Custom split function.
    :param s:
    :return:
    '''
    ls = []
    lw = ""
    for ch in s:
        if ch.isspace():
            if len(lw) == 0:
                continue
            else:
                ls.append(lw)
                lw = ""
        else:
            lw += ch
    return ls


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
