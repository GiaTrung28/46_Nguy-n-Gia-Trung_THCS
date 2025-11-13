
gia_san_pham = 50.0
so_luong = 3
tong_chi_phi = gia_san_pham * so_luong
thue_vat = tong_chi_phi * 0.10
tong_tien_phai_tra = tong_chi_phi + thue_vat
print(f"Tổng tiền phải trả (làm tròn): *{round(tong_tien_phai_tra, 2)}* VND")
