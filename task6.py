def safe_divide(func):
    def wrapper(a, b):
        if b == 0:
            return "Error: Cannot divide by zero!"
        return func(a, b)
    return wrapper

@safe_divide
def divide(a, b):
    return a / b

print(divide(10, 2))
print(divide(10, 0))
