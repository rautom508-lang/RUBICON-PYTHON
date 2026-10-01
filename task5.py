def log_execution(func):
    def wrapper(*args, **kwargs):
        print("Starting execution...")
        result = func(*args, **kwargs)
        print("Finished execution.")
        return result
    return wrapper

@log_execution
def add_numbers(a, b):
    return a + b

print(add_numbers(5, 7))