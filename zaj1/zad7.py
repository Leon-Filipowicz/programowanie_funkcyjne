words = ["auto", "autobus", "rower", "hulajnoga", "samolot"]
long_words = list(filter(lambda x: len(x) > 5, words))
print(long_words)
