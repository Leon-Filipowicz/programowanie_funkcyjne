import itertools

list1 = ['A', 'B']
list2 = ['C', 'D']
generated_list = []

generated_list += itertools.product(list1, list2, repeat=1)
for pair in generated_list:
    print(''.join(pair))
