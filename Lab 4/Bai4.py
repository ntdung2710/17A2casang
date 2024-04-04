n = int(input("Nhập số nguyên n > 10:"))
#S1:
a = 1
S1 = 0
while 6**a <= n:
    S1 += 6**a
    a += 1
print("S1 =", S1)
#S2:
a = 0
S2 = 0
while 3**(2*a+1) <= n:
    S2 += 1/(3**(2*a+1))
    a +=1
print("S2 =",S2)
#S3:
a = 1
S3 = 0 
while a <= n:
    S3 += (-1)**(a-1)*a**2
    a += 1
print("S3 =",S3)
#S4:
a = 1
S4 = 0 
while a*(a+1)*(a+2) <= n:
    S4 += a*(a+1)*(a+2)
    a += 1
print("S4 =",S4)
