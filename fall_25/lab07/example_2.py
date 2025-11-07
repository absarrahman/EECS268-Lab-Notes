def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def calc(func, a, b):
    res = func(a, b)
    print(res)


calc(add, 1, 2)
