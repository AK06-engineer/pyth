numbers = [12, 3, 7, 25, 30, 15, 21, 50, 8, 17]
odd_not_divisible_by_5 = [x for x in numbers if x % 2 == 1 and x % 5 != 0]
print(odd_not_divisible_by_5)
def is_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return b == n or n == 0

fibonacci_numbers = [x for x in numbers if is_fibonacci(x)]
print(fibonacci_numbers)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime_numbers = [x for x in numbers if is_prime(x)]
largest_prime = max(prime_numbers) if prime_numbers else None
print(largest_prime)
smallest_fibonacci = min(fibonacci_numbers) if fibonacci_numbers else None
print(smallest_fibonacci)
odd_numbers = [x for x in numbers if x % 2 == 1]
average = sum(odd_numbers) / len(odd_numbers) if odd_numbers else 0
print(average)
from functools import reduce
odd_not_div_by_3 = [x for x in numbers if x % 2 == 1 and x % 3 != 0]
product = reduce(lambda x, y: x * y, odd_not_div_by_3, 1)
print(product)
def swap_positions(lst, pos1, pos2):
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]

swap_positions(numbers, 1, 3)
print(numbers)
print(numbers[::-1])
unique_numbers = list(set(numbers))
unique_numbers.sort(reverse=True)
second_largest = unique_numbers[1] if len(unique_numbers) > 1 else None
print(second_largest)
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

total_sum_digits = sum(sum_of_digits(x) for x in numbers)
print(total_sum_digits)
count_number = numbers.count(7)  # Thay 7 bằng số cần đếm
print(count_number)
from collections import Counter
counter = Counter(numbers)
n = 2  # Số lần xuất hiện mong muốn
result = [k for k, v in counter.items() if v == n]
print(result)
most_common_number = counter.most_common(1)
print(most_common_number)
