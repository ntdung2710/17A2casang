tien_dau_tu = 10000
lai_suat_hang_nam = 0.06
amount_after_5_years = tien_dau_tu * (1 + lai_suat_hang_nam) * 5
print(f"Số tiền có sau 5 năm là :{amount_after_5_years:.2f}".format(amount_after_5_years))
amount_after_10_years = tien_dau_tu * (1 + lai_suat_hang_nam) * 10
print(f"Số tiền có sau 10 năm là :{amount_after_10_years:.2f}".format(amount_after_10_years))
growth_rate = (amount_after_10_years - amount_after_5_years) / tien_dau_tu
print(f"Tỷ lệ tăng trưởng của số tiền bạn sẽ có sau 10 năm so với số tiền bạn sẽ có sau 5 năm là :{growth_rate:.2f}".format(growth_rate))