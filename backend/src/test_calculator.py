import unittest
import math
from backend.src import calculator
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 5), 4)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(-5, -10), -15)
        self.assertEqual(self.calculator.addition(10, -10), 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(5, 0), 0)
        self.assertEqual(self.calculator.multiplication(-2, 4), -8)
        self.assertEqual(self.calculator.multiplication(0, 10), 0)
        self.assertEqual(self.calculator.multiplication(-3, -5), 15)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 2), 3)
        self.assertEqual(self.calculator.subtraction(-1, -5), 4)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(10, -10), 20)
        self.assertEqual(self.calculator.subtraction(-10, -5), -5)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertIsNone(self.calculator.division(6, 0))
        self.assertAlmostEqual(self.calculator.division(10, 3), 10/3)
        self.assertAlmostEqual(self.calculator.division(-6, 2), -3)
        self.assertAlmostEqual(self.calculator.division(-6, -2), 3)

    def test_division_fraction(self):
        self.assertAlmostEqual(self.calculator.division(1, 3), 1/3)
        self.assertAlmostEqual(self.calculator.division(5, 2), 2.5)
        self.assertAlmostEqual(self.calculator.division(8, 4), 2)
        self.assertAlmostEqual(self.calculator.division(100, 7), 100/7)

    def test_division_negative(self):
        self.assertAlmostEqual(self.calculator.division(-10, 3), -10/3)
        self.assertAlmostEqual(self.calculator.division(10, -3), -10/3)
        self.assertAlmostEqual(self.calculator.division(-10, -3), 10/3)

    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(10), 10)
        self.assertEqual(self.calculator.adsolute(-100), 100)
        self.assertEqual(self.calculator.adsolute(0.5), 0.5)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(0, 2), 0)
        self.assertEqual(self.calculator.degree(1, 100), 1)
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(0.5), -0.693147181)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(0.5), math.log(0.5))

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)
        self.assertAlmostEqual(self.calculator.log(10, 10), 1)
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3)
        self.assertAlmostEqual(self.calculator.log(1, 2), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(self.calculator.nth_root(0, 5), 0)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(-1, 5), 4)
        self.assertEqual(self.calculator.addition(10, -10), 0)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, 3), -6)
        self.assertEqual(self.calculator.multiplication(-2, -4), 8)
        self.assertEqual(self.calculator.multiplication(0, -10), 0)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(-5, -2), -3)
        self.assertEqual(self.calculator.subtraction(-10, -5), -5)
        self.assertEqual(self.calculator.subtraction(0, -5), 5)

    def test_absolute_negative(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(-100), 100)
        self.assertEqual(self.calculator.adsolute(-0.5), 0.5)

    def test_degree_negative(self):
        self.assertAlmostEqual(self.calculator.degree(-2, 3), -8)

    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-1)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-100, 10)

    def test_sqrt_negative(self):
        result = self.calculator.sqrt(-9)
        self.assertIsInstance(result, complex)

    def test_nth_root_negative(self):
        result = self.calculator.nth_root(-8, 3)
        self.assertIsInstance(result, complex)

    def test_addition_array(self):
        result = self.calculator.addition([6, 2], [3, 1])
        self.assertEqual(result, [6, 2, 3, 1])

    def test_multiplication_array(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication([6, 2], [3, 1])

    def test_subtraction_array(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction([5, 2], [1, 1])

    def test_division_array(self):
        with self.assertRaises(TypeError):
            self.calculator.division([6, 2], [3, 1])

    def test_absolute_array(self):
        with self.assertRaises(TypeError):
            self.calculator.adsolute([5])

    def test_degree_array(self):
        with self.assertRaises(TypeError):
            self.calculator.degree([2, 3], [2, 3])

    def test_ln_array(self):
        with self.assertRaises(TypeError):
            self.calculator.ln([1, 2])

    def test_log_array(self):
        with self.assertRaises(TypeError):
            self.calculator.log([100, 10], 10)

    def test_sqrt_array(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt([9])

    def test_nth_root_array(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root([8, 3], [2, 3])

    def test_addition_string(self):
        result = self.calculator.addition('2', '3')
        self.assertEqual(result, '23')

    def test_multiplication_string(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication('2', '3')

    def test_subtraction_string(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('2', '3')

    def test_division_string(self):
        with self.assertRaises(TypeError):
            self.calculator.division('6', '2')

    def test_adsolute_string(self):
        with self.assertRaises(TypeError):
            self.calculator.adsolute('5')

    def test_degree_string(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('2', '3')

    def test_ln_string(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('2')

    def test_log_string(self):
        with self.assertRaises(TypeError):
            self.calculator.log('100', '10')

    def test_sqrt_string(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('9')

    def test_nth_root_string(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('8', '3')

    def test_addition_float(self):
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.2), 3.3)

    def test_multiplication_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.5, 2), 3.0)

    def test_subtraction_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(5.5, 2.2), 3.3)

    def test_division_float(self):
        self.assertAlmostEqual(self.calculator.division(6.0, 2.0), 3.0)

    def test_absolute_float(self):
        self.assertAlmostEqual(self.calculator.adsolute(-5.5), 5.5)

    def test_degree_float(self):
        self.assertAlmostEqual(self.calculator.degree(2.0, 3.0), 8.0)

    def test_ln_float(self):
        self.assertAlmostEqual(self.calculator.ln(2.0), 0.6931471805599453)

    def test_log_float(self):
        self.assertAlmostEqual(self.calculator.log(100.0, 10.0), 2.0)

    def test_sqrt_float(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.0), 1.4142135623730951)

    def test_nth_root_float(self):
        self.assertAlmostEqual(self.calculator.nth_root(8.0, 3.0), 2.0)

    def test_addition_infinity(self):
        self.assertEqual(self.calculator.addition(float('inf'), float('inf')), float('inf'))
        self.assertEqual(self.calculator.addition(float('-inf'), float('-inf')), float('-inf'))
        self.assertTrue(math.isnan(self.calculator.addition(float('inf'), float('-inf'))))

    def test_multiplication_infinity(self):
        self.assertEqual(self.calculator.multiplication(float('inf'), float('inf')), float('inf'))
        self.assertEqual(self.calculator.multiplication(float('-inf'), float('-inf')), float('inf'))
        self.assertEqual(self.calculator.multiplication(float('-inf'), 1), float('-inf'))
        self.assertEqual(self.calculator.multiplication(1, float('inf')), float('inf'))
        self.assertEqual(self.calculator.multiplication(float('inf'), -1), float('-inf'))
        self.assertEqual(self.calculator.multiplication(-1, float('-inf')), float('inf'))
        self.assertTrue(math.isnan(self.calculator.multiplication(float('-inf'), 0)))
        self.assertTrue(math.isnan(self.calculator.multiplication(0, float('-inf'))))

    def test_subtraction_infinity(self):
        result = self.calculator.subtraction(float('inf'), float('inf'))
        self.assertTrue(math.isnan(result))
        result = self.calculator.subtraction(float('-inf'), float('-inf'))
        self.assertTrue(math.isnan(result))

    def test_division_infinity(self):
        self.assertEqual(self.calculator.division(float('inf'), 1), float('inf'))
        self.assertEqual(self.calculator.division(float('-inf'), 1), float('-inf'))
        self.assertEqual(self.calculator.division(1, float('inf')), 0)
        self.assertTrue(math.isnan(self.calculator.division(float('inf'), float('inf'))))
        self.assertTrue(math.isnan(self.calculator.division(float('-inf'), float('-inf'))))
        self.assertTrue(math.isnan(self.calculator.division(float('inf'), float('-inf'))))
        self.assertTrue(math.isnan(self.calculator.division(float('-inf'), float('inf'))))

    def test_adsolute_infinity(self):
        self.assertEqual(self.calculator.adsolute(float('inf')), float('inf'))
        self.assertEqual(self.calculator.adsolute(float('-inf')), float('inf'))

    def test_degree_infinity(self):
        self.assertEqual(self.calculator.degree(2, float('inf')), float('inf'))
        self.assertEqual(self.calculator.degree(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.degree(float('-inf'), 2), float('inf'))

    def test_ln_infinity(self):
        self.assertEqual(self.calculator.ln(float('inf')), float('inf'))
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_log_infinity(self):
        self.assertEqual(self.calculator.log(float('inf'), 10), float('inf'))
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)

    def test_sqrt_infinity(self):
        self.assertEqual(self.calculator.sqrt(float('inf')), float('inf'))
        self.assertFalse(math.isnan(self.calculator.sqrt(float('-inf'))))

    def test_nth_root_infinity(self):
        self.assertEqual(self.calculator.nth_root(float('inf'), 3), float('inf'))

    def test_addition_zero(self):
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_subtraction_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_ln_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 10)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 5), 0)

    def test_addition_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.addition('hello', 5)
        with self.assertRaises(TypeError):
            self.calculator.addition({}, 5)
        with self.assertRaises(TypeError):
            self.calculator.addition([], 5)

    def test_multiplication_type_error(self):
        result = self.calculator.multiplication('hello', 2)
        self.assertEqual(result, 'hellohello')
        with self.assertRaises(TypeError):
            self.calculator.multiplication({}, 5)
        result = self.calculator.multiplication([], 5)
        self.assertEqual(result, [])

    def test_subtraction_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('hello', 5)
        with self.assertRaises(TypeError):
            self.calculator.subtraction({}, 5)
        with self.assertRaises(TypeError):
            self.calculator.subtraction([], 5)

    def test_division_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.division('hello', 5)
        with self.assertRaises(TypeError):
            self.calculator.division({}, 5)
        with self.assertRaises(TypeError):
            self.calculator.division([], 5)

    def test_absolute_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.adsolute({})
        with self.assertRaises(TypeError):
            self.calculator.adsolute([])
        with self.assertRaises(TypeError):
            self.calculator.adsolute(())

    def test_degree_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('hello', 5)
        with self.assertRaises(TypeError):
            self.calculator.degree({}, 5)
        with self.assertRaises(TypeError):
            self.calculator.degree([], 5)

    def test_ln_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.ln({})
        with self.assertRaises(TypeError):
            self.calculator.ln([])
        with self.assertRaises(TypeError):
            self.calculator.ln(())

    def test_log_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.log('hello', 5)
        with self.assertRaises(TypeError):
            self.calculator.log({}, 5)
        with self.assertRaises(TypeError):
            self.calculator.log([], 5)

    def test_sqrt_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt({})
        with self.assertRaises(TypeError):
            self.calculator.sqrt([])
        with self.assertRaises(TypeError):
            self.calculator.sqrt(())

    def test_nth_root_type_error(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('hello', 5)
        with self.assertRaises(TypeError):
            self.calculator.nth_root({}, 5)
        with self.assertRaises(TypeError):
            self.calculator.nth_root([], 5)


if __name__ == "__main__":
    unittest.main()
