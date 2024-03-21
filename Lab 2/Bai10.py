the_loai = int(input("Nhập thể loại phim muốn xem: "))
thoi_gian = input("Nhập thời gian muốn xem (sáng, trưa, chiều, tối): ")
if the_loai == "Hành động" or the_loai == "Hài hước":
    if thoi_gian == "sáng" or thoi_gian == "trưa":
        print("Thời gian chiếu phim:", thoi_gian)
    else:
        print("Không có suất chiếu")
elif the_loai == "Kinh dị":
    if thoi_gian == "tối":
        print("Thời gian chiếu phim:", thoi_gian)
    else:
        print("Không có suất chiếu")
elif the_loai == "Tình cảm":
    if thoi_gian == "tối":
        print("Thời gian chiếu phim:", thoi_gian)
    else:
        print("Không có suất chiếu")
elif the_loai == "Hoạt hình":
    if thoi_gian == "sáng" or thoi_gian == "trưa":
        print("Thời gian chiếu phim:", thoi_gian)
    else:
        print("Không có suất chiếu")
else:
    print("Thể loại phim không hợp lệ")