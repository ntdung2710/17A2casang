chuoi1 = input("Nhập chuỗi thứ nhất: ")
chuoi2 = input("Nhập chuỗi thứ hai: ")
len1 = len(chuoi1)
len2 = len(chuoi2)
min_len = min(len1, len2)
chuoi_con_chung = ""
for i in range(min_len):
    if chuoi1[i] == chuoi2[i]:
        chuoi_con_chung += chuoi1[i]
    else:
        break
if len(chuoi_con_chung) > 0:
    print("Chuỗi con chung có độ dài ngắn nhất là:", chuoi_con_chung)
else:
    print("Không có chuỗi con chung nào.")
