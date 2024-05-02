sinh_vien = {}
for i in range(1, 11):
    ten = input(f"Nhập tên của sinh viên {i}: ")
    diem = float(input(f"Nhập điểm của sinh viên {i}: "))
    if diem < 4.0:
        loai_diem = 'F'
    elif diem < 5.5:
        loai_diem = 'D'
    elif diem < 7.0:
        loai_diem = 'C'
    elif diem < 8.5:
        loai_diem = 'B'
    else:
        loai_diem = 'A'

    sinh_vien[ten] = loai_diem
print("\nBảng xếp loại học lực:")
print("Tên sinh viên\t|\tXếp loại")
print("-" * 30)
for ten, loai_diem in sinh_vien.items():
    print(f"{ten}\t|\t{loai_diem}")

# 2) Thống kê số lượng sinh viên ở mỗi loại học lực
so_luong_loai_diem = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
for loai_diem in sinh_vien.values():
    so_luong_loai_diem[loai_diem] += 1
print("\nThống kê số lượng sinh viên theo loại học lực:")
for loai_diem, so_luong in so_luong_loai_diem.items():
    print(f"{loai_diem}: {so_luong} sinh viên")