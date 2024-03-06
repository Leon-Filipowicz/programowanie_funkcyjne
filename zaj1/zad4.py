import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(execution_time)
        return result

    return wrapper


@timeit
def example():
    time.sleep(1)


example()
