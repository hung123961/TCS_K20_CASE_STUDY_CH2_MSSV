cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

#Tinh dien nang tieu thu va don gia 
dien_nang_kwh = cong_suat_w * so_phut / 60/ 1000
chi_phi =  dien_nang_kwh * don_gia_kwh

#in ca gia tri va kieu du lieu cua ca hai KQ
print("Voi so_phut = 90:")
print("Dien nang:" , dien_nang_kwh, "Kieu:" , type(dien_nang_kwh))
print("Chi phi:" , chi_phi , "Kieu:" , type(chi_phi))

#Thay so phut
so_phut = 60
dien_nang_kwh = cong_suat_w * so_phut / 60 /1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Voi so_phut = 60:")
print("Dien nang:" , dien_nang_kwh, "Kieu:" , type(dien_nang_kwh))
print("Chi phi:" , chi_phi, "Kieu:" , type(chi_phi))

