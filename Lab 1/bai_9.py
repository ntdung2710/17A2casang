def midpoint(p1, p2):
    # Tính toán tọa độ trung điểm của một cạnh
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)

# Hàm nhập tọa độ của một điểm từ người dùng
def input_point(point_name):
    x = float(input(f"Nhập tọa độ x của điểm {point_name}: "))
    y = float(input(f"Nhập tọa độ y của điểm {point_name}: "))
    return (x, y)

# Hàm tính toán và in ra tọa độ trung điểm của mỗi cạnh của tứ giác
def calculate_midpoints(M, N, P, Q):
    MN_midpoint = midpoint(M, N)
    NP_midpoint = midpoint(N, P)
    PQ_midpoint = midpoint(P, Q)
    QM_midpoint = midpoint(Q, M)
    
    print("Tọa độ trung điểm của cạnh MN:", MN_midpoint)
    print("Tọa độ trung điểm của cạnh NP:", NP_midpoint)
    print("Tọa độ trung điểm của cạnh PQ:", PQ_midpoint)
    print("Tọa độ trung điểm của cạnh QM:", QM_midpoint)

# Nhập tọa độ của bốn đỉnh M, N, P, Q từ người dùng
M = input_point("M")
N = input_point("N")
P = input_point("P")
Q = input_point("Q")

# Tính toán và in ra tọa độ trung điểm của mỗi cạnh của tứ giác
calculate_midpoints(M, N, P, Q)