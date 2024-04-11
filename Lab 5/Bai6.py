chuoi = input("Nhập chuỗi: ")
ky_tu_dac_biet = {}
for ky_tu in chuoi:
    if not ky_tu.isalnum():
        ky_tu_dac_biet[ky_tu] = ky_tu_dac_biet.get(ky_tu, 0) + 1
tong_so_ky_tu_dac_biet = sum(ky_tu_dac_biet.values())
ty_le_phan_tram = {}
for ky_tu, so_lan_xuat_hien in ky_tu_dac_biet.items():
    ty_le_phan_tram[ky_tu] = (so_lan_xuat_hien / tong_so_ky_tu_dac_biet) * 100
print("Ký tự đặc biệt và số lần xuất hiện tương ứng:")
for ky_tu, so_lan_xuat_hien in ky_tu_dac_biet.items():
    print(f"'{ky_tu}': {so_lan_xuat_hien} lần")
print("\nTỷ lệ phần trăm của mỗi ký tự đặc biệt trong chuỗi:")
for ky_tu, ty_le in ty_le_phan_tram.items():
    print(f"'{ky_tu}': {ty_le:.2f}%")
