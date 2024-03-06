from functools import partial


def multiply(x, y):
    return x * y


multiply_by_3 = partial(multiply, y=3)
print(multiply_by_3(5))
