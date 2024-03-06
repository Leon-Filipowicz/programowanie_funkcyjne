def add(x):
    def add_inner(y):
        return x + y

    return add_inner


add_partial = add(3)
print(add_partial(4))
