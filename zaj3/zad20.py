def sum_of_squares_of_odds(numbers):
    return sum(x ** 2 for x in numbers if x % 2 != 0)


example_numbers = [1, 2, 3, 4, 5]
print(sum_of_squares_of_odds(example_numbers))
