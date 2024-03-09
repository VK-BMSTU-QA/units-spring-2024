import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)

    def test_subtraction_negative_result(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_division_negative_denominator(self):
        self.assertEqual(self.calculator.division(1, -1), -1)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-100), 100)

    def test_adsolute_negative(self):
        self.assertEqual(self.calculator.adsolute(-1), 1)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(123331, 0), 1)

    def test_degree_negative_exponent(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)

    def test_log_invalid_base(self):
        self.assertRaises(ValueError, self.calculator.log, 8, -2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_negative(self):
        self.assertRaises(ValueError, self.calculator.sqrt, -9)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(64, 2), 8)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(8, 8), 64)

    def test_multiply_negative(self):
        self.assertEqual(self.calculator.multiplication(-8, 8), -64)

if __name__ == "__main__":
    unittest.main()
