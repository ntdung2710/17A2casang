def sumPdivisors(n):
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors += i
    return sum_divisors
def amicable(a, b):
    return sumPdivisors(a) == b and sumPdivisors(b) == a and a != b
a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if amicable(a, b):
    print(f"{a} và {b} là một cặp số amicable.")
else:
    print(f"{a} và {b} không phải là một cặp số amicable.")