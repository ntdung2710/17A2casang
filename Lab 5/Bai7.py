chuoi = input("Nhập chuỗi: ")
so_chu_thuong = 0
so_chu_hoa = 0
so_chu_so = 0
so_ky_tu_dac_biet = 0
for ky_tu in chuoi:
    if ky_tu.islower():
        so_chu_thuong += 1
    elif ky_tu.isupper():
        so_chu_hoa += 1
    elif ky_tu.isdigit():
        so_chu_so += 1
    else:
        so_ky_tu_dac_biet += 1
print("Số lượng chữ thường trong chuỗi:", so_chu_thuong)
print("Số lượng chữ hoa trong chuỗi:", so_chu_hoa)
print("Số lượng chữ số trong chuỗi:", so_chu_so)
print("Số lượng ký tự đặc biệt trong chuỗi:", so_ky_tu_dac_biet)
