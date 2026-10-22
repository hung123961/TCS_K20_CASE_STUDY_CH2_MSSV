#Dung input() de nhan bon gia triva in ngay sau khi nhap

ma_may = input("Nhap ma may:")
print("Kieu du lieu ma_may:" , type (ma_may))

cong_suat_raw = input("Nhap cong suat w:")
print("Kieu du lieu cong_suat_raw:" , type(cong_suat_raw))

so_phut_raw = input("Nhap so phut su dung:")
print("Kieu du lieu so_phut_raw:" , type(so_phut_raw))

don_gia_raw = input("Nhap don gia dien/kwh")
print("Kieu du lieu don_gia_raw:" , type(don_gia_raw))

#chuyen doi kieu du lieu phu hop
cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

#tinh lai
dien_nang_kwh = cong_suat_w * so_phut /60/1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Ket qua sau khi chuyen doi kieu du lieu:")
print(" Ma may:" , ma_may)
print("Dien nang tieu thu (kwh) : " , dien_nang_kwh)
print("Chi phi dien (VND) :" , chi_phi)


