def recursive_sum(numbers):
    if isinstance(numbers, list):
        return sum(numbers) + sum([recursive_sum(n) for n in numbers])
    else:
        return numbers


example_numbers = [1, 2, 12, 121, 21, 9]

print(recursive_sum(example_numbers))
