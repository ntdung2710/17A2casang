n = int(input("Nhập vào chiều cao của tam giác: "))
for i in range(1, n + 1):
    # In ra khoảng trắng
    for j in range(n - i):
        print(" ", end="")
    # In ra dấu *
    for j in range(2 * i - 1):
        print("*", end="")
    print()

#Em chỉ vẽ được phầm trên