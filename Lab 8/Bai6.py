# Ý 1:
def kiem_tra_so_le(n):
    return n % 2 != 0
danh_sach = [1, 9, 2, 7, 19, 27, 28, 12, 20, 25]
so_le = list(filter(kiem_tra_so_le, danh_sach))
print("Các số lẻ trong danh sách là:", so_le)

# Ý 2:
def kiem_tra_so_chan(n):
    return n % 2 == 0
danh_sach = [1, 9, 2, 7, 19, 27, 28, 12, 20, 25]
so_chan = list(filter(kiem_tra_so_chan, danh_sach))
print("Các số chẵn trong danh sách là:", so_chan)

# Ý 3:
def lap_phuong(n):
    return n ** 3
danh_sach_ban_dau = [1, 9, 2, 7]
danh_sach_lap_phuong = list(map(lap_phuong, danh_sach_ban_dau))
print("Danh sách các lập phương của các phần tử trong danh sách ban đầu là:", danh_sach_lap_phuong)

# Ý 4:
def kiem_tra_so_chan(n):
    return n % 2 == 0
def lap_phuong(n):
    return n ** 3
danh_sach_ban_dau = [1, 9, 2, 7, 19, 27, 28, 12, 20, 25]
so_chan = list(filter(kiem_tra_so_chan, danh_sach_ban_dau))
danh_sach_lap_phuong_so_chan = list(map(lap_phuong, so_chan))
print("Danh sách các lập phương của các số chẵn trong danh sách ban đầu là:", danh_sach_lap_phuong_so_chan)

# Ý 5:
def kiem_tra_so_le(n):
    return n % 2 != 0
def binh_phuong(n):
    return n ** 2
danh_sach_ban_dau = [1, 9, 2, 7, 19, 27, 28, 12, 20, 25]
so_le = list(filter(kiem_tra_so_le, danh_sach_ban_dau))
danh_sach_binh_phuong_so_le = list(map(binh_phuong, so_le))
print("Danh sách các bình phương của các số lẻ trong danh sách ban đầu là:", danh_sach_binh_phuong_so_le)