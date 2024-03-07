import unittest
import math
from .calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_concatenate(self):
        self.assertEqual(self.calculator.addition('1', '2'), '12')

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)

    def test_add_TypeError(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, '1')

    def test_add_none(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_add_float(self):
        self.assertEqual(self.calculator.addition(1.2, 2.3), 3.5)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-5, -1), -6)

    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)

    def test_repeat(self):
        self.assertEqual(self.calculator.multiplication('1', 5), '11111')

    def test_mult_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf)

    def test_mult_TypeError(self):
        self.assertRaises(TypeError, self.calculator.multiplication, '1', '1')

    def test_mult_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)

    def test_mult_float(self):
        self.assertEqual(self.calculator.multiplication(1.5, 1.5), 2.25)

    def test_mult_negative(self):
        self.assertEqual(self.calculator.multiplication(-5, -1), 5)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 0), math.inf)

    def test_sub_TypeError(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 1, '1')

    def test_sub_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)

    def test_sub_float(self):
        self.assertEqual(self.calculator.subtraction(1.5, 2.5), -1.0)

    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(-5, -1), -4)

    def test_div(self):
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_div_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_div_TypeError(self):
        self.assertRaises(TypeError, self.calculator.division, 1, '1')

    def test_div_none(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    def test_div_float(self):
        self.assertEqual(self.calculator.division(2.5, 2), 1.25)

    def test_div_negative(self):
        self.assertEqual(self.calculator.division(-5, -1), 5)

    def test_root(self):
        self.assertEqual(self.calculator.nth_root(81, 4), 3)

    def test_root_inf(self):
        self.assertEqual(self.calculator.nth_root(math.inf, math.inf), 1)

    def test_root_TypeError(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 1, '1')

    def test_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, None)

    def test_root_float(self):
        self.assertEqual(self.calculator.nth_root(10.5, 1.5), 4.795046974161089)

    def test_root_negative(self):
        self.assertEqual(self.calculator.nth_root(-5, -1), -0.2)

    def test_log(self):
        self.assertEqual(self.calculator.log(100, 10), 2)

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(1, math.inf), 0)

    def test_log_TypeError(self):
        self.assertRaises(TypeError, self.calculator.log, 1, '1')

    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, None, None)

    def test_log_float(self):
        self.assertEqual(self.calculator.log(10.5, 1.5), 5.7992049380885575)

    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -5, -1)

    def test_ads(self):
        self.assertEqual(self.calculator.adsolute(1), 1)

    def test_ads_inf(self):
        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)

    def test_ads_TypeError(self):
        self.assertRaises(TypeError, self.calculator.adsolute, '1')

    def test_ads_none(self):
        self.assertRaises(TypeError, self.calculator.adsolute, None)

    def test_ads_float(self):
        self.assertEqual(self.calculator.adsolute(1.2), 1.2)

    def test_ads_negative(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

    def test_ln_TypeError(self):
        self.assertRaises(TypeError, self.calculator.ln, '1')

    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln_float(self):
        self.assertEqual(self.calculator.ln(1.2), 0.1823215567939546)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -5)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(81), 9)

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

    def test_sqrt_TypeError(self):
        self.assertRaises(TypeError, self.calculator.sqrt, '1')

    def test_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt_float(self):
        self.assertEqual(self.calculator.sqrt(7.2), 2.6832815729997477)

    def test_sqrt_negative(self):
        self.assertEqual(self.calculator.sqrt(-5), 1.3691967456605067e-16 + 2.23606797749979j)


if __name__ == "__main__":
    unittest.main()
