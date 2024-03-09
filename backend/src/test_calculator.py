import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-50, 50), 0)

    def test_add_strings(self):
        self.assertEqual(self.calculator.addition('hello, ', 'world'), 'hello, world')

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)

    def test_add_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(2, 2), 4)

    def test_mult_negative(self):
        self.assertEqual(self.calculator.multiplication(0.5, -0.5), -0.25)

    def test_mult_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 10), math.inf)

    def test_mult_inf_negative(self):
        self.assertEqual(self.calculator.multiplication(math.inf, -10), -math.inf)

    def test_mult_strings(self):
        self.assertEqual(self.calculator.multiplication('hi', 3), 'hihihi')

    def test_mult_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'hello', 'world')

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(100, 50), 50)

    def test_sub_float(self):
        self.assertEqual(self.calculator.subtraction(0.5, 0.1), 0.4)

    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 100), math.inf)

    def test_sub_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'hello', 'world')

    def test_div(self):
        self.assertEqual(self.calculator.division(100, 20), 5)

    def test_div_negative(self):
        self.assertEqual(self.calculator.division(100, -20), -5)

    def test_div_by_zero(self):
        self.assertEqual(self.calculator.division(10, 0), None)

    def test_div_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(-100), 100)

    def test_abs_inf(self):
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

    def test_abs_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.adsolute, None)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 10), 1024)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(-2, 2), 4)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_degree_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.degree, None, None)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e * math.e), 2)

    def test_ln_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)

    def test_log_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.log, None, None)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(25), 5)

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

    def test_sqrt_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(1024, 10), 2)

    def test_nth_root_of_one(self):
        self.assertEqual(self.calculator.nth_root(1, 10), 1)

    def test_nth_root_wrong_type(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, None)


if __name__ == "__main__":
    unittest.main()
