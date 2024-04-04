so_nguyen = []
tong_so = 0
while tong_so <= 1000:
    so = int(input("Nhập số nguyên dương: "))
    if so > 0:
        so_nguyen.append(so)
        tong_so += so
    else:
        print("Vui lòng nhập số nguyên dương.")
so_le = []
so_chan = []
for so in so_nguyen:
    if so % 2 != 0:
        so_le.append(so)
    else:
        so_chan.append(so)
print("Các số lẻ đã nhập là:", end=" ")
for le in so_le:
    print(le, end=" ")
print("\nCác số chẵn đã nhập là:", end=" ")
for chan in so_chan:
    print(chan, end=" ")
print("\nSố lượng các số nguyên đã nhập:", len(so_nguyen))
