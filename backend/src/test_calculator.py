import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    def test_division(self):
        self.assertEqual(self.calculator.division(2, 1), 2)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-10), 10)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(10, 3), 1000)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0.0)
        self.assertEqual(self.calculator.ln(math.e), 1.0)
        self.assertEqual(self.calculator.ln(10), math.log(10))

    def test_log(self):
        self.assertEqual(self.calculator.log(100, 10), 2.0)
        self.assertEqual(self.calculator.log(8, 2), 3.0)
        self.assertEqual(self.calculator.log(27, 3), 3.0)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2.0)
        self.assertEqual(self.calculator.sqrt(9), 3.0)
        self.assertEqual(self.calculator.sqrt(16), 4.0)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(1, 2), 1.0)
        self.assertEqual(self.calculator.nth_root(8, 3), 2.0)
        self.assertEqual(self.calculator.nth_root(27, 3), 3.0)

if __name__ == "__main__":
    unittest.main()
