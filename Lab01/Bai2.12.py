def so_le_khong_chia_het_cho_5(arr):
    return [x for x in arr if x % 2 != 0 and x % 5 != 0]

arr = [1, 3, 5, 7, 9, 10, 15, 17, 19]
print(so_le_khong_chia_het_cho_5(arr))
def so_fibonacci_trong_ds(arr):
    def is_fibonacci(n):
        x1 = 5 * n * n + 4
        x2 = 5 * n * n - 4
        return int(x1**0.5)**2 == x1 or int(x2**0.5)**2 == x2
    
    return [x for x in arr if is_fibonacci(x)]

arr = [1, 2, 3, 4, 5, 8, 13, 21, 34, 50]
print(so_fibonacci_trong_ds(arr))
def so_nguyen_to_lon_nhat(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    so_nguyen_to = [x for x in arr if is_prime(x)]
    return max(so_nguyen_to) if so_nguyen_to else "Không có số nguyên tố"

arr = [10, 23, 45, 67, 89, 91]
print(so_nguyen_to_lon_nhat(arr))
def so_fibonacci_be_nhat(arr):
    fibonacci_numbers = so_fibonacci_trong_ds(arr)
    return min(fibonacci_numbers) if fibonacci_numbers else "Không có số Fibonacci"

arr = [10, 1, 2, 3, 5, 8, 34]
print(so_fibonacci_be_nhat(arr))
def trung_binh_so_le(arr):
    so_le = [x for x in arr if x % 2 != 0]
    return sum(so_le) / len(so_le) if so_le else 0

arr = [1, 2, 3, 4, 5, 7, 9]
print(trung_binh_so_le(arr))
def tich_so_le_khong_chia_cho_3(arr):
    tich = 1
    found = False
    for x in arr:
        if x % 2 != 0 and x % 3 != 0:
            tich *= x
            found = True
    return tich if found else 0

arr = [1, 2, 3, 4, 5, 7, 9]
print(tich_so_le_khong_chia_cho_3(arr))
def doi_cho(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr

arr = [1, 2, 3, 4, 5]
print(doi_cho(arr, 1, 3))
def dao_nguoc(arr):
    return arr[::-1]

arr = [1, 2, 3, 4, 5]
print(dao_nguoc(arr))
def so_lon_thu_nhi(arr):
    arr = list(set(arr))  # Loại bỏ số trùng lặp
    arr.sort(reverse=True)
    return arr[1] if len(arr) > 1 else "Không có số lớn thứ nhì"

arr = [10, 20, 20, 30, 40, 50]
print(so_lon_thu_nhi(arr))
def tong_chu_so(arr):
    return sum(sum(int(digit) for digit in str(abs(x))) for x in arr)

arr = [123, 45, 67]
print(tong_chu_so(arr))
def dem_so_lan_xuat_hien(arr, x):
    return arr.count(x)

arr = [1, 2, 2, 3, 3, 3, 4]
print(dem_so_lan_xuat_hien(arr, 3))
from collections import Counter

def so_xuat_hien_n_lan(arr, n):
    dem = Counter(arr)
    return [x for x, count in dem.items() if count == n]

arr = [1, 2, 2, 3, 3, 3, 4, 4]
print(so_xuat_hien_n_lan(arr, 2))
def so_xuat_hien_nhieu_nhat(arr):
    dem = Counter(arr)
    max_count = max(dem.values())
    return [x for x, count in dem.items() if count == max_count]

arr = [1, 2, 2, 3, 3, 3, 4, 4, 4]
print(so_xuat_hien_nhieu_nhat(arr))
    