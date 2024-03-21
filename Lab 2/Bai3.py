so_nguyen = input("Nhập một số nguyên có ba chữ số: ")

# Kiểm tra số nguyên có ba chữ số hay không
if len(so_nguyen) != 3 or not so_nguyen.isdigit():
    print("Số nguyên nhập không hợp lệ!")
else:
    hang_tram = int(so_nguyen[0])
    hang_chuc = int(so_nguyen[1])
    hang_don_vi = int(so_nguyen[2])

    # Dictionary chứa cách đọc các chữ số
    hang_tram_dict = {
        1: 'one hundred',
        2: 'two hundred',
        3: 'three hundred',
        4: 'four hundred',
        5: 'five hundred',
        6: 'six hundred',
        7: 'seven hundred',
        8: 'eight hundred',
        9: 'nine hundred'
    }

    hang_chuc_dict = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }

    hang_don_vi_dict = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }

    # In cách đọc của số nguyên
    print("Cách đọc của số nguyên", so_nguyen, "là:", end=" ")

    if hang_tram != 0:
        print(hang_tram_dict[hang_tram], end=" ")
    
    if hang_chuc == 1:
        ten_to_nineteen = int(so_nguyen[1:])
        if ten_to_nineteen in range(10, 20):
            if hang_tram != 0:
                print("and", end=" ")
            print(hang_don_vi_dict[ten_to_nineteen])
    elif hang_chuc != 0:
        if hang_tram != 0:
            print("and", end=" ")
        print(hang_chuc_dict[hang_chuc], end=" ")

    if hang_chuc != 1 and hang_don_vi != 0:
        if hang_tram != 0 or hang_chuc != 0:
            print(hang_don_vi_dict[hang_don_vi])
        else:
            print(hang_don_vi_dict[hang_don_vi])