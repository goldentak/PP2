import functools

def multiply_list(numbers):
    return functools.reduce(lambda x, y: x * y, numbers)

nums = [1, 2, 3, 4, 5]
result = multiply_list(nums)
print("Product of numbers:", result)
