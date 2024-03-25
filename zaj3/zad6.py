def map_nested(lst, func):
    return [func(x) if isinstance(x, list) else x for x in lst]


example_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(map_nested(example_lst, lambda x: x * 2))
