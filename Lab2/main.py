from datetime import datetime
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
from ds_sinh_vien import DanhSachSv

# Tạo các đối tượng sinh viên
sv1 = SinhVienChinhQuy(1957690, "Trần Văn A", datetime.strptime("23/6/1999", "%d/%m/%Y"), 80)
sv2 = SinhVienChinhQuy(1957691, "Nguyễn Văn C", datetime.strptime("5/12/1999", "%d/%m/%Y"), 90)
sv3 = SinhVienPhiCQ(1957692, "Thái Thị Thu", datetime.strptime("15/8/1998", "%d/%m/%Y"), "Cao Đẳng", 2)
sv4 = SinhVienPhiCQ(2000324, "Trần Thanh Tâm", datetime.strptime("27/8/2000", "%d/%m/%Y"), "Cao Đẳng", 2)
sv5 = SinhVienPhiCQ(2004544, "Nguyễn Thanh Trà", datetime.strptime("17/5/2000", "%d/%m/%Y"), "Trung Cấp", 2.5)
sv6 = SinhVienChinhQuy(2004567, "Nguyễn Thành Nam", datetime.strptime("7/12/1999", "%d/%m/%Y"), 60)
sv7 = SinhVienPhiCQ(2004545, "Nguyễn Thanh Thanh", datetime.strptime("29/10/1998", "%d/%m/%Y"), "Trung Cấp", 2.5)
sv8 = SinhVienChinhQuy(2004679, "Võ Hoài Nam", datetime.strptime("4/1/2000", "%d/%m/%Y"), 70)

# Quản lý danh sách sinh viên
dssv = DanhSachSv()
dssv.themSV(sv1)
dssv.themSV(sv2)
dssv.themSV(sv3)
dssv.themSV(sv4)
dssv.themSV(sv5)
dssv.themSV(sv6)
dssv.themSV(sv7)
dssv.themSV(sv8)

dssv.Xuat()

vt = dssv.timSVTheoMs(2000324)
print(f"Sinh viên ở vị trí thứ {vt + 1} trong danh sách")

kq = dssv.timSvTheoLoai("chinhquy")
print("Danh sách sinh viên chính quy:")
for sv in kq:
    print(sv)