import functools
import operator

numbers = [2, 5, -2, 0, 10, -15]
big_number = functools.reduce(lambda x, y: x if x > y else y, numbers)
print(f'Największa liczba to: {big_number}')

numbers_for_avg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
avg_numbers = functools.reduce(lambda x, y: x + y, numbers_for_avg) / len(numbers_for_avg)
print(avg_numbers)
