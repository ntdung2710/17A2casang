print("Các số nguyên tố từ 100 đến 1000 là:")
for i in range(100, 1001):
    if i > 1:
        is_prime = True
        for n in range(2, int(i ** 0.5) + 1):
            if i % n == 0:
                is_prime = False
                break
        if is_prime:
            print(i, end=" ")