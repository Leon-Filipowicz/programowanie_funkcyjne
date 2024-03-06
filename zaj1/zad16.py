def compose(f, g):
    def composed_function(x):
        return f(g(x))

    return composed_function


def double(x):
    return 2 * x


def square(x):
    return x ** 2


double_then_square = compose(square, double)
print(double_then_square(3))
