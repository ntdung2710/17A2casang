n = int(input("Nhập vào chiều cao của tam giác: "))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end="")
    for j in range(i):
        print("* ", end='')
    print()
for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end="")
    for j in range(i):
        print("* ", end='')
    print()
