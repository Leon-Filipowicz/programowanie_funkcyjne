def compose(f, g):
    def composed_func(x):
        return f(g(x))

    return composed_func


def double(x):
    return 2 * x


def square(x):
    return x ** 2


double_square = compose(square, double)
print(double_square(3))
