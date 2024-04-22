def suma(a, b):
    return a + b


def print_global():
    print("Global variable value:", global_variable)


operation1 = suma
result = operation1(3, 4)
print(result)

global_variable = 42

print_global()
