def decor(func):
    def inner(a, b):
        print('enter decorator ')
        res = func(a, b)
        print('exit decorator ')
        return res
    return inner


def decor2(func):
    def inner(*args):
        print('enter decorator ')
        res = func(*args)
        print('exit decorator ')
        return res
    return inner


@decor2
def add(a, b):
    print(a + b)
    # return c


add(2, 3)
