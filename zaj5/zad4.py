def list_add(a, b):
    return a + b


list_a = [1, 2, 3]
list_b = [10, 11, 12]
result = list(map(list_add, list_a, list_b))
print(result)
