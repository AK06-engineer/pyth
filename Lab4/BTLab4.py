import tkinter as tk
from tkinter import messagebox

# Biến lưu trữ biểu thức toán học hiện tại
expression = ""

def btn_click(char):
    """Thêm ký tự (số hoặc toán tử) vào biểu thức."""
    global expression
    expression += str(char)
    input_text.set(expression)

def btn_clear():
    """Xóa toàn bộ biểu thức."""
    global expression
    expression = ""
    input_text.set("")

def btn_back():
    """Xóa ký tự cuối cùng của biểu thức."""
    global expression
    if len(expression) > 0:
        expression = expression[:-1]
        input_text.set(expression)

def btn_equal():
    """Tính toán biểu thức hiện tại và hiển thị kết quả."""
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result  # Cho phép tiếp tục tính tiếp với kết quả
    except Exception:
        messagebox.showerror("Lỗi", "Biểu thức không hợp lệ!")
        expression = ""
        input_text.set("")

def btn_close():
    """Đóng ứng dụng."""
    root.destroy()

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Calculator")
root.resizable(False, False)

# Tạo biến StringVar để liên kết với ô nhập (Entry)
input_text = tk.StringVar()

# Thanh nhập liệu
entry = tk.Entry(root, textvariable=input_text, font=('Arial', 14), bd=5, insertwidth=2, width=15, justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Hàng đầu tiên: Cls, Back, Close
btn_cls = tk.Button(root, text="Cls", width=7, height=2, command=btn_clear)
btn_cls.grid(row=1, column=0, padx=2, pady=2)

btn_back = tk.Button(root, text="Back", width=7, height=2, command=btn_back)
btn_back.grid(row=1, column=1, padx=2, pady=2)

btn_close = tk.Button(root, text="Close", width=7, height=2, command=btn_close)
btn_close.grid(row=1, column=2, padx=2, pady=2, columnspan=2, sticky='we')

# Hàng thứ hai: 7, 8, 9, /
btn_7 = tk.Button(root, text="7", width=7, height=2, command=lambda: btn_click("7"))
btn_7.grid(row=2, column=0, padx=2, pady=2)

btn_8 = tk.Button(root, text="8", width=7, height=2, command=lambda: btn_click("8"))
btn_8.grid(row=2, column=1, padx=2, pady=2)

btn_9 = tk.Button(root, text="9", width=7, height=2, command=lambda: btn_click("9"))
btn_9.grid(row=2, column=2, padx=2, pady=2)

btn_div = tk.Button(root, text="/", width=7, height=2, command=lambda: btn_click("/"))
btn_div.grid(row=2, column=3, padx=2, pady=2)

# Hàng thứ ba: 4, 5, 6, *
btn_4 = tk.Button(root, text="4", width=7, height=2, command=lambda: btn_click("4"))
btn_4.grid(row=3, column=0, padx=2, pady=2)

btn_5 = tk.Button(root, text="5", width=7, height=2, command=lambda: btn_click("5"))
btn_5.grid(row=3, column=1, padx=2, pady=2)

btn_6 = tk.Button(root, text="6", width=7, height=2, command=lambda: btn_click("6"))
btn_6.grid(row=3, column=2, padx=2, pady=2)

btn_mul = tk.Button(root, text="*", width=7, height=2, command=lambda: btn_click("*"))
btn_mul.grid(row=3, column=3, padx=2, pady=2)

# Hàng thứ tư: 1, 2, 3, -
btn_1 = tk.Button(root, text="1", width=7, height=2, command=lambda: btn_click("1"))
btn_1.grid(row=4, column=0, padx=2, pady=2)

btn_2 = tk.Button(root, text="2", width=7, height=2, command=lambda: btn_click("2"))
btn_2.grid(row=4, column=1, padx=2, pady=2)

btn_3 = tk.Button(root, text="3", width=7, height=2, command=lambda: btn_click("3"))
btn_3.grid(row=4, column=2, padx=2, pady=2)

btn_sub = tk.Button(root, text="-", width=7, height=2, command=lambda: btn_click("-"))
btn_sub.grid(row=4, column=3, padx=2, pady=2)

# Hàng thứ năm: 0, ., =, +
btn_0 = tk.Button(root, text="0", width=7, height=2, command=lambda: btn_click("0"))
btn_0.grid(row=5, column=0, padx=2, pady=2)

btn_dot = tk.Button(root, text=".", width=7, height=2, command=lambda: btn_click("."))
btn_dot.grid(row=5, column=1, padx=2, pady=2)

btn_eq = tk.Button(root, text="=", width=7, height=2, command=btn_equal)
btn_eq.grid(row=5, column=2, padx=2, pady=2)

btn_add = tk.Button(root, text="+", width=7, height=2, command=lambda: btn_click("+"))
btn_add.grid(row=5, column=3, padx=2, pady=2)

# Bắt đầu vòng lặp giao diện
root.mainloop()
