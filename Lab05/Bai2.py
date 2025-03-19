import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# Kết nối SQL Server
def connect_db():
    try:
        conn = pyodbc.connect(
            "DRIVER={SQL Server};"
            "SERVER=CONGTHANH;"  # Thay thế bằng tên máy chủ của bạn
            "DATABASE=QLMonAn;"
            "Trusted_Connection=yes;"  # Sử dụng Windows Authentication
        )
        return conn
    except Exception as e:
        messagebox.showerror("Lỗi kết nối", str(e))
        return None

# Hàm lấy danh sách nhóm món ăn
def load_nhom_monan():
    conn = connect_db()
    if conn is None:
        return []
    cursor = conn.cursor()
    cursor.execute("SELECT MaNhom, TenNhom FROM NhomMonAn")
    nhoms = cursor.fetchall()
    conn.close()
    return nhoms

# Hàm lấy danh sách món ăn theo nhóm
def load_monan(ma_nhom=None):
    conn = connect_db()
    if conn is None:
        return []
    cursor = conn.cursor()
    if ma_nhom:
        cursor.execute("SELECT MaMonAn, TenMonAn, DonViTinh, DonGia FROM MonAn WHERE Nhom = ?", (ma_nhom,))
    else:
        cursor.execute("SELECT MaMonAn, TenMonAn, DonViTinh, DonGia FROM MonAn")
    monans = cursor.fetchall()
    conn.close()
    return monans

# Hàm cập nhật danh sách món ăn lên giao diện
def update_table(ma_nhom=None):
    tree.delete(*tree.get_children())
    for mon in load_monan(ma_nhom):
        tree.insert("", "end", values=mon)

# Hàm khi chọn nhóm món ăn
def on_nhom_selected(event):
    selected_nhom = combo_nhom.get()
    ma_nhom = next((nhom[0] for nhom in nhom_list if nhom[1] == selected_nhom), None)
    update_table(ma_nhom)

# Hàm thêm món ăn
def add_monan():
    ten = entry_ten.get().strip()
    dvt = entry_dvt.get().strip()
    gia = entry_gia.get().strip()
    nhom_ten = combo_nhom_add.get().strip()

    if not ten or not dvt or not gia or not nhom_ten:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return
    
    try:
        gia = float(gia)  # Kiểm tra nếu giá trị là số hợp lệ
    except ValueError:
        messagebox.showerror("Lỗi", "Đơn giá phải là số hợp lệ!")
        return

    ma_nhom = next((nhom[0] for nhom in nhom_list if nhom[1] == nhom_ten), None)
    if ma_nhom is None:
        messagebox.showerror("Lỗi", "Nhóm món ăn không hợp lệ!")
        return

    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()

    cursor.execute("SELECT COALESCE(MAX(MaMonAn), 0) + 1 FROM MonAn")
    new_ma_monan = cursor.fetchone()[0]

    cursor.execute("INSERT INTO MonAn (MaMonAn, TenMonAn, DonViTinh, DonGia, Nhom) VALUES (?, ?, ?, ?, ?)",  
                   (new_ma_monan, ten, dvt, gia, ma_nhom))  
    conn.commit()
    conn.close()
    
    update_table()
    messagebox.showinfo("Thành công", "Đã thêm món ăn!")

# Hàm xóa món ăn
def delete_monan():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Lỗi", "Vui lòng chọn món ăn để xóa!")
        return

    mon_id = tree.item(selected_item, "values")[0]
    
    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM MonAn WHERE MaMonAn = ?", (mon_id,))
    conn.commit()
    conn.close()

    update_table()
    messagebox.showinfo("Thành công", "Đã xóa món ăn!")

# Hàm sửa món ăn
def update_monan():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Lỗi", "Vui lòng chọn món ăn để sửa!")
        return

    mon_id = tree.item(selected_item, "values")[0]
    ten = entry_ten.get().strip()
    dvt = entry_dvt.get().strip()
    gia = entry_gia.get().strip()

    if not ten or not dvt or not gia:
        messagebox.showerror("Lỗi", "Vui lòng nhập đầy đủ thông tin!")
        return

    try:
        gia = float(gia)
    except ValueError:
        messagebox.showerror("Lỗi", "Đơn giá phải là số hợp lệ!")
        return

    conn = connect_db()
    if conn is None:
        return
    cursor = conn.cursor()
    cursor.execute("UPDATE MonAn SET TenMonAn = ?, DonViTinh = ?, DonGia = ? WHERE MaMonAn = ?", 
                   (ten, dvt, gia, mon_id))
    conn.commit()
    conn.close()

    update_table()
    messagebox.showinfo("Thành công", "Đã cập nhật món ăn!")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý món ăn")
root.geometry("700x500")

# Dropdown chọn nhóm món ăn
nhom_list = load_nhom_monan()
if nhom_list:
    combo_nhom = ttk.Combobox(root, values=[nhom[1] for nhom in nhom_list], state="readonly")
    combo_nhom.pack(pady=5)
    combo_nhom.bind("<<ComboboxSelected>>", on_nhom_selected)

# Bảng hiển thị danh sách món ăn
columns = ("Mã món ăn", "Tên món ăn", "Đơn vị tính", "Đơn giá")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=150)
tree.pack(pady=10, fill="both", expand=True)

# Khung nhập thông tin
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Tên món ăn:").grid(row=0, column=0)
entry_ten = tk.Entry(frame)
entry_ten.grid(row=0, column=1)

tk.Label(frame, text="Đơn vị tính:").grid(row=1, column=0)
entry_dvt = tk.Entry(frame)
entry_dvt.grid(row=1, column=1)

tk.Label(frame, text="Đơn giá:").grid(row=2, column=0)
entry_gia = tk.Entry(frame)
entry_gia.grid(row=2, column=1)

tk.Label(frame, text="Nhóm món ăn:").grid(row=3, column=0)
combo_nhom_add = ttk.Combobox(frame, values=[nhom[1] for nhom in nhom_list] if nhom_list else [], state="readonly")
combo_nhom_add.grid(row=3, column=1)

# Nút thêm, xóa, sửa
tk.Button(root, text="Thêm", command=add_monan).pack(side="left", padx=10, pady=10)
tk.Button(root, text="Xóa", command=delete_monan).pack(side="left", padx=10, pady=10)
tk.Button(root, text="Sửa", command=update_monan).pack(side="left", padx=10, pady=10)

# Load danh sách món ăn ban đầu
update_table()

# Chạy ứng dụng
root.mainloop()
