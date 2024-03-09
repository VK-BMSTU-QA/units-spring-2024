import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()


    #addition tests

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_add_one_negative(self):
        self.assertEqual(self.calculator.addition(-1, 2), 1)

    def test_add_all_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_double(self):
        self.assertAlmostEqual(self.calculator.addition(1.3, 2.4), 3.7)

    def test_add_zero(self):
        self.assertEqual(self.calculator.addition(1, 0), 1)

    def test_add_none(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, None)

    def test_add_inf(self):
        self.assertEqual(self.calculator.addition(1, math.inf), math.inf)
    
    def test_add_string(self):
        self.assertRaises(TypeError, self.calculator.addition, 'abc', 1)


    #miltiplication tests

    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)
    
    def test_mult_one_negative(self):
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)

    def test_mult_all_negative(self):
        self.assertEqual(self.calculator.multiplication(-3, -2), 6)

    def test_mult_double(self):
        self.assertAlmostEqual(self.calculator.multiplication(1.4, 2.2), 3.08)

    def test_mult_zero(self):
        self.assertEqual(self.calculator.multiplication(5, 0), 0)

    def test_mult_none(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 5, None)

    def test_mult_inf(self):
        self.assertEqual(self.calculator.multiplication(5, math.inf), math.inf)
    
    def test_mult_string_number(self):
        self.assertEqual(self.calculator.multiplication('abc', 2), 'abcabc')
    
    def test_mult_string_string(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'abc', 'cba') 

    

    #subtraction tests

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)
    
    def test_sub_one_negative(self):
        self.assertEqual(self.calculator.subtraction(-3, 2), -5)

    def test_sub_all_negative(self):
        self.assertEqual(self.calculator.subtraction(-3, -2), -1)

    def test_sub_double(self):
        self.assertAlmostEqual(self.calculator.subtraction(1.2, 2.4), -1.2)

    def test_sub_zero(self):
        self.assertEqual(self.calculator.subtraction(5, 0), 5)

    def test_sub_none(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 5, None)

    def test_sub_inf(self):
        self.assertEqual(self.calculator.subtraction(100, math.inf), -math.inf)
    
    def test_sub_from_inf(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 100), math.inf)
    
    def test_sub_string(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 'abc', 3)
    

    #division tests

    def test_div(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
    
    def test_div_one_negative(self):
        self.assertEqual(self.calculator.division(-6, 2), -3)

    def test_div_all_negative(self):
        self.assertEqual(self.calculator.division(-6, -2), 3)

    def test_div_double(self):
        self.assertAlmostEqual(self.calculator.division(1.2, 2.4), 0.5)

    def test_div_by_zero(self):
        self.assertEqual(self.calculator.division(5, 0), None)

    def test_div_zero_by_number(self):
        self.assertEqual(self.calculator.division(0, 5), 0)

    def test_div_none(self):
        self.assertRaises(TypeError, self.calculator.division, 5, None)

    def test_div_inf(self):
        self.assertEqual(self.calculator.division(100, math.inf), 0)
    
    def test_div_from_inf(self):
        self.assertEqual(self.calculator.division(math.inf, 100), math.inf)
    
    def test_div_string(self):
        self.assertRaises(TypeError, self.calculator.division, 'abc', 3)
    

    #absolute tests

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(6), 6)
    
    def test_absolute_negative(self):
        self.assertEqual(self.calculator.absolute(-6), 6)

    def test_absolute_double(self):
        self.assertAlmostEqual(self.calculator.absolute(1.2), 1.2)

    def test_absolute_negative_double(self):
        self.assertAlmostEqual(self.calculator.absolute(-1.2), 1.2)

    def test_absolute_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_absolute_none(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    def test_absolute_inf(self):
        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
    
    def test_absolute_string(self):
        self.assertRaises(TypeError, self.calculator.absolute, 'abc')


    #degree tests
    
    def test_degree(self):
        self.assertEqual(self.calculator.degree(6, 2), 36)
    
    def test_degree_negative_degree_base_even(self):
        self.assertEqual(self.calculator.degree(-6, 2), 36)

    def test_degree_negative_degree_base_odd(self):
        self.assertEqual(self.calculator.degree(-6, 3), -216)

    def test_degree_negative_degree(self):
        self.assertEqual(self.calculator.degree(2, -1), 0.5)

    def test_degree_double_base(self):
        self.assertAlmostEqual(self.calculator.degree(1.2, 2), 1.44)

    def test_degree_double_degree(self):
        self.assertAlmostEqual(self.calculator.degree(9, 0.5), 3) 

    def test_degree_zero_degree(self):
        self.assertEqual(self.calculator.degree(5, 0), 1)

    def test_degree_zero_base(self):
        self.assertEqual(self.calculator.degree(0, 5), 0)

    def test_degree_none(self):
        self.assertRaises(TypeError, self.calculator.degree, 5, None)

    def test_degree_inf(self):
        self.assertEqual(self.calculator.degree(100, math.inf), math.inf)
    
    def test_degree_from_inf(self):
        self.assertEqual(self.calculator.degree(math.inf, 100), math.inf)
    
    def test_degree_string(self):
        self.assertRaises(TypeError, self.calculator.degree, 'abc', 3)

    
    #ln tests

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
    
    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -4)

    def test_ln_zero(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)

    def test_ln_none(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
    
    def test_ln_string(self):
        self.assertRaises(TypeError, self.calculator.ln, 'abc')

    
    #log tests

    def test_log(self):
        self.assertEqual(self.calculator.log(4, 2), 2)
    
    def test_log_negative_log_base(self):
        self.assertRaises(ValueError, self.calculator.log, 4, -2)

    def test_log_negative_number(self):
        self.assertRaises(ValueError, self.calculator.log, -4, 2)

    def test_log_double(self):
        self.assertAlmostEqual(self.calculator.log(1.44, 1.2), 2)

    def test_log_zero_number(self):
        self.assertRaises(ValueError, self.calculator.log, 0, 2)

    def test_log_zero_base(self):
        self.assertRaises(ValueError, self.calculator.log, 4, 0)

    def test_log_one_in_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.log, 4, 1)

    def test_log_none(self):
        self.assertRaises(TypeError, self.calculator.log, 5, None)
    
    def test_log_from_inf(self):
        self.assertEqual(self.calculator.log(math.inf, 100), math.inf)
    
    def test_log_string(self):
        self.assertRaises(TypeError, self.calculator.log, 'abc', 3)


    #sqrt tests
        
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(36), 6)

    def test_sqrt_double(self):
        self.assertAlmostEqual(self.calculator.sqrt(1.44), 1.2)

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_none(self):
        self.assertRaises(TypeError, self.calculator.sqrt, None)

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
    
    def test_sqrt_string(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'abc', 3)


    #nth_root tests
    
    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(216, 3), 6)

    def test_nth_root_negative_base(self):
        self.assertAlmostEqual(self.calculator.nth_root(25, -2), 0.2)

    def test_nth_root_double(self):
        self.assertAlmostEqual(self.calculator.nth_root(1.44, 2), 1.2)

    def test_nth_root_double_base(self):
        self.assertAlmostEqual(self.calculator.nth_root(9, 0.5), 81) 

    def test_nth_root_zero_base(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 5, 0)

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 5), 0)

    def test_nth_root_none(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 5, None)

    def test_nth_root_inf(self):
        self.assertEqual(self.calculator.nth_root(100, math.inf), 1)
    
    def test_nth_root_from_inf(self):
        self.assertEqual(self.calculator.nth_root(math.inf, 100), math.inf)
    
    def test_nth_root_string(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'abc', 3)


if __name__ == "__main__":
    unittest.main()
