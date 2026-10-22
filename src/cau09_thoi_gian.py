from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026 , 10 , 14 , 13 , 15 )
ket_thuc = datetime(2026 , 10 , 14 , 15 , 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

#du doan KQ phep tru(thoi_luong) : 1:50:00
#datetime : luu tru cu the ,ot moc TG co dinh
#str : chuoi van ban thuon tuy bieu dien thong tin ngay thang de nguoi dung doc dc, ko dung truc tiep de tinh toan cong tru dc
#timedelta : bieu thi mot khoang TG hay do lech, la KQ cua phep tru giua hai doi tuong

