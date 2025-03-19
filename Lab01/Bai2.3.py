def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def danh_sach_nguyen_to(a, b):
    return [n for n in range(a, b+1) if is_prime(n)]

print(danh_sach_nguyen_to(10, 50))
