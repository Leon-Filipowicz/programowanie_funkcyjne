from functools import partial


def add(x, y):
    return x + y


add_5 = partial(add, y=5)
print(add_5(10))
