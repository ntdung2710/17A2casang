so_phan_tu = int(input("Nhập số phần tử của mảng: "))
mang = []
for i in range(so_phan_tu):
    so_nguyen = int(input("Nhập phần tử thứ {}: ".format(i+1)))
    mang.append(so_nguyen)
print("Các số nguyên tố trong mảng là:")
for so in mang:
    if so > 1:
        la_so_nguyen_to = True
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                la_so_nguyen_to = False
                break
        if la_so_nguyen_to:
            print(so)
print("Các số hoàn hảo trong mảng là:")
for so in mang:
    if so > 1:
        tong_uoc = 1
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                tong_uoc += i
                if i != so // i:
                    tong_uoc += so // i
        if tong_uoc == so:
            print(so)