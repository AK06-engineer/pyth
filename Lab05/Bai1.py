import pyodbc

# Thông tin kết nối đến SQL Server
SERVER = "CONGTHANH"  # Thay bằng tên thật của bạn
DATABASE = "QLSinhVien"

# Chuỗi kết nối
conn_str = f"DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;"

def lay_danh_sach_lop():
    """Lấy danh sách lớp và hiển thị theo format đẹp"""
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Lop")
        lop_hoc = cursor.fetchall()

        print("Danh sách các lớp là:")
        for lop in lop_hoc:
            print("*" * 50)
            print(f"Mã lớp: {lop[0]}")
            print(f"Tên lớp: {lop[1]}")
            print("*" * 50)

        conn.close()
    except Exception as e:
        print("Lỗi khi lấy danh sách lớp:", e)

def lay_danh_sach_sinh_vien():
    """Lấy danh sách sinh viên và hiển thị theo format đẹp"""
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SinhVien")
        sinh_vien = cursor.fetchall()

        print("\nDanh sách sinh viên:")
        for sv in sinh_vien:
            print("-" * 50)
            print(f"Mã sinh viên: {sv[0]}")
            print(f"Họ và tên: {sv[1]}")
            print(f"Mã lớp: {sv[2]}")
            print("-" * 50)

        conn.close()
    except Exception as e:
        print("Lỗi khi lấy danh sách sinh viên:", e)

def tim_sinh_vien(ma_sv):
    """Tìm sinh viên theo mã sinh viên"""
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SinhVien WHERE ID = ?", (ma_sv,))
        sv = cursor.fetchone()

        if sv:
            print("\nThông tin sinh viên tìm được:")
            print("-" * 50)
            print(f"Mã sinh viên: {sv[0]}")
            print(f"Họ và tên: {sv[1]}")
            print(f"Mã lớp: {sv[2]}")
            print("-" * 50)
        else:
            print("\nKhông tìm thấy sinh viên!")

        conn.close()
    except Exception as e:
        print("Lỗi khi tìm sinh viên:", e)

def tim_sinh_vien_theo_lop_ten(ma_lop, ten):
    """Tìm sinh viên theo lớp và tên gần đúng"""
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM SinhVien WHERE MaLop = ? AND HoTen LIKE ?", (ma_lop, f"%{ten}%"))
        sv_list = cursor.fetchall()

        if sv_list:
            print("\nDanh sách sinh viên tìm được:")
            for sv in sv_list:
                print("-" * 50)
                print(f"Mã sinh viên: {sv[0]}")
                print(f"Họ và tên: {sv[1]}")
                print(f"Mã lớp: {sv[2]}")
                print("-" * 50)
        else:
            print("\nKhông tìm thấy sinh viên!")

        conn.close()
    except Exception as e:
        print("Lỗi khi tìm sinh viên theo lớp và tên:", e)

def them_sinh_vien(id, ho_ten, ma_lop):
    """Thêm một sinh viên mới vào cơ sở dữ liệu"""
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO SinhVien (ID, HoTen, MaLop) VALUES (?, ?, ?)", (id, ho_ten, ma_lop))
        conn.commit()
        print("\nThêm sinh viên thành công!")
        conn.close()
    except Exception as e:
        print("Lỗi khi thêm sinh viên:", e)

def cap_nhat_sinh_vien(id, ten_moi):
    """Cập nhật tên sinh viên"""
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("UPDATE SinhVien SET HoTen = ? WHERE ID = ?", (ten_moi, id))
        conn.commit()
        print("\nCập nhật sinh viên thành công!")
        conn.close()
    except Exception as e:
        print("Lỗi khi cập nhật sinh viên:", e)

def xoa_sinh_vien(id):
    """Xóa sinh viên theo mã ID"""
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM SinhVien WHERE ID = ?", (id,))
        conn.commit()
        print("\nXóa sinh viên thành công!")
        conn.close()
    except Exception as e:
        print("Lỗi khi xóa sinh viên:", e)

# Gọi các hàm để kiểm tra kết quả hiển thị
lay_danh_sach_lop()
lay_danh_sach_sinh_vien()
tim_sinh_vien(1)
tim_sinh_vien_theo_lop_ten(2, "Mai")
them_sinh_vien(13, "Nguyễn Văn A", 2)
cap_nhat_sinh_vien(13, "Nguyễn Văn B")
xoa_sinh_vien(13)
