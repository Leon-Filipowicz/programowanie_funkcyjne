from itertools import combinations


def generated_list(elements):
    return list(combinations(elements, 2))


list1 = ['A', 'B', 'C']
for pair in generated_list(list1):
    print(''.join(pair))
