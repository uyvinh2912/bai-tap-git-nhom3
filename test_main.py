# test_main.py
import unittest
from main3 import tinh_diem_gpa

class TestGpaFunctions(unittest.TestCase):
    def test_gpa_he_muoi(self):
        # Kiểm tra điểm 8.5 trả về 4.0
        self.assertEqual(tinh_diem_gpa(8.5), 4.0)
    
    def test_gpa_tuyen_tinh(self):
        # Kiểm tra điểm 7.0 trả về 2.8
        self.assertEqual(tinh_diem_gpa(7.0), 2.8)

if __name__ == '__main__':
    unittest.main()