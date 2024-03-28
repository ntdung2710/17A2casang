n = int(input("Nhập số nguyên dương n: "))
gt = 1
for i in range(1, n + 1):
    gt *= i
print("Giai thừa của", n, "là:", gt)
