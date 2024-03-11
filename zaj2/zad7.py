from itertools import groupby

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_even(number):
    return number % 2 == 0


group = groupby(numbers, key=is_even)

for key, group in group:
    group_list = list(group)
    print(f'{'Even' if key else 'Odd'} numbers: {group_list}')
