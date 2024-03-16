import math
import unittest
from .calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    #test add

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_none(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)

    def test_add_fract(self):
        self.assertEqual(self.calculator.addition(1.2, 3.5), 4.7)

    def test_add_types(self):
        self.assertRaises(TypeError, self.calculator.addition, "1", 1)
    
    def test_add_string(self):
        self.assertEqual(self.calculator.addition("1", "3"), "13")

    def test_add_arr(self):
        self.assertRaises(TypeError, self.calculator.addition, [1, 2], 1)
    
    #test multiplication

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-3, -2), 6)

    def test_multiplication_one_negative(self):
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)

    def test_multiplication_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)

    def test_multiplication_inf(self):
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf)

    def test_multiplication_fract(self):
        self.assertEqual(self.calculator.multiplication(1.2, 3.5), 4.2)

    def test_multiplication_fract2natural(self):
        self.assertEqual(self.calculator.multiplication(3, 1.5), 4.5)

    def test_multiplication_string2int(self):
        self.assertEqual(self.calculator.multiplication("3", 2), "33")

    def test_multiplication_string(self):
        self.assertRaises(TypeError, self.calculator.multiplication, "1", "1")

    def test_multiplication_arr(self):
        self.assertEqual(self.calculator.multiplication([1, 2], 2), [1, 2, 1, 2])

    #test subtraction

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(4, 2), 2)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(-4, -2), -2)

    def test_subtraction_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)

    def test_subtraction_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)

    def test_subtraction_fract(self):
        self.assertAlmostEqual(self.calculator.subtraction(4.2, 2.1), 2.1)

    def test_subtraction_types(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "1", 1)

    def test_subtraction_arr(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2], 1)

    #test division

    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)

    def test_division_negative(self):
        self.assertEqual(self.calculator.division(-4, -2), 2)

    def test_division_one_negative(self):
        self.assertEqual(self.calculator.division(4, -2), -2)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(-4, 0), None)

    def test_division_none(self):
        self.assertRaises(TypeError, self.calculator.division, None, None)

    def test_division_inf(self):
        self.assertAlmostEqual(self.calculator.division(2, math.inf), 0)

    def test_division_fract(self):
        self.assertAlmostEqual(self.calculator.division(4.5, 1.5), 3)

    def test_division_period(self):
        self.assertAlmostEqual(self.calculator.division(10, 3), 3.333333333333333333333333333)

    def test_division_types(self):
        self.assertRaises(TypeError, self.calculator.division, "1", 1)

    def test_division_arr(self):
        self.assertRaises(TypeError, self.calculator.division, [1, 2], 1)

    #test adsolute

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(4), 4)

    def test_adsolute_negative(self):
        self.assertEqual(self.calculator.adsolute(-4), 4)

    def test_adsolute_none(self):
        self.assertRaises(TypeError, self.calculator.adsolute, None)

    def test_adsolute_inf(self):
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

    def test_adsolute_fract(self):
        self.assertAlmostEqual(self.calculator.adsolute(4.2), 4.2)

    def test_adsolute_types(self):
        self.assertRaises(TypeError, self.calculator.adsolute, "1")

    def test_adsolute_arr(self):
        self.assertRaises(TypeError, self.calculator.adsolute, [1, 2])

    #test degree

    def test_degree(self):
        self.assertEqual(self.calculator.degree(4, 2), 16)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(-4, 2), 16)

    def test_degree_negative_degree(self):
        self.assertEqual(self.calculator.degree(5, -2), 0.04)

    def test_degree_zero_degree(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_degree_none(self):
        self.assertRaises(TypeError, self.calculator.degree, None, None)

    def test_degree_inf(self):
        self.assertEqual(self.calculator.degree(math.inf, math.inf), math.inf)

    def test_degree_fract(self):
        self.assertAlmostEqual(self.calculator.degree(4.2, 2.1), 20.3621443)

    def test_degree_types(self):
        self.assertRaises(TypeError, self.calculator.degree, "1", 1)

    def test_degree_arr(self):
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], 1)			

    #test ln

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -10)

    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

    def test_ln_fract(self):
        self.assertEqual(self.calculator.ln(2.7), 0.9932517730102834)

    def test_ln_types(self):
        self.assertRaises(TypeError, self.calculator.ln, "1")

    def test_ln_arr(self):
        self.assertRaises(TypeError, self.calculator.ln, [1, 2])

    #test log

    def test_log(self):
        self.assertEqual(self.calculator.log(4, 4), 1)

    def test_log_negative(self):
        self.assertRaises(ValueError, self.calculator.log, -4, -4)
    
    def test_log_less_one(self):
        self.assertEqual(self.calculator.log(2, 4), 0.5)

    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, None, None)

    def test_log_inf(self):
        self.assertEqual(self.calculator.log(math.inf, 3), math.inf)

    def test_log_fract(self):
        self.assertAlmostEqual(self.calculator.log(4.2, 2.1), 1.9342395088803244)

    def test_log_types(self):
        self.assertRaises(TypeError, self.calculator.log, "1", "2")

    def test_log_arr(self):
        self.assertRaises(TypeError, self.calculator.log, [1, 2], 2)

    #test sqrt

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)

    def test_sqrt_negative(self):
        self.assertEqual(self.calculator.sqrt(-4), 1.2246467991473532e-16+2j)

    def test_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

    def test_sqrt_fract(self):
        self.assertAlmostEqual(self.calculator.sqrt(4.2), 2.04939015319192)

    def test_sqrt_fract_result(self):
        self.assertAlmostEqual(self.calculator.sqrt(8), 2.8284271247461903)

    def test_sqrt_types(self):
        self.assertRaises(TypeError, self.calculator.sqrt, "1")

    def test_sqrt_arr(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2])

    #test nth_root

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(4, 2), 2)

    def test_nth_root_negative(self):
        self.assertEqual(self.calculator.nth_root(-4, 2), 1.2246467991473532e-16+2j)

    def test_nth_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, None)

    def test_nth_root_inf(self):
        self.assertEqual(self.calculator.nth_root(math.inf, 10), math.inf)

    def test_nth_root_fract(self):
        self.assertAlmostEqual(self.calculator.nth_root(4.2, 2), 2.04939015)

    def test_nth_root_types(self):
        self.assertRaises(TypeError, self.calculator.nth_root, "1", 1)

    def test_nth_root_arr(self):
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2], 1)



if __name__ == "__main__":
    unittest.main()
