N = int(input("Nhập vào một số nguyên N: "))
if N <= 0:
    print("Vui lòng nhập một số nguyên dương.")
else:
    NT_Dung = {}
    for x in range(1, N+1):
        NT_Dung[x] = x**3

    print("Từ điển Dũng dạng key = x và value = x^3:")
    print(NT_Dung)