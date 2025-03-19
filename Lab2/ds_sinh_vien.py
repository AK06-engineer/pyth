from datetime import datetime
from sinh_vien_chinh_quy import SinhVienChinhQuy
from sv_phi_chinh_quy import SinhVienPhiCQ
class DanhSachSv:
    def __init__(self):
        self.ds_sv = []

    def themSV(self, sv):
        self.ds_sv.append(sv)

    def Xuat(self):
        for sv in self.ds_sv:
            print(sv)

    def timSVTheoMs(self, maSo: int):
        for idx, sv in enumerate(self.ds_sv):
            if sv.maSo == maSo:
                return idx
        return -1

    def timSvTheoLoai(self, loai: str):
        if loai.lower() == "chinhquy":
            return [sv for sv in self.ds_sv if isinstance(sv, SinhVienChinhQuy)]
        elif loai.lower() == "phi chinh quy":
            return [sv for sv in self.ds_sv if isinstance(sv, SinhVienPhiCQ)]
        else:
            return []