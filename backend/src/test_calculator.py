import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(2, 5), 10)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(5, 8), -3)

    def test_div__zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_div__int(self):
        self.assertEqual(self.calculator.division(1, 1), 1)

    def test_abs__positive(self):
        self.assertEqual(self.calculator.adsolute(3), 3)

    def test_abs__neitral(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_abs__negative(self):
        self.assertEqual(self.calculator.adsolute(-3), 3)

    def test_degree__zero(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_degree_5_2(self):
        self.assertEqual(self.calculator.degree(5, 2), 25)

    def test_degree_5_0(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_ln_1(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_e(self):
        self.assertEqual(self.calculator.ln(math.e), math.log(math.e))

    def test_log_4_2(self):
        self.assertEqual(self.calculator.log(4, 2), math.log(4, 2))

    def test_sqrt_2(self):
        self.assertEqual(self.calculator.sqrt(2), math.sqrt(2))

    def test_sqrt_0(self):
        self.assertEqual(self.calculator.sqrt(0), math.sqrt(0))

if __name__ == "__main__":
    unittest.main()
