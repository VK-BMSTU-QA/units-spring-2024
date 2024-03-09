import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertEqual(self.calculator.addition(1.1, 1.2), 2.3)

    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertEqual(self.calculator.multiplication(-1, -1), 1)
        self.assertEqual(self.calculator.multiplication(1, 0), 0)
        self.assertEqual(self.calculator.multiplication(1.1, 1.2), 1.32)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertEqual(self.calculator.subtraction(1, -1), 2)
        self.assertEqual(self.calculator.subtraction(-1, 1), -2)
        self.assertEqual(self.calculator.subtraction(1, 0), 1)
        self.assertAlmostEqual(self.calculator.subtraction(1.1, 1.2), -0.1)

    def test_div(self):
        self.assertIsNone(self.calculator.division(1, 0), 0)
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertEqual(self.calculator.division(2, 1), 2)
        self.assertEqual(self.calculator.division(2, 2), 1)
        self.assertEqual(self.calculator.division(1, 2), 0.5)
        self.assertEqual(self.calculator.division(1, 0.5), 2)
        self.assertEqual(self.calculator.division(1, -1), -1)

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(-1), 1)
        self.assertEqual(self.calculator.adsolute(1), 1)
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_deg(self):
        self.assertEqual(self.calculator.degree(1, 1), 1)
        self.assertEqual(self.calculator.degree(1, 2), 1)
        self.assertEqual(self.calculator.degree(2, 1), 2)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(2, -1), 0.5)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(4, 0.5), 2)
        self.assertEqual(self.calculator.degree(0, 0), 1)


    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertEqual(self.calculator.ln(math.e ** 2), 2)

    def test_log(self):
        self.assertEqual(self.calculator.log(1, 2), 0)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 1, 1)
        self.assertRaises(ValueError, self.calculator.log, -1, 2)
        self.assertRaises(ValueError, self.calculator.log, 2, -1)
        self.assertEqual(self.calculator.log(2, 2), 1)
        self.assertEqual(self.calculator.log(4, 2), 2)
        self.assertEqual(self.calculator.log(6.25, 2.5), 2)
        self.assertEqual(self.calculator.log(2, 4), 0.5)
        self.assertEqual(self.calculator.log(0.5, 2), -1)
        self.assertEqual(self.calculator.log(0.5, 4), -0.5)
        self.assertRaises(ValueError, self.calculator.log, 0, 2)
        self.assertRaises(ValueError, self.calculator.log, 2, 0)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(6.25), 2.5)
        self.assertEqual(self.calculator.sqrt(0.25), 0.5)
        self.assertIsInstance(self.calculator.sqrt(-1), complex)
        self.assertEqual(self.calculator.sqrt(-1).imag, 1)
    
    def test_nroot(self):
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertEqual(self.calculator.nth_root(1, 1), 1)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)
        self.assertEqual(self.calculator.nth_root(1, -1), 1)
        self.assertEqual(self.calculator.nth_root(1, -2), 1)
        self.assertEqual(self.calculator.nth_root(4, 2), 2)
        self.assertEqual(self.calculator.nth_root(4, 1), 4)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 4, 0)
        self.assertEqual(self.calculator.nth_root(2, -1), 0.5)
        self.assertEqual(self.calculator.nth_root(4, -2), 0.5)
        self.assertEqual(self.calculator.nth_root(6.25, -1), 0.16)
        self.assertEqual(self.calculator.nth_root(6.25, -2), 0.4)


if __name__ == "__main__":
    unittest.main()
