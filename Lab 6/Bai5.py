chuoi_so = input("Nhập vào dãy số nguyên: ")
danh_sach_so = [int(x) for x in chuoi_so.split()]
n = len(danh_sach_so)
if n <= 2:
    print("Dãy số không đủ phần tử để tạo thành cấp số cộng.")
else:
    delta = danh_sach_so[1] - danh_sach_so[0]
    la_cap_so_cong = all(danh_sach_so[i] - danh_sach_so[i - 1] == delta for i in range(2, n))
    if la_cap_so_cong:
        print("Dãy số", danh_sach_so, "tạo thành cấp số cộng.")
    else:
        print("Dãy số", danh_sach_so, "không tạo thành cấp số cộng.")