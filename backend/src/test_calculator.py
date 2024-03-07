import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, -3), -9)
    def test_substraction(self):
        self.assertEqual(self.calculator.subtraction(5, 7), -2)
    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
    def test_division_by_zero(self):
        self.assertEqual(self.calculator.division(4, 0), None)
    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(-4), 4)
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 4), 16)
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
    def test_log(self):
        self.assertEqual(self.calculator.log(16, 2), 4)
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)


if __name__ == "__main__":
    unittest.main()
