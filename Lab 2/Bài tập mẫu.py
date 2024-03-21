#Bài 1:
'''
n=int(input("Nhập vào một năm để kiểm tra:"))
if (n % 4 == 0)
'''





#Bài 2:
'''
x,y=map(int,input("Nhập tọa độ điểm M : ").split())
a,b=map(int,input("Nhập tọa độ điểm I : ").split())
r=int(input("Nhập bán kính: "))
import math
IM=math.sqrt((x-a)**2 + (y-b)**2)
if IM<=r:
    print("True")
else:
    print("False")
'''
#Bài 3:
#a,b,c = map(int,input("Nhập vào số đo của 3 cạnh: ").split())
#if (a + b > c) and (a + c > b) and (b + c > a): # kiểm tra điều kiện tam giác
 #   if ( a==b) and ( a==c) and ( b==c): #Kiểm tra điều kiện tam giác đều
  #      print("Bộ ba số lập thành tam giác đều")
   # elif ( a == b ) or (a == c) or (b == c): #Kiểm tra điều kiện tam giác cân
    #    if (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2): #Kiểm tra điều kiện vuông cân
     #       print("Bộ ba số đo nhập thành tam giác vuông cân")
      #  else:
       #     print("Bộ ba số đo lập thành tam giác cân")
    #elif (a ** 2 + b ** 2 == c ** 2) or (a ** 2 + c ** 2 == b ** 2) or (b ** 2 + c ** 2 == a ** 2): #Kiểm tra điều kiện vuông
     #   print("Bộ ba số đo lập thành tam giác vuông ")
    #else:
    #    print("Bộ ba số đo lập thành tam giác thường")
#else:
 #   print("Bộ ba số đo không phải là bộ ba của tam giác")        

#Bài 4:
'''
Viết chương trình tìm số lớn nhất trong 3 số bằng Python
max = a
Kiểm tra max có lớn hơn b hay không: max = b
Kiểm tra max có lớn hơn c hay không: max = c
In số lớn nhất trong 3 số
'''
"""
a,b,c = map(float,input("Nhập vào 3 số:").split())
if a>b and a>c:
    print("a là số lớn nhất trong 3 số")
elif b>a and b>c:
    print("b là số lớn nhất")
else:
    print("c là số lớn nhất")
"""

#Bài 5:
'''
Viết chương trinfhkieemr tra 1 kí tự trong bảng chữ cái tiếng anh là nguyên âm hay phụ âm
Ký tự là bất kì đc nhập từ bàn phím
Nguyên âm : UE OAI
'''
"""
ky_tu = input("Nhập vào một ký tự: ")
if (ky_tu == "u") or (ky_tu == "e") or (ky_tu == "o") or (ky_tu == "a") or (ky_tu == "i"):
    print("Ký tự đã nhập là nguyên âm ")
else:
    print("Ký tự đã nhập là phụ âm")
"""

#Bài 7:
# Viết chương trình giải hệ phương trình bậc nhất 2 ẩn:
a1,b1,c1 = map(float, input("Nhập các hệ số của phương trình 1: ").split())
a2,b2,c2 = map(float, input("Nhập các hệ số của phương trình 2: ").split())
d = a1*b2 - a2*b1
dx = c1*b2 - c2*b1
dy = a1*c2 - a2*c1
if d == 0:
    if dx == 0 and dy == 0:
        print("Hệ phương trình có vô số nghiệm")
    else:
        print("Hệ phương trình vô nghiệm")
else:
    x = dx/d
    y = dy/d
    print("Hệ phương trình có nghiệm duy nhất")