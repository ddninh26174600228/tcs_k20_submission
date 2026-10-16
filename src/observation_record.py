ma_quan_sat= input("Nhap ma quan sat: ")
gia_tri_do= float(input("Nhap gia tri do: "))
gia_tri_f= gia_tri_do *9/5+32
print("Ma quan sat: ")
print(ma_quan_sat)
print("Gia tri do: ")
print(gia_tri_do)
print("Gia tri sau chuyen doi")
print(gia_tri_f)
from datetime import datetime
# Phan input da hoan thanh o checkpointB
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(f"ma quan sat: { ma_quan_sat}")
print(f"dai luong: Nhiet do")
print(f"gia tri: {gia_tri_do: .2f} do F")
print(f"thoi diem: {thoi_diem_text}")