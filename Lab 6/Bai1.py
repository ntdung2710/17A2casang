danh_sach = []
so_luong = int(input("Nhập số lượng phần tử của mảng: "))
print("Nhập các phần tử của mảng:")
for i in range(so_luong):
    so = int(input())
    danh_sach.append(so)
tong_chan = 0
tong_le = 0
for so in danh_sach:
    if so % 2 == 0:
        tong_chan += so
    else:
        tong_le += so
print("Tổng các số chẵn trong mảng là:", tong_chan)
print("Tổng các số lẻ trong mảng là:", tong_le)
