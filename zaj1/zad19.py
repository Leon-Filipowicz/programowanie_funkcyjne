def tuple_example(t):
    new_tuple = tuple(x * 2 for x in t)
    return new_tuple


original_tuple = (1, 2, 3, 4, 5)
result_tuple = tuple_example(original_tuple)
print(result_tuple)
