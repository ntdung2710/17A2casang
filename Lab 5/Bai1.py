so_nguyen_duong = int(input("Nhập số nguyên dương: "))
if so_nguyen_duong < 0:
    print("Vui lòng nhập số nguyên dương.")
else:
    so_nhi_phan = ""
    while so_nguyen_duong > 0:
        du = so_nguyen_duong % 2
        so_nhi_phan = str(du) + so_nhi_phan
        so_nguyen_duong //= 2
print("Số nhị phân tương ứng là:", so_nhi_phan)
