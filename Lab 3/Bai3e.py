tong_ngu_giac = 0
for n in range(1, 201):
    so_ngu_giac = n * (3 * n - 1) // 2
    tong_ngu_giac += so_ngu_giac
print("Tổng của các số ngũ giác trong đoạn từ 1 đến 200 là:", so_ngu_giac)
