print("Các số hoàn hảo bé hơn 500 là:")
for i in range(2, 500):
    sum_of_divisors = 0
    for n in range(1, i):
        if i % n == 0:
            sum_of_divisors += n
    if sum_of_divisors == i:
        print(i, end=" ")
