a=float(input("Hãy nhập độ dài cạnh đáy: "))
h=float(input("Hãy nhập chiều cao: "))
Sxq=2*a*h
print(f"Diện tích xung quanh của hình chóp tứ giác đều là :{Sxq:.2f}".format(Sxq))
Stp=Sxq+a*2
print(f"Diện tích toàn phần của hình chóp tứ giác đều là :{Stp:.2f}".format(Stp))
V=1/3*a*2*h
print(f"Thể tích của hình chóp tứ giác đều là :{V:.2f}".format(V))