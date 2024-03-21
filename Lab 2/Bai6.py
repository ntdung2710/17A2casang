a = int(input("Nhập số nguyên thứ nhất: "))
b = int(input("Nhập số nguyên thứ hai: "))
c = int(input("Nhập số nguyên thứ ba: "))
if a >= b >= c or c >= b >= a:
    so_lon_thu_hai = b
elif b >= a >= c or c >= a >= b:
    so_lon_thu_hai = a
else:
    so_lon_thu_hai = c
print("Số lớn thứ hai là:", so_lon_thu_hai)
