def filter_long_words(words):
    average_length = sum(len(s) for s in words) / len(words)
    return [s for s in words if len(s) > average_length]


example_words = ['jablko', 'gruszka', 'banan', 'pies', 'jeż', 'kot']

print(filter_long_words(example_words))
