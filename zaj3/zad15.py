def custom_sort(lst, key_fun):
    return sorted(lst, key=key_fun)


def key_func(x):
    return x % 3


print(custom_sort([3, 1, 4, 1, 5, 9], key_func))
