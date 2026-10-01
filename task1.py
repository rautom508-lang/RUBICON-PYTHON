def square_number(n):
    return n * n

def process_list(numbers, callback):
    result = []
    for num in numbers:
        result.append(callback(num))
    return result

numbers = [1, 2, 3, 4, 5]
print(process_list(numbers, square_number))