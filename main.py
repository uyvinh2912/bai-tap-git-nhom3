def tinh_thue_thu_nhap(thu_nhap):
    # Kết hợp logic: Giảm trừ 4 triệu của A và tính thuế 10% của B
    thu_nhap_tinh_thue = thu_nhap - 4000000
    return max(0, thu_nhap_tinh_thue * 0.1)

print("Thuế phải nộp của bạn là:", tinh_thue_thu_nhap(10000000))

