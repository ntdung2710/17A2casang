print("Các số chính phương từ 1 đến 1000 là:")
for i in range(1, 1001):
    if int(i ** 0.5) ** 2 == i:
        print(i, end=" ")