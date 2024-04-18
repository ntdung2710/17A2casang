n = int(input("Nhập số lượng số Fibonacci cần tạo: "))
fib = [0, 1]
[fib.append(fib[-2] + fib[-1]) for _ in range(2, n)]
print("Danh sách Fibonacci gồm", n, "số đầu tiên là:", fib[:n])