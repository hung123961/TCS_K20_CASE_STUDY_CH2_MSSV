#Khai bao cac bien ban dau theo de bai
tong_phut = 135
cong_suat_w = 250

#Tinh so gio tron ven va so phut con lzi
so_gio = 135// 60
so_phut_du = 135 % 60
print(f"So gio tron ven: {so_gio} gio")
print(f"So phut con lai: {so_phut_du} phut")

#Tao bien su_dung_launhan True khi tong_phut > 60
su_dung_lau = tong_phut > 60
print(f"Su dung lau (>60 phut) : {su_dung_lau}")

#Tao bien du_lieu_hop_le nhan True khi cong_suat_w >0
du_lieu_hop_le =  (cong_suat_w > 0) and (tong_phut > 0)
print(f"Du lieu hop le: {du_lieu_hop_le}")

# du doan KQ va kiem chung
#BT 1 = 160 
#BT 2 = 360
bieu_thuc_1 = 100 + 20 * 3
bieu_thuc_2 = (100 + 20) * 3
print(f"Ket qua bieu thuc 1 (100 + 20 * 3) : {bieu_thuc_1}")
print(f"Ket qua bieu thuc 2 ((100 + 20) * 3 : {bieu_thuc_2}")



