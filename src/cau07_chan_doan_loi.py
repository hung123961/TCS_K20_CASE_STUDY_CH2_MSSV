ma_may = input("Nhap ma may:")
cong_suat_w = float(input("Nhap cong suat W:"))
so_phut = int(input("Nhap so phut:"))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"May: {ma_may}")
print(f"Dien nang: {dien_nang_kwh:.3f}kwh")





#loi thieu dau ) 0 cuoi dong 7
#loi la : bien cong_suat_w dang o kieu chuoi ki tu str nen ko the dung toan tu nhan vs so phut
#sua lai la : float(input......
#goi sai ten bien
#sua lai la : dien_nang_kwh
