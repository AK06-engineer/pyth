def doi_gio_phut_giay(soGiay):
    gio = soGiay // 3600
    phut = (soGiay % 3600) // 60
    giay = soGiay % 60
    return f"{gio}:{phut}:{giay}"

print(doi_gio_phut_giay(3770))  # 1:2:50
