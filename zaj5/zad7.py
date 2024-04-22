def function_1(x):
    return x ** 2


def function_2(x):
    return x + 5


def function_sum(x):
    return function_2(function_1(x))


numbers = [1, 2, 3, 4, 5]
result = list(map(function_sum, numbers))
print(result)
