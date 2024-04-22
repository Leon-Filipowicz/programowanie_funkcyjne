def words_start_on_a(words_list):
    return list(filter(lambda word: word.lower().startswith('a'), words_list))


def square_numbers(x):
    return x ** 2


my_words = ['ala', 'ma', 'zupe', 'kota', 'auto']

result = words_start_on_a(my_words)
print(f'Słowa na literę a : {result}')

numbers = [1, 2, 3, 4, 5]

maped_square_numbers = list(map(square_numbers, numbers))
print(maped_square_numbers)
