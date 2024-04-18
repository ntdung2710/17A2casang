day_so = input("Nhập dãy số: ").split()
day_so = [float(so) for so in day_so]
so_lon_nhat = max(day_so)
so_nho_nhat = min(day_so)
print("Số lớn nhất trong dãy số là:", so_lon_nhat)
print("Số nhỏ nhất trong dãy số là:", so_nho_nhat)
