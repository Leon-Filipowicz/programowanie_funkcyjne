def rotate_list(lst, steps):
    steps = steps % len(lst)
    return lst[-steps:] + lst[:-steps]


print(rotate_list([1, 2, 3, 4, 5], 2))
