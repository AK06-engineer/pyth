def tinh_toan(a, b):
    tong = a + b
    thuong = a / b if b != 0 else "Không thể chia cho 0"
    luy_thua = a ** b
    return tong, thuong, luy_thua

# Gọi hàm thử nghiệm
a, b = 5, 3
print(tinh_toan(a, b))
