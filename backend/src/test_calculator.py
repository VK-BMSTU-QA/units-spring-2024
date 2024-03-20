import unittest
import math
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_null_add(self):
        self.assertEqual(self.calculator.addition(8, 0), 8)

    def test_negative_add(self):
        self.assertEqual(self.calculator.addition(-1, -5), -6)

    def test_str_add(self):
        self.assertEqual(self.calculator.addition('capi', 'bara'), 'capibara')

    def test_fraction_add(self):
        self.assertEqual(self.calculator.addition(5.6, 6.7), 12.3)

    def test_empty_add(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(None, None)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(5, 2), 10)

    def test_null_multiplication(self):
        self.assertEqual(self.calculator.multiplication(0, 2), 0)

    def test_fraction_multiplication(self):
        math.isclose(self.calculator.multiplication(5.6, 2.3), 12.88, abs_tol=1e-9)

    def test_negative_multiplication(self):
        self.assertEqual(self.calculator.multiplication(-5, -2), 10)

    def test_str_multiplication(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication('capibara', 'cool')

    def test_empty_multiplication(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication(None, None)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(50, 5), 45)

    def test_null_subtraction(self):
        self.assertEqual(self.calculator.subtraction(50, 0), 50)

    def test_fraction_subtraction(self):
        self.assertTrue(math.isclose(self.calculator.subtraction(53, 52.3), 0.7, abs_tol=1e-9))

    def test_negative_subtraction(self):
        self.assertEqual(self.calculator.subtraction(-6, -8), 2)

    def test_str_subtraction(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('cat', 'cool')

    def test_empty_subtraction(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction(None, None)
    
    def test_division(self):
        self.assertEqual(self.calculator.division(45, 5), 9)
    
    def test_division_null(self):
        self.assertEqual(self.calculator.division(45, 0), None)
    
    def test_null_division(self):
        self.assertEqual(self.calculator.division(0, 70), 0)

    def test_fraction_division(self):
        self.assertEqual(self.calculator.division(4.4, 2.2), 2)

    def test_period_division(self):
        self.assertEqual(self.calculator.division(471, 900), 0.5233333333333333)

    def test_str_division(self):
        with self.assertRaises(TypeError):
            self.calculator.division('monkey', 'capibara')

    def test_empty_division(self):
        with self.assertRaises(TypeError):
            self.calculator.division(None, None)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-65), 65)

    def test_null_adsolute(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_positive_adsolute(self):
        self.assertEqual(self.calculator.adsolute(55), 55)

    def test_fraction_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-65.5), 65.5)

    def test_str_adsolute(self):
        with self.assertRaises(TypeError):
            self.calculator.adsolute('capibara', 'capibara')

    def test_empty_adsolute(self):
        with self.assertRaises(TypeError):
            self.calculator.adsolute(None, None)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 10), 1024)

    def test_degree_fraction(self):
        self.assertEqual(self.calculator.degree(100, 1.5), 1000)

    def test_fraction_degree(self):
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)

    def test_degree_null(self):
        self.assertEqual(self.calculator.degree(10, 0), 1)

    def test_null_degree(self):
        self.assertEqual(self.calculator.degree(0, 10), 0)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(5, -2), 0.04)

    def test_negative_degree(self):
        self.assertEqual(self.calculator.degree(-5, 2), 25)

    def test_str_degree(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('chipi', 'chipi')

    def test_empty_degree(self):
        with self.assertRaises(TypeError):
            self.calculator.degree(None, None)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_negative_ln(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_null_ln(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_str_ln(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('chapa chapa')

    def test_empty_ln(self):
        with self.assertRaises(TypeError):
            self.calculator.ln(None)

    def test_log(self):
        self.assertEqual(self.calculator.log(3, 9), 0.5)

    def test_fraction_log(self):
        self.assertEqual(self.calculator.log(2.5, 6.25), 0.5)

    def test_null_log(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 9)

    def test_log_null(self):
        with self.assertRaises(ValueError):
            self.calculator.log(8, 0)

    def test_str_log(self):
        with self.assertRaises(TypeError):
            self.calculator.log('dubi', 'dubi')

    def test_log_empty(self):
        with self.assertRaises(TypeError):
            self.calculator.log(None, None)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)

    def test_null_sqrt(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_fraction_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4.84), 2.2)

    def test_sqrt_fraction(self):
        self.assertEqual(self.calculator.sqrt(21), math.sqrt(21))

    def test_str_sqrt(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('daba daba')

    def test_empty_sqrt(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt(None)
    
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2)
    
    def test_null_nth_root(self):
        self.assertEqual(self.calculator.nth_root(0, 4), 0)

    def test_nth_root_null(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(4, 0)
    
    def test_fraction_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16.4, 4), math.pow(16.4, 1/4))

    def test_nth_root_empty(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root(None, None)

    def test_nth_root_str(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('magico', 'mi')

if __name__ == "__main__":
    unittest.main()
