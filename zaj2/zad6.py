def safe_function(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None

    return wrapper


@safe_function
def divide(a, b):
    return a / b


print(divide(2, 1))
print(divide(5, 0))
print(divide(0, 0))

