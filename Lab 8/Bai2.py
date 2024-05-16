def tinh_giai_thua(n):
    ket_qua = 1
    for i in range(2, n + 1):
        ket_qua *= i
    return ket_qua
def hoan_vi(n, r):
    if r > n:
        return 0
    ket_qua = 1
    for i in range(n, n - r, -1):
        ket_qua *= i
    return ket_qua
def to_hop(n, r):
    if r > n:
        return 0
    tu_so = 1
    for i in range(n, n - r, -1):
        tu_so *= i
    mau_so = 1
    for i in range(1, r + 1):
        mau_so *= i
    return tu_so // mau_so
so_phan_tu = int(input("Nhập số phần tử (n): "))
so_phan_tu_lay = int(input("Nhập số phần tử lấy mỗi lần (r): "))
print(f"Số hoán vị của {so_phan_tu} phần tử lấy {so_phan_tu_lay} phần tử mỗi lần: p({so_phan_tu}, {so_phan_tu_lay}) = {hoan_vi(so_phan_tu, so_phan_tu_lay)}")
print(f"Số tổ hợp của {so_phan_tu} phần tử lấy {so_phan_tu_lay} phần tử mỗi lần: c({so_phan_tu}, {so_phan_tu_lay}) = {to_hop(so_phan_tu, so_phan_tu_lay)}")