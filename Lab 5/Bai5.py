chuoi1 = input("Nhập chuỗi thứ nhất: ")
chuoi2 = input("Nhập chuỗi thứ hai: ")
len1 = len(chuoi1)
len2 = len(chuoi2)
if len1 < len2:
    chuoi1 += ' ' * (len2 - len1)
elif len2 < len1:
    chuoi2 += ' ' * (len1 - len2)
chuoi_tron = ""
for i in range(max(len1, len2)):
    if i < len1:
        chuoi_tron += chuoi1[i]
    chuoi_tron += "-"
    if i < len2:
        chuoi_tron += chuoi2[i]
print("Chuỗi sau khi trộn là:", chuoi_tron)
