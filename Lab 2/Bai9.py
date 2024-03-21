a = float(input("Nhập hệ số góc của đường thẳng: "))
b = float(input("Nhập hệ số tự do của đường thẳng: "))
x_center = float(input("Nhập tọa độ x của tâm đường tròn: "))
y_center = float(input("Nhập tọa độ y của tâm đường tròn: "))
radius = float(input("Nhập bán kính của đường tròn: "))
distance = abs(b - y_center - a * x_center) / ((a**2 + 1)**0.5)
if distance < radius:
    print("\nĐường thẳng cắt đường tròn.")
else:
    if distance == radius:
        print("\nĐường thẳng tiếp xúc đường tròn.")
    else:
        if distance > radius:
            print("\nĐường thẳng nằm ngoài đường tròn.")
        else:
            print("\nĐường thẳng nằm trong đường tròn.")
