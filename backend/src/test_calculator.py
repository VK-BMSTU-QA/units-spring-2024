import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)
    def test_add_float(self):
        self.assertAlmostEqual(self.calculator.addition(1.5, 2.3), 3.8)
    # def test_add_strings(self):
    #     self.assertRaises(TypeError, self.calculator.addition, "1", "2")
    
    def test_sub_int(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)
    def test_sub_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(1.5, 2.3), -0.8)
    def test_sub_strings(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "1", "2")
    
    def test_multiplication_int(self):
        self.assertEqual(self.calculator.multiplication(1, 0), 0)
    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)
    def test_multiplication_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.5, 2.3), 3.45)
    # def test_multiplication_int_strings(self):
    #     self.assertRaises(TypeError, self.calculator.multiplication, "1", 0)
    
    def test_division_int(self):
        self.assertEqual(self.calculator.division(1, 1), 1)
    def test_division_negative(self):
        self.assertEqual(self.calculator.division(-4, -2), 2)
    # def test_division_zero(self):
    #     self.assertRaises(ZeroDivisionError, self.calculator.division, -4, 0)
    def test_division_float(self):
        self.assertAlmostEqual(self.calculator.division(1.5, 2.3), 0.6521739)
    # def test_division_int_strings(self):
    #     self.assertRaises(TypeError, self.calculator.division, "1", 0)
    
    def test_absolute_int(self):
        self.assertEqual(self.calculator.adsolute(1), 1)
    def test_absolute_negative(self):
        self.assertEqual(self.calculator.adsolute(-1), 1)
    def test_absolute_float(self):
        self.assertAlmostEqual(self.calculator.adsolute(-1.5), 1.5)
    def test_absolute_int_strings(self):
        self.assertRaises(TypeError, self.calculator.adsolute, "1")
        
    def test_degree_int_one(self):
        self.assertEqual(self.calculator.degree(1, 10), 1)
    def test_degree_int(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
    def test_degree_negative_odd_degree(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)
    def test_degree_negative_even_degree(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)
    # def test_degree_less_than_one(self):
    #     self.assertEqual(self.calculator.degree(0.2, 3), 0.008)
    # def test_degree_negative_degree(self):
    #     self.assertEqual(self.calculator.degree(8, -3), 2)
    def test_degree_zero_degree(self):
        self.assertAlmostEqual(self.calculator.degree(4, 0), 1)
    # def test_degree_int_float_degree(self):
    #     self.assertEqual(self.calculator.degree(-1, 0.2), -1)
    def test_degree_int_strings(self):
        self.assertRaises(TypeError, self.calculator.degree, "1", 1)
    
    def test_ln_int_one(self):
        self.assertEqual(self.calculator.ln(1), 0)
    def test_ln_e2(self):
        self.assertEqual(self.calculator.ln(math.e**2), 2)
    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -2)
    
    def test_log_int_one(self):
        self.assertEqual(self.calculator.log(1, 3), 0)
    def test_log_int_normal(self):
        self.assertEqual(self.calculator.log(4, 2), 2)
    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -2, -1)
    
    def test_sqrt_int_one(self):
        self.assertEqual(self.calculator.sqrt(1), 1)
    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
    def test_sqrt_float(self):
        self.assertEqual(self.calculator.sqrt(0.04), 0.2)
    
    def test_nth_int_one(self):
        self.assertEqual(self.calculator.nth_root(1, 10), 1)
    def test_nth_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 10), 0)
    def test_nth_zero_root(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)
    
    
    
    
    
        
    
if __name__ == "__main__":
    unittest.main()
