def remove_duplicates(words):
    return list(dict.fromkeys(words))


example_words = ['a', 'b', 'b', 'c', 'd', 'e', 'e']

print(remove_duplicates(example_words))
