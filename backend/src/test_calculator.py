import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    # тесты функции add
    def test_add_int(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_none(self):
        self.assertRaises(TypeError, self.calculator.addition, None, 1)

    def test_add_none_str(self):
        self.assertRaises(TypeError, self.calculator.addition, None, "1")

    def test_add_int_comm(self):
        self.assertEqual(self.calculator.addition(2, 1), 3)

    def test_add_neg(self):
        self.assertEqual(self.calculator.addition(-1, 2), 1)

    def test_add_neg_comm(self):
        self.assertEqual(self.calculator.addition(2, -1), 1)

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(2, 0), 2)

    def test_add_one_float(self):
        self.assertAlmostEqual(self.calculator.addition(2.3, 3), 5.3)

    def test_add_two_float(self):
        self.assertAlmostEqual(self.calculator.addition(2.3, 3.1), 5.4)

    # тесты функции mul
    def test_mul_int(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)

    def test_mul_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, None, 1)

    def test_mul_lst_str(self):
        self.assertRaises(TypeError, self.calculator.multiplication, [], "")

    def test_mul_lst_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, [], None)

    def test_mul_int_comm(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(10, 0), 0)

    def test_mul_one_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(10.1, 2), 20.2)

    def test_mul_two_float(self):
        result = 10.1 * 2.1
        self.assertAlmostEqual(self.calculator.multiplication(10.1, 2.1), result)

    def test_mul_neg(self):
        result = -10 * 2
        self.assertEqual(self.calculator.multiplication(-10, 2), result)

    def test_mul_one_float_neg(self):
        result = -10.2 * 2
        self.assertAlmostEqual(self.calculator.multiplication(-10.2, 2), result)

    def test_mul_two_float_neg(self):
        result = -10.2 * 2.1
        self.assertAlmostEqual(self.calculator.multiplication(-10.2, 2.1), result)

    def test_mul_two_float_two_neg(self):
        result = -10.2 * -2.1
        self.assertAlmostEqual(self.calculator.multiplication(-10.2, -2.1), result)

    # тесты функции sub
    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    def test_sub_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)

    def test_sub_lst_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [], 1)

    def test_sub_neg(self):
        self.assertEqual(self.calculator.subtraction(3, -2), 5)

    def test_sub_two_neg(self):
        self.assertEqual(self.calculator.subtraction(-3, -2), -1)

    def test_sub_res_neg(self):
        self.assertEqual(self.calculator.subtraction(1, -2), 3)

    def test_sub_res_zero(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)

    def test_sub_two_floats(self):
        result = 3.1 - 2.1
        self.assertEqual(self.calculator.subtraction(3.1, 2.1), result)

    # тесты функции div
    def test_div(self):
        result = 3 / 2
        self.assertAlmostEqual(self.calculator.division(3, 2), result)

    def test_div_none(self):
        self.assertRaises(TypeError, self.calculator.division, 1, None)

    def test_div_lst_none(self):
        self.assertRaises(TypeError, self.calculator.division, [], None)

    def test_div_period(self):
        result = 1 / 3
        self.assertAlmostEqual(self.calculator.division(1, 3), result)

    def test_div_one_float(self):
        result = 3.2 / 2
        self.assertAlmostEqual(self.calculator.division(3.2, 2), result)
    
    def test_div_one_neg(self):
        result = -3 / 2
        self.assertAlmostEqual(self.calculator.division(-3, 2), result)

    def test_div_one_neg_one_float(self):
        result = -3.2 / 2
        self.assertAlmostEqual(self.calculator.division(-3.2, 2), result)

    def test_div_two_neg_one_float(self):
        result = -3.2 / -2
        self.assertAlmostEqual(self.calculator.division(-3.2, -2), result)

    def test_div_two_neg_one_float(self):
        result =  -3.2 / -2.2
        self.assertAlmostEqual(self.calculator.division(-3.2, -2.2), result)

    def test_div_zero(self):
        self.assertEqual(self.calculator.division(10, 0), None)
    
    # тесты на функцию abs
    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(3), 3)

    def test_abs_none(self):
        self.assertRaises(TypeError, self.calculator.adsolute, None)
    
    def test_abs_lst(self):
        self.assertRaises(TypeError, self.calculator.adsolute, [])

    def test_abs_neg(self):
        self.assertEqual(self.calculator.adsolute(-3), 3)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    # тесты на функцию deg
    def test_deg(self):
        result = 3 ** 2
        self.assertEqual(self.calculator.degree(3, 2), result)

    def test_deg_none(self):
        self.assertRaises(TypeError, self.calculator.degree, 1, None)
    
    def test_deg_lst_none(self):
        self.assertRaises(TypeError, self.calculator.degree,[], None)
    
    def test_deg_neg_deegre(self):
        result = 3 ** -2
        self.assertAlmostEqual(self.calculator.degree(3, -2), result)

    def test_deg_neg_num(self):
        result = (-3) ** 2
        self.assertEqual(self.calculator.degree(-3, 2), result)

    def test_deg_float_negs(self):
        result = (-3.1) ** (-2)
        self.assertAlmostEqual(self.calculator.degree(-3.1, -2), result)
        
    # тесты на функцию ln
    def test_ln(self):
        result = math.log(2)
        self.assertAlmostEqual(self.calculator.ln(2), result)

    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)
    
    def test_ln_lst(self):
        self.assertRaises(TypeError, self.calculator.ln, [])

    def test_ln_float(self):
        result = math.log(2.1)
        self.assertAlmostEqual(self.calculator.ln(2.1), result)

    # тесты на функцию log
    def test_log_float(self):
        result =  math.log(2, 1.1)
        self.assertAlmostEqual(self.calculator.log(2, 1.1), result)

    def test_ln_none_lst(self):
        self.assertRaises(TypeError, self.calculator.log, None, [])

    def test_log(self):
        result =  math.log(2, 2)
        self.assertAlmostEqual(self.calculator.log(2, 2), result)

    def test_log_period(self):
        result =  math.log(2, 1.5)
        self.assertAlmostEqual(self.calculator.log(2, 1.5), result)

    def test_log_neg_deg(self):
        with self.assertRaises(ValueError): 
            self.calculator.log(1, -5)

    def test_log_neg_num(self):
        with self.assertRaises(ValueError): 
            self.calculator.log(-1, 5)

    def test_log_two_neg(self):
        with self.assertRaises(ValueError): 
            self.calculator.log(-1, -5)

    # тесты на функцию sqrt
    def test_sqrt(self):
        r = 2 ** 0.5
        self.assertAlmostEqual(self.calculator.sqrt(2), r)

    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_log_lst(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [])
    
    def test_sqrt_float(self):
        r = 2.1 ** 0.5
        self.assertAlmostEqual(self.calculator.sqrt(2.1), r)

    def test_sqrt_neg(self):
        r = (-2) ** 0.5
        self.assertAlmostEqual(self.calculator.sqrt(-2), r)
    
    # тесты на функцию nth_root
    def test_nth_root(self):
        r = 2 ** (1. / 1)
        self.assertAlmostEqual(self.calculator.nth_root(2, 1), r)
    
    def test_nth_root_lst_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, None, [])

    def test_nth_root_none_lst(self):
        self.assertRaises(TypeError, self.calculator.nth_root, [], None)

    def test_nth_root_neg(self):
        r = (-2) ** (1. / 1)
        self.assertAlmostEqual(self.calculator.nth_root(-2, 1), r)

    def test_nth_root_two_neg(self):
        r = (-2) ** (1. / -1)
        self.assertAlmostEqual(self.calculator.nth_root(-2, -1), r)

    def test_nth_root_float(self):
        r = 2 ** (1. / 3.1)
        self.assertAlmostEqual(self.calculator.nth_root(2, 3.1), r)
    
    def test_nth_root_two_float(self):
        r = 2.1 ** (1. / 3.1)
        self.assertAlmostEqual(self.calculator.nth_root(2.1, 3.1), r)
        


if __name__ == "__main__":
    unittest.main()

