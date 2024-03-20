import unittest
import math
from src.calculator import Calculator
 

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()  
    # Тесты на сложение
    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    def test_fractional_add(self):
        self.assertEqual(self.calculator.addition(1.5, 2.5), 4.0)

    def test_negative_add(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_with_zero(self):
        self.assertEqual(self.calculator.addition(0, 5), 5)

    # Тесты на умножение
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, -3), -9) 
    def test_fractional_multiplication(self):
        self.assertEqual(self.calculator.multiplication(0.5, 2), 1.0)

    def test_positive_multiplication(self):
        self.assertEqual(self.calculator.multiplication(5, 5), 25)

    def test_multiply_by_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 10), 0)

    # Тесты на вычитание
    def test_fractional_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5.5, 0.5), 5.0)

    def test_negative_subtraction(self):
        self.assertEqual(self.calculator.subtraction(-5, -3), -2)

    def test_substraction(self):
        self.assertEqual(self.calculator.subtraction(5, 7), -2)

    # Тесты на деление
    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
    def test_fractional_division(self):
        self.assertEqual(self.calculator.division(1, 2), 0.5)

    def test_zero_divided_by_number(self):
        self.assertEqual(self.calculator.division(0, 5), 0)

    def test_division_resulting_in_periodic_number(self):
        self.assertAlmostEqual(self.calculator.division(2, 3), 0.666666, places=5)

    def test_division_by_zero(self):
        self.assertEqual(self.calculator.division(4, 0), None)

    # Тесты на возведение в степень
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 4), 16)
    def test_negative_exponent(self):
        self.assertEqual(self.calculator.degree(2, -1), 0.5)

    def test_fractional_exponent(self):
        self.assertAlmostEqual(self.calculator.degree(9, 0.5), 3, places=5)

    def test_number_to_zero_power(self):
        self.assertEqual(self.calculator.degree(7, 0), 1)

    def test_zero_to_power(self):
        self.assertEqual(self.calculator.degree(0, 5), 0)

    # Тесты на модуль
    def test_absolute_of_negative_number(self):
        self.assertEqual(self.calculator.adsolute(-4), 4)
    def test_absolute_of_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)
    def test_absolute_of_positive_number(self):
        self.assertEqual(self.calculator.adsolute(4), 4)
    def test_absolute_of_fractional_number(self):
        self.assertEqual(self.calculator.adsolute(0.5), 0.5)
    # Тесты на натуральный логарифм 
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)
    def test_ln_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)
    # Тесты на логарифм
    def test_log(self):
        self.assertEqual(self.calculator.log(16, 2), 4)
    def test_log_negative_base(self):
        with self.assertRaises(ValueError):
            self.calculator.log(4, -2)

    def test_log_negative_argument(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-16, 2)

    def test_log_zero_base(self):
        with self.assertRaises(ValueError):
            self.calculator.log(4, 0)

    def test_log_zero_argument(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 2)
    # Тесты на квадратный корень
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)
    def test_sqrt_of_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)
    def test_sqrt_of_fraction(self):
        self.assertAlmostEqual(self.calculator.sqrt(0.25), 0.5, places=5)
    # Тесты на корень
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
    def test_nth_root_of_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 3), 0)
    def test_nth_root_of_fraction(self):
        self.assertAlmostEqual(self.calculator.nth_root(0.125, 3), 0.5, places=5)

    # Дополнительные тесты на валидацию ввода
    def test_addition_of_strings(self):
        self.assertEqual(self.calculator.addition('a', 'b'), 'ab')

    def test_multiplication_of_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication("a", "b")


if __name__ == "__main__":
    unittest.main()
