import time


def timer(func):
    def wrapper(s):
        start_time = time.time()
        str_len = func(s)
        end_time = time.time()
        print(f"func name: {func.__name__}, total cost: {round((end_time - start_time) * 1000 * 1000, 2)} ns")
        return str_len
    return wrapper
