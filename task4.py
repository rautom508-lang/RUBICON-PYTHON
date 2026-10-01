def greetings():
    return "hello world"

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

greetings = uppercase_decorator(greetings)

print(greetings())