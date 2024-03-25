def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


for n in generate_fibonacci():
    if n > 1000:
        break
    print(n)
