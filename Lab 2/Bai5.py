so_nguoi = int(input("Nhập số lượng người: "))
gia_ve_mot_nguoi = 120000
tong_tien = so_nguoi * gia_ve_mot_nguoi
if so_nguoi >= 2 and so_nguoi <= 4:
    tong_tien *= 0.95
elif so_nguoi >= 5 and so_nguoi <= 10:
    tong_tien *= 0.9
elif so_nguoi > 10:
    tong_tien *= 0.8
print("Tổng số tiền phải trả:", tong_tien, "đồng")