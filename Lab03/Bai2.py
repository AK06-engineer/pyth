def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(10))
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
def is_fibonacci_recursive(n, a=0, b=1):
    if b > n:
        return False
    if b == n:
        return True
    return is_fibonacci_recursive(n, b, a + b)

print(is_fibonacci_recursive(13))
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))
def sum_fibonacci(n, a=0, b=1):
    if n == 0:
        return 0
    return a + sum_fibonacci(n - 1, b, a + b)

print(sum_fibonacci(7))
import math
def sum_square_root(n):
    if n == 1:
        return math.sqrt(1)
    return math.sqrt(n) + sum_square_root(n - 1)

print(sum_square_root(5))
