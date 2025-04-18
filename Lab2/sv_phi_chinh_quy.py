from SinhVien import SinhVien
from datetime import datetime

class SinhVienPhiCQ(SinhVien):
    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhDo: str, tgdt: int) -> None:
        super().__init__(maSo, hoTen, ngaySinh)
        self.trinhDo = trinhDo
        self.thoiGianDaoTao = tgdt

    def __str__(self) -> str:
        return super().__str__() + f"\t{self.trinhDo}\t{self.thoiGianDaoTao}"