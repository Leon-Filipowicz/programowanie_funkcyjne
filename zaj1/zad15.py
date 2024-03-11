def add(x):
    def add_inner(y):
        return x + y

    return add_inner


add_part = add(3)
print(add_part(4))
