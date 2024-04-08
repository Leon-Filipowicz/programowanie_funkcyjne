def apply_function_to_tuples(lst, func):
    return [func(*tup) for tup in lst]


def square_function(x, y):
    return x ** 2, y ** 2


data = [(1, 2), (3, 4), (5, 6)]

print(apply_function_to_tuples(data, square_function))
