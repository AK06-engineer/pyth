from datetime import datetime

class SinhVien:
    truong = "Dai hoc Da Lat"

    def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
        self.maSo = maSo
        self.hoTen = hoTen
        self.ngaySinh = ngaySinh

    @property
    def hoTen(self):
        return self._hoTen

    @hoTen.setter
    def hoTen(self, hoTen: str):
        self._hoTen = hoTen

    @property
    def mssv(self):
        return self._maSo

    @mssv.setter
    def mssv(self, ms: int):
        if self.ktMsHopLe(ms):
            self._maSo = ms

    @staticmethod
    def ktMsHopLe(mssv: int):
        return len(str(mssv)) == 7

    def __str__(self) -> str:
        return f"{self.maSo}\t{self._hoTen}\t{self.ngaySinh.strftime('%d/%m/%Y')}"