def analyze_data(data):
    if isinstance(data, list):
        print("To jest lista.")
        print("Ilość elementów:", len(data))
    elif isinstance(data, tuple):
        print("To jest krotka.")
        print("Ilość elementów:", len(data))
    else:
        print("To nie jest ani lista, ani krotka.")


analyze_data([1, 2, 3])
analyze_data((1, 2, 3, 4))
analyze_data(100)
