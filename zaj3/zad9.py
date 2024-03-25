def zip_with_index(lst):
    return list(enumerate(lst))


example_lst = ['a', 'b', 'c', 'd', 'e']

zipped = zip_with_index(example_lst)
print(zipped)
