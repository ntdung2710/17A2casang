import random
import csv

def rut_so():
    return random.randint(1, 100)

def kiem_tra_ket_qua(so_ban_chon, so_rut):
    return so_ban_chon == so_rut

def tinh_xac_suat_trung_giai(so_ban_chon, so_rut):
    if kiem_tra_ket_qua(so_ban_chon, so_rut):
        return "100%"
    else:
        return "0%"

def main():
    so_lan_choi = min(int(input("Nhập số lần chơi (tối đa 5 lần): ")), 5)
    so_ban_chon = set()
    ket_qua = []

    for _ in range(so_lan_choi):
        so_ban_chon_input = int(input("Nhập số bạn chọn (từ 1 đến 100): "))
        so_ban_chon.add(so_ban_chon_input)

    so_rut_list = [rut_so() for _ in range(so_lan_choi)]

    with open("ket_qua.csv", "w", newline="") as csvfile:
        fieldnames = ["So_ban_chon", "So_rut", "Xac_suat_trung_giai"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i, so_ban_chon_item in enumerate(so_ban_chon):
            if i < len(so_rut_list):
                ket_qua.append({
                    "So_ban_chon": so_ban_chon_item,
                    "So_rut": so_rut_list[i],
                    "Xac_suat_trung_giai": tinh_xac_suat_trung_giai(so_ban_chon_item, so_rut_list[i]),
                })
                writer.writerow({
                    "So_ban_chon": so_ban_chon_item,
                    "So_rut": so_rut_list[i],
                    "Xac_suat_trung_giai": tinh_xac_suat_trung_giai(so_ban_chon_item, so_rut_list[i]),
                })

    print("\nKết quả:")
    for i, so_ban_chon_item in enumerate(so_ban_chon):
        if i < len(so_rut_list):
            a = tinh_xac_suat_trung_giai(so_ban_chon_item, so_rut_list[i])
            print(
                f"Số bạn chọn: {so_ban_chon_item}, Số rút: {so_rut_list[i]}, Xác suất trúng giải: {a}"
            )
            if a == "100%":
                print("Bạn đã nhận được giải là 2 tỷ đồng 💵💵💵💵và 1 người đẹp trai như tôi 🤹🤹🤹🤹")

    return ket_qua

if __name__ == "__main__":
    ket_qua = main()