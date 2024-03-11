def tuple_example(t):
    new_tuple = tuple(x * 2 for x in t)
    return new_tuple


tuple1 = (1, 2, 3, 4, 5)
last_tuple = tuple_example(tuple1)
print(last_tuple)
