def tinh_diem_gpa(diem_so):
    if diem_so >= 8.5:
        return 4.0          # ✅ Có indent (4 spaces)
    else:
        # TAO LOI CO Y: He so 3.5 (dung la 4)
        return round((diem_so / 10) * 3.5, 2)  # ✅ Có indent (4 spaces)

print("Điểm GPA hệ 4 là:", tinh_diem_gpa(8.5))