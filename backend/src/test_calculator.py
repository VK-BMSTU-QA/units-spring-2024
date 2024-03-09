import unittest
from calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(0, 90), 90)
        self.assertEqual(self.calculator.addition(34789, -30), 34759)
        self.assertEqual(self.calculator.addition(77447, 677889), 755336)

    def test_multiplicat(self):
        self.assertEqual(self.calculator.multiplication(1, 4), 4)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 789), 0)
        self.assertEqual(self.calculator.multiplication(34789, -30), -1043670)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(0, 1), -1)
        self.assertEqual(self.calculator.subtraction(34789, -30), 34819)

    def test_div(self):
        self.assertIsNone(self.calculator.division(1, 0), 0)
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertEqual(self.calculator.division(2, 1), 2)
        self.assertEqual(self.calculator.division(1, 2), 0.5)
        self.assertEqual(self.calculator.division(9, 3), 3)
        self.assertEqual(self.calculator.division(354, 8), 44.25)

    def test_deg(self):
        self.assertEqual(self.calculator.degree(1, 1), 1)
        self.assertEqual(self.calculator.degree(1, 2), 1)
        self.assertEqual(self.calculator.degree(2, 1), 2)
        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertEqual(self.calculator.degree(2, -1), 0.5)
        self.assertEqual(self.calculator.degree(-2, 9), -512)
        self.assertEqual(self.calculator.degree(81, 0.5), 9)
        self.assertEqual(self.calculator.degree(789008, 0), 1)     

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertEqual(self.calculator.ln(math.e ** 2), 2)

    def test_log(self):
        self.assertEqual(self.calculator.log(1, 2), 0)
        self.assertEqual(self.calculator.log(2, 2), 1)
        self.assertEqual(self.calculator.log(4, 2), 2)
        self.assertEqual(self.calculator.log(6.25, 2.5), 2)
        self.assertEqual(self.calculator.log(2, 4), 0.5)
        self.assertEqual(self.calculator.log(0.5, 2), -1)
        self.assertEqual(self.calculator.log(0.5, 4), -0.5)
        self.assertRaises(ValueError, self.calculator.log, 0, 1)
        self.assertRaises(ValueError, self.calculator.log, 1, 0)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 1, 1)
        self.assertRaises(ValueError, self.calculator.log, -1, 577)
        self.assertRaises(ValueError, self.calculator.log, 4878, -1)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(6.25), 2.5)
        self.assertEqual(self.calculator.sqrt(0.25), 0.5)

    def nth_root(self):
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertEqual(self.calculator.nth_root(1, 1), 1)
        self.assertEqual(self.calculator.nth_root(1, -2), 1)
        self.assertEqual(self.calculator.nth_root(4, 2), 2)
        self.assertEqual(self.calculator.nth_root(4, 1), 4)
        self.assertEqual(self.calculator.nth_root(2, -1), 0.5)
        self.assertEqual(self.calculator.nth_root(4, -2), 0.5)
        self.assertEqual(self.calculator.nth_root(6.25, -1), 0.16)
        self.assertEqual(self.calculator.nth_root(6.25, -2), 0.4)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)

if __name__ == "__main__":
    unittest.main()
