chuoi_van_ban = input("Nhập chuỗi văn bản: ")
danh_sach_tu = chuoi_van_ban.split()
tu_can_tim = input("Nhập từ cần tìm kiếm: ")
vi_tri = []
so_lan_xuat_hien = 0
for i, tu in enumerate(danh_sach_tu):
    if tu == tu_can_tim:
        vi_tri.append(i)
        so_lan_xuat_hien += 1
if so_lan_xuat_hien > 0:
    print("Vị trí (index) của từ '{}' trong chuỗi là:".format(tu_can_tim), vi_tri)
else:
    print("Từ '{}' không xuất hiện trong chuỗi.".format(tu_can_tim))
tu_xuat_hien_nhieu_nhat = max(set(danh_sach_tu), key=danh_sach_tu.count)
so_lan_xuat_hien_nhieu_nhat = danh_sach_tu.count(tu_xuat_hien_nhieu_nhat)
print("Từ '{}' xuất hiện nhiều nhất trong chuỗi, xuất hiện {} lần.".format(tu_xuat_hien_nhieu_nhat, so_lan_xuat_hien_nhieu_nhat))
