import unittest
from src.calculator import Calculator
# from calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_no_input(self):
        with self.assertRaises(TypeError):
          self.calculator.addition()

        with self.assertRaises(TypeError):
          self.calculator.addition(1)

        with self.assertRaises(TypeError):
          self.calculator.multiplication()

        with self.assertRaises(TypeError):
          self.calculator.subtraction()

        with self.assertRaises(TypeError):
          self.calculator.division()

        with self.assertRaises(TypeError):
          self.calculator.ln()

        with self.assertRaises(TypeError):
          self.calculator.adsolute()

        with self.assertRaises(TypeError):
          self.calculator.degree()

    def test_not_int(self):
      with self.assertRaises(TypeError):
        self.calculator.addition('asdf', 123)

      with self.assertRaises(TypeError):
        self.calculator.degree('asdf')

      with self.assertRaises(TypeError):
        self.calculator.ln([])

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_fractional(self):
        self.assertEqual(self.calculator.addition(1.2, 2.1), 3.3)

    def test_add_with_zero(self):
        self.assertEqual(self.calculator.addition(0, 8), 8)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(2, 5), 10)

    def test_mul_fractional(self):
        self.assertEqual(self.calculator.multiplication(8.1, 3.6), 29.16)

    def test_mul_with_zero(self):
        self.assertEqual(self.calculator.multiplication(9999, 0), 0)

    def test_mul_negative(self):
        self.assertEqual(self.calculator.multiplication(-15, -3), 45)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(5, 8), -3)

    def test_sub_fractional(self):
        self.assertEqual(self.calculator.subtraction(5.3, 8.5), -3.2)

    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(-5, -8), 3)

    def test_div__zero(self):
        self.assertEqual(self.calculator.division(1, 0), None)

    def test_div__int(self):
        self.assertEqual(self.calculator.division(1, 1), 1)

    def test_div__fractional(self):
        self.assertEqual(self.calculator.division(1.5, 1.2), 1.25)

    def test_div__zero_with_num(self):
        self.assertEqual(self.calculator.division(0, 9999), 0)

    def test_div__period(self):
        self.assertAlmostEqual(self.calculator.division(2, 3), 0.66667, places=5)

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

    def test_degree_4_05(self):
        self.assertEqual(self.calculator.degree(4, 0.5), 2)

    def test_degree_4_negative_2(self):
        self.assertEqual(self.calculator.degree(4, -2), 0.0625)

    def test_degree_fractional(self):
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)

    def test_ln_1(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_negative_1(self):
        with self.assertRaises(ValueError):
          self.calculator.ln(-1)

    def test_ln_0(self):
        with self.assertRaises(ValueError):
          self.calculator.ln(0)

    def test_ln_e(self):
        self.assertEqual(self.calculator.ln(math.e), math.log(math.e))

    def test_log_4_2(self):
        self.assertEqual(self.calculator.log(4, 2), math.log(4, 2))

    def test_sqrt_9(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_sqrt_625(self):
        self.assertEqual(self.calculator.sqrt(6.25), 2.5)

    def test_sqrt_3(self):
        self.assertAlmostEqual(self.calculator.sqrt(3), 1.732, places=3)

    def test_sqrt_0(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

if __name__ == "__main__":
    unittest.main()
