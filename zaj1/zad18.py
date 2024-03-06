def even_numbers():
    num = 0
    while True:
        yield num
        num += 2


generator = even_numbers()

for _ in range(5):
    print(next(generator))
