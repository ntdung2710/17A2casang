chuoi_ban_dau = input("Nhập chuỗi ban đầu: ")
chuoi_sau_khi = input("Nhập chuỗi sau khi thay đổi: ")
if len(chuoi_sau_khi) > len(chuoi_ban_dau):
    co_the_thay_doi = all(chuoi_ban_dau.count(char) <= chuoi_sau_khi.count(char) for char in set(chuoi_sau_khi))
elif len(chuoi_sau_khi) < len(chuoi_ban_dau):
    co_the_thay_doi = all(chuoi_ban_dau.count(char) >= chuoi_sau_khi.count(char) for char in set(chuoi_ban_dau))
else:
    co_the_thay_doi = set(chuoi_ban_dau) == set(chuoi_sau_khi)
if co_the_thay_doi:
    print("Có thể thay đổi chuỗi ban đầu thành chuỗi sau khi thay đổi.")
else:
    print("Không thể thay đổi chuỗi ban đầu thành chuỗi sau khi thay đổi.")
