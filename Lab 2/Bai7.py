chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
can_nang = float(input("Nhập cân nặng của bạn (kg): "))
bmi = can_nang / (chieu_cao ** 2)
print("Chỉ số BMI của bạn là:", bmi)
if bmi < 18.5:
    print("Phân loại: Gầy")
elif 18.5 <= bmi <= 24.9:
    print("Phân loại: Bình thường")
elif 25.0 <= bmi <= 29.9:
    print("Phân loại: Hơi béo")
else:
    print("Phân loại: Béo")