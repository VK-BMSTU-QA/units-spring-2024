import unittest
import math
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_int_1(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    def test_add_int_2(self):
        self.assertEqual(self.calculator.addition(2, 1), 3)
    def test_add_int_3(self):
        self.assertEqual(self.calculator.addition(3, 1), self.calculator.addition(1, 3))
    def test_add_int_4(self):
        self.assertIsInstance(self.calculator.addition(1, 2), int)
    def test_add_int_5(self): # тестируем пул интов... =)
        self.assertIs(self.calculator.addition(1, 2), 3)
    def test_add_str_1(self):
        self.assertEqual(self.calculator.addition("ab", "ba"), "abba")
    def test_add_str_2(self):
        self.assertEqual(self.calculator.addition("ba", "ab"), "baab")
    def test_add_str_3(self):
        self.assertIsInstance(self.calculator.addition("ba", "ab"), str)
    def test_add_float_1(self):
        self.assertAlmostEqual(self.calculator.addition(0.3, 0.2), 0.5)
    def test_add_float_2(self):
        self.assertAlmostEqual(self.calculator.addition(0.2, 0.3), 0.5)
    def test_add_float_3(self):
        self.assertAlmostEqual(self.calculator.addition(0.3, 0.2), self.calculator.addition(0.2, 0.3))
    def test_add_float_4(self):
        self.assertIsInstance(self.calculator.addition(0.3, 0.2), float)
    def test_add_types(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, "123")

    def test_mul_1(self):
        self.assertEqual(self.calculator.multiplication(2, 7), 14)
    def test_mul_2(self):
        self.assertAlmostEqual(self.calculator.multiplication(2.0, 7.5), 15.0)
    def test_mul_3(self):
        self.assertEqual(self.calculator.multiplication(3, "ab"), "ababab")
    def test_mul_types(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 3.0, "ab")

    def test_sub_1(self):
        self.assertEqual(self.calculator.subtraction(2, 7), -5)
    def test_sub_2(self):
        self.assertAlmostEqual(self.calculator.subtraction(2.0, 7.5), -5.5)
    def test_sub_types(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 3.0, "ab")

    def test_div_1(self):
        self.assertAlmostEqual(self.calculator.division(1, 3), 1/3)
    def test_div_2(self):
        self.assertAlmostEqual(self.calculator.division(-1, -1), 1)
    def test_div_types(self):
        self.assertRaises(TypeError, self.calculator.division, 3.0, "ab")
    def test_div_zero(self):
        self.assertIsNone(self.calculator.division(3.0, 0))
    
    def test_abs_1(self):
        self.assertEqual(self.calculator.adsolute(4), 4)
    def test_abs_2(self):
        self.assertEqual(self.calculator.adsolute(-4), 4)
    
    def test_deg_1(self):
        self.assertAlmostEqual(self.calculator.degree(1, 219465322), 1)
    def test_deg_2(self):
        self.assertAlmostEqual(self.calculator.degree(3, -1), 1/3)

    def test_ln_1(self):
        self.assertAlmostEqual(self.calculator.ln(3), math.log(3))
    def test_ln_2(self):
        self.assertRaises(ValueError, self.calculator.ln, -4)

    def test_log_1(self):
        self.assertAlmostEqual(self.calculator.log(3, 5), math.log(3, 5))
    def test_log_2(self):
        self.assertRaises(ValueError, self.calculator.log, 3, -1)
    def test_log_3(self):
        self.assertAlmostEqual(self.calculator.log(1, 25), 0.0)

    def test_sqrt_1(self):
        self.assertAlmostEqual(self.calculator.sqrt(25), 5.0)
    def test_sqrt_2(self):
        self.assertAlmostEqual(self.calculator.sqrt(0), 0.0)

    def test_nth_root_1(self):
        self.assertAlmostEqual(self.calculator.nth_root(32, 22), 32 ** (1. / 22))
    def test_nth_root_2(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 32, 0.0)




if __name__ == "__main__":
    unittest.main()
