def tinh_diem_gpa(diem_so):
    if diem_so >= 8.5:
        return 4.0
    else:
        # ❌ Sai: hệ số 3.5 (đúng là 4)
        return round((diem_so / 10) * 3.5, 2)