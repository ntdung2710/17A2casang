while True:
    n = int(input("Nhập một số nguyên dương: "))
    if n > 0:
        break
    else:
        print("Vui lòng nhập lại số nguyên dương.")
# Tính tổng a
s_a = 0
for i in range(1, n + 1):
    s_a_temp = 1
    for j in range(1, i + 1):
        s_a_temp *= j
    s_a += s_a_temp
print("a) S =", s_a)
