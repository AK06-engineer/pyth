import math

def is_perfect_square(x):
    return int(math.sqrt(x)) ** 2 == x

def is_fibonacci(n):
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

print(is_fibonacci(8))  # True
print(is_fibonacci(10)) # False
