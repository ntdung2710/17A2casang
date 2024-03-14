import math

def calculate_expression(x, z):
    result = (math.sin(x)**2 + math.atan(z)) / (math.log(x) + x*z + math.e**(-z))
    return round(result, 2)

# Yêu cầu người dùng nhập vào hai số thực x và z
x = float(input("Nhập vào giá trị của x: "))
z = float(input("Nhập vào giá trị của z: "))

# Tính giá trị của biểu thức
result = calculate_expression(x, z)

# In kết quả
print("Giá trị của biểu thức là:", result)