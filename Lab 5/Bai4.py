chuoi_ky_tu = input("Nhập chuỗi ký tự: ")
chuoi_so = ''.join(filter(lambda x: x.isdigit(), chuoi_ky_tu))
if chuoi_so:
    so_nguyen = int(chuoi_so)
    if so_nguyen <= 1:
        la_so_nguyen_to = False
    else:
        la_so_nguyen_to = True
        for i in range(2, int(so_nguyen**0.5) + 1):
            if so_nguyen % i == 0:
                la_so_nguyen_to = False
                break
    if la_so_nguyen_to:
        print("Chuỗi ký tự sau khi loại bỏ là số nguyên tố.")
    else:
        print("Chuỗi ký tự sau khi loại bỏ không phải là số nguyên tố.")
else:
    print("Không có số nào trong chuỗi ký tự đã cho.")
