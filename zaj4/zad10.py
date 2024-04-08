from itertools import permutations


def generate_permutations(lst):
    return list(permutations(lst))


data = [1, 2, 3]

print(generate_permutations(data))
