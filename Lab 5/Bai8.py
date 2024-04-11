# Nhập một chuỗi từ người dùng có độ dài ít nhất là 10 ký tự
while True:
    chuoi = input("Nhập một chuỗi có độ dài ít nhất 10 ký tự: ")
    if len(chuoi) >= 10:
        break
    else:
        print("Chuỗi quá ngắn. Vui lòng nhập lại.")

# a) 
chuoi_a = chuoi[1:8]
print("a) Chuỗi con từ vị trí thứ 2 đến vị trí thứ 8:", chuoi_a)
# b)
chuoi_b = chuoi[4:9]
print("b) Chuỗi con từ vị trí thứ 5 gồm 5 ký tự:", chuoi_b)

# c) 
chuoi_c = chuoi[-3:]
print("c) Chuỗi con từ cuối chuỗi gồm 3 ký tự:", chuoi_c)

# d) 
chuoi_thuong = chuoi.lower()
print("d) Chuỗi sau khi chuyển đổi thành chữ thường:", chuoi_thuong)

# e)
chuoi_hoa = chuoi.upper()
print("e) Chuỗi sau khi chuyển đổi thành chữ hoa:", chuoi_hoa)

# f) 
chuoi_dao_nguoc = chuoi[::-1]
print("f) Chuỗi sau khi đảo ngược:", chuoi_dao_nguoc)
