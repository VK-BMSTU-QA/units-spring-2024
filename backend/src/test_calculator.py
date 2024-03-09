import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    # Addition

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_backward(self):
        self.assertEqual(self.calculator.addition(2, 1), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-2, 3), 1)

    def test_add_negative_equals_zero(self):
        self.assertEqual(self.calculator.addition(-2, 2), 0)

    def test_add_negative_equals_negative_num(self):
        self.assertEqual(self.calculator.addition(-2, 1), -1)

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(1, 0), 1)

    def test_add_fraction(self):
        self.assertAlmostEqual(self.calculator.addition(0.1, 1), 1.1, places=7)

    def test_add_negative_fraction(self):
        self.assertAlmostEqual(self.calculator.addition(-0.1, 1.1), 1, places=7)

    # Subtraction

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    def test_subtraction_equals_negative_num(self):
        self.assertEqual(self.calculator.subtraction(2, 3), -1)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(3, -2), 5)

    def test_subtraction_zero(self):
        self.assertEqual(self.calculator.subtraction(3, 0), 3)

    def test_subtraction_fraction(self):
        self.assertAlmostEqual(self.calculator.subtraction(3, 0.2), 2.8, places=7)

    def test_subtraction_negative_fraction(self):
        self.assertAlmostEqual(self.calculator.subtraction(3, -0.2), 3.2, places=7)

    def test_subtraction_fraction_from_fraction(self):
        self.assertAlmostEqual(self.calculator.subtraction(3.2, 0.2), 3, places=7)

    def test_subtraction_negative_fraction_from_fraction(self):
        self.assertAlmostEqual(self.calculator.subtraction(3.2, -0.2), 3.4, places=7)

    # Multiplication

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_multiplication_backwards(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)

    def test_multiplication_one(self):
        self.assertEqual(self.calculator.multiplication(2, 1), 2)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(2, 0), 0)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(2, -3), -6)

    def test_multiplication_negative_one(self):
        self.assertEqual(self.calculator.multiplication(2, -1), -2)

    def test_multiplication_fraction(self):
        self.assertAlmostEqual(self.calculator.multiplication(2, 0.5), 1, places=7)

    def test_multiplication_negative_fraction(self):
        self.assertAlmostEqual(self.calculator.multiplication(2, -0.5), -1, places=7)

    def test_multiplication_fraction_result_is_fraction(self):
        self.assertAlmostEqual(self.calculator.multiplication(2, 0.7), 1.4, places=7)

    def test_multiplication_fraction_result_is_negative_fraction(self):
        self.assertAlmostEqual(self.calculator.multiplication(2, -0.7), -1.4, places=7)

    # Division
        
    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2)

    def test_division_same_number(self):
        self.assertEqual(self.calculator.division(3, 3), 1)

    def test_division_one(self):
        self.assertEqual(self.calculator.division(5, 1), 5)

    def test_division_divisible_zero(self):
        self.assertEqual(self.calculator.division(0, 5), 0)

    def test_division_negative_num(self):
        self.assertEqual(self.calculator.division(6, -3), -2)

    def test_division_negative_divisible(self):
        self.assertEqual(self.calculator.division(-6, 3), -2)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(3, 0), None)

    def test_division_fraction(self):
        self.assertAlmostEqual(self.calculator.division(5, 2.5), 2, places=7)

    def test_division_result_is_fraction(self):
        self.assertAlmostEqual(self.calculator.division(5, 2), 2.5, places=7)

    def test_division_smaller_num_by_bigger(self):
        self.assertAlmostEqual(self.calculator.division(2, 5), 0.4, places=7)

    def test_division_negative_fraction(self):
        self.assertAlmostEqual(self.calculator.division(5, -2.5), -2, places=7)

    def test_division_by_fraction_negative_divisible(self):
        self.assertAlmostEqual(self.calculator.division(-5, 2.5), -2, places=7)

    # Absolute

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(3), 3)

    def test_adsolute_negative(self):
        self.assertEqual(self.calculator.adsolute(-3), 3)

    def test_adsolute_fraction(self):
        self.assertAlmostEqual(self.calculator.adsolute(3.2), 3.2)

    def test_adsolute_fraction(self):
        self.assertAlmostEqual(self.calculator.adsolute(-3.2), 3.2)

    # Degree ("power of" правильно)

    def test_degree(self):
        self.assertAlmostEqual(self.calculator.degree(3, 2), 9)

    def test_degree_one(self):
        self.assertAlmostEqual(self.calculator.degree(1, 2), 1)

    def test_degree_power_of_zero(self):
        self.assertAlmostEqual(self.calculator.degree(3, 0), 1)

    def test_degree_power_of_one(self):
        self.assertAlmostEqual(self.calculator.degree(3, 1), 3)

    def test_degree_power_of_fraction(self):
        self.assertAlmostEqual(self.calculator.degree(9, 0.5), 3)

    def test_degree_fraction(self):
        self.assertAlmostEqual(self.calculator.degree(0.5, 2), 0.25)

    def test_degree_power_is_negative(self):
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)

    def test_degree_negative(self):
        self.assertAlmostEqual(self.calculator.degree(-2, 2), 4)

    # Ln

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.exp(1)), 1)

    def test_ln_one(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.exp(2)), 2)

    def test_ln_negative(self):
        with self.assertRaises(Exception) as cm:
            self.calculator.ln(-1)

    def test_ln_zero(self):
        with self.assertRaises(Exception) as cm:
            self.calculator.ln(0)

    # Log

    def test_log(self):
        self.assertEqual(self.calculator.log(4, 2), 2)

    def test_log_same_num(self):
        self.assertEqual(self.calculator.log(2, 2), 1)

    def test_log_one(self):
        self.assertEqual(self.calculator.log(1, 2), 0)

    def test_log_log_is_fraction(self):
        self.assertAlmostEqual(self.calculator.log(2, 4), 0.5)

    def test_log_result_is_fraction(self):
        self.assertAlmostEqual(self.calculator.log(0.5, 2), -1)

    def test_log_fraction(self):
        self.assertAlmostEqual(self.calculator.log(2, 0.5), -1)

    def test_log_exp(self):
        self.assertAlmostEqual(self.calculator.log(math.exp(2), math.exp(1)), 2)

    def test_log_ln_is_fraction(self):
        self.assertAlmostEqual(self.calculator.log(math.exp(1), math.exp(2)), 0.5)

    def test_log_zero(self):
        with self.assertRaises(Exception) as cm:
            self.calculator.log(0, 2)

    def test_log_num_is_one(self):
        with self.assertRaises(Exception) as cm:
            self.calculator.log(2, 1)

    # Sqrt

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_zero(self):
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_one(self):
        self.assertAlmostEqual(self.calculator.sqrt(1), 1)

    def test_sqrt_fraction(self):
        self.assertAlmostEqual(self.calculator.sqrt(0.25), 0.5)

    # Nth root

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(4, 2), 2)

    def test_nth_root_zero(self):
        self.assertAlmostEqual(self.calculator.nth_root(0, 3), 0)

    def test_nth_root_one(self):
        self.assertAlmostEqual(self.calculator.nth_root(1, 4), 1)

    def test_nth_root_fractiom(self):
        self.assertAlmostEqual(self.calculator.nth_root(0.25, 2), 0.5)


if __name__ == "__main__":
    unittest.main()
