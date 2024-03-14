def factorial(n):
    # Hàm tính giai thừa
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, k):
    # Hàm tính tổ hợp chập k của n
    return factorial(n) / (factorial(k) * factorial(n - k))

def probability_all_red(total_balls, red_balls, num_drawn):
    # Xác suất rút ra tất cả là bi đỏ
    return combination(red_balls, num_drawn) / combination(total_balls, num_drawn)

def probability_at_least_one_blue(total_balls, blue_balls, num_drawn):
    # Xác suất ít nhất một viên bi xanh
    return 1 - probability_all_red(total_balls, blue_balls, num_drawn)

def probability_exactly_two_yellow(total_balls, yellow_balls, num_drawn):
    # Xác suất đúng hai viên là bi vàng
    return (combination(yellow_balls, 2) * combination(total_balls - yellow_balls, num_drawn - 2)) / combination(total_balls, num_drawn)

# Số lượng các viên bi trong hộp
total_balls = 50
red_balls = 20
blue_balls = 15
yellow_balls = 15

# Số lượng viên bi mà người dùng muốn rút ra
num_drawn = int(input("Nhập số lượng viên bi mà bạn muốn rút ra từ hộp: "))

# Tính và in ra xác suất cho từng trường hợp
print("1. Xác suất rút ra tất cả là bi đỏ:", round(probability_all_red(total_balls, red_balls, num_drawn), 4))
print("2. Xác suất ít nhất một viên là bi xanh:", round(probability_at_least_one_blue(total_balls, blue_balls, num_drawn), 4))
print("3. Xác suất đúng hai viên là bi vàng:", round(probability_exactly_two_yellow(total_balls, yellow_balls, num_drawn), 4))