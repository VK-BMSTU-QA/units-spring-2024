import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_ints(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_add_negatives(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_floats(self):
        self.assertAlmostEqual(self.calculator.addition(0.1, 0.2), 0.3)
    
    def test_add_int_float(self):
        self.assertAlmostEqual(self.calculator.addition(1, 0.1), 1.1)

    def test_add_inf_int(self):
        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)

    def test_add_infs(self):
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf) 
    
    def test_add_strings(self):
        self.assertEqual(self.calculator.addition('a', 'b'), 'ab')
    
    def test_add_lists(self):
        self.assertEqual(self.calculator.addition([1, 2], [3]), [1, 2, 3])
    
    def test_add_tuples(self):
        self.assertEqual(self.calculator.addition((1, 2), (3, 4)), (1, 2, 3, 4))
    
    def test_add_sets(self):
        self.assertRaises(TypeError, self.calculator.addition, {1, 2}, {3, 4})

    def test_add_dicts(self):
        self.assertRaises(TypeError, self.calculator.addition, {'a': 1}, {'b': 2})


    def test_sub_int(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)

    def test_sub_floats(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.3, 0.2), 0.1)
    
    def test_sub_float_int(self):
        self.assertAlmostEqual(self.calculator.subtraction(1, 0.1), 0.9)
    
    def test_sub_inf_int(self):
        self.assertEqual(self.calculator.subtraction(math.inf, 9999999999), math.inf)
    
    def test_sub_int_inf(self):
        self.assertEqual(self.calculator.subtraction(999999999, math.inf), -math.inf)
    
    def test_sub_infs(self):
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))

    def test_sub_strings(self):
        self.assertRaises(TypeError, self.calculator.subtraction, "ab", "b")
    
    def test_sub_lists(self):
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2, 3], [2, 3])

    def test_sub_tuples(self):
        self.assertRaises(TypeError, self.calculator.subtraction, (1, 2, 3), (2, 3))
    
    def test_sub_sets(self):
        self.assertEqual(self.calculator.subtraction({1, 2, 3, 4}, {1, 2}), {3, 4})

    def test_sub_dicts(self):
        self.assertRaises(TypeError, self.calculator.subtraction,{'a': 1, 'b': 2}, {'b': 2})

    
    def test_mul_int(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
    
    def test_mul_int_float(self):
        self.assertAlmostEqual(self.calculator.multiplication(12, 0.1), 1.2)
    
    def test_mul_negatives(self):
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)

    def test_mul_inf_int(self):
        self.assertEqual(self.calculator.multiplication(math.inf, 999999), math.inf)

    def test_mul_infs(self):
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf) 
    
    def test_mul_int_string(self):
        self.assertEqual(self.calculator.multiplication(5, 'a'), 'aaaaa')
    
    def test_mul_strings(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'b')
    
    def test_mul_lists(self):
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2], [3, 4])
    
    def test_mul_tuples(self):
        self.assertRaises(TypeError, self.calculator.multiplication, (1, 2), (3, 4))
    
    def test_mul_sets(self):
        self.assertRaises(TypeError, self.calculator.multiplication, {1, 2}, {3, 4})

    def test_mul_dicts(self):
        self.assertRaises(TypeError, self.calculator.multiplication, {'a': 1}, {'b': 2})
    

    def test_div_ints(self):
        self.assertEqual(self.calculator.division(25, 5), 5)
    
    def test_div_floats(self):
        self.assertAlmostEqual(self.calculator.division(0.2, 0.1), 2.0)
    
    def test_div_zero(self):
        self.assertEqual(self.calculator.division(0, 12), 0)

    def test_div_by_zero(self):
        self.assertIsNone(self.calculator.division(12, 0))
    
    def test_div_negatives(self):
        self.assertEqual(self.calculator.division(-2, -1), 2)
    
    def test_div_int_inf(self):
        self.assertAlmostEqual(self.calculator.division(9999999, math.inf), 0.0)
    
    def test_div_inf_int(self):
        self.assertEqual(self.calculator.division(math.inf, 9999999), math.inf)

    def test_div_infs(self):
        self.assertTrue(math.isnan(self.calculator.division(math.inf, math.inf)))
    
    def test_div_strings(self):
        self.assertRaises(TypeError, self.calculator.division, 'a', 'b')
    
    def test_div_lists(self):
        self.assertRaises(TypeError, self.calculator.division, [1, 2], [3, 4])
    
    def test_div_tuples(self):
        self.assertRaises(TypeError, self.calculator.division, (1, 2), (3, 4))
    
    def test_div_sets(self):
        self.assertRaises(TypeError, self.calculator.division, {1, 2}, {3, 4})

    def test_div_dicts(self):
        self.assertRaises(TypeError, self.calculator.division, {'a': 1}, {'b': 2})

    
    def test_abs_positive(self):
        self.assertEqual(self.calculator.adsolute(1), 1)
    
    def test_abs_negative(self):
        self.assertEqual(self.calculator.adsolute(-1), 1)
    
    def test_abs_eq_pos_neg(self):
        self.assertEqual(self.calculator.adsolute(1), self.calculator.adsolute(-1))
    
    def test_abs_inf(self):
        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)
    
    def test_abs__neg_inf(self):
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)
    
    def test_abs_strings(self):
        self.assertRaises(TypeError, self.calculator.adsolute, 'a')
    
    def test_abs_lists(self):
        self.assertRaises(TypeError, self.calculator.adsolute, [1, 2])
    
    def test_abs_tuples(self):
        self.assertRaises(TypeError, self.calculator.adsolute, (1, 2))
    
    def test_abs_sets(self):
        self.assertRaises(TypeError, self.calculator.adsolute, {1, 2})

    def test_abs_dicts(self):
        self.assertRaises(TypeError, self.calculator.adsolute, {'a': 1})
    

    def test_degree_ints(self):
        self.assertEqual(self.calculator.degree(2, 2), 4)
    
    def test_degree_int_float(self):
        self.assertAlmostEqual(self.calculator.degree(25, 0.5), 5.0)
    
    def test_degree_int_zero(self):
        self.assertEqual(self.calculator.degree(25, 0), 1)

    def test_degree_int_negative(self):
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)

    def test_degree_zero_zero(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)
    
    def test_degree_negative_even_degree(self):
        self.assertEqual(self.calculator.degree(-1, 2), 1)

    def test_degree_one_inf(self):
        self.assertAlmostEqual(self.calculator.degree(1, math.inf), 1.0)

    def test_degree_int_inf(self):
        self.assertEqual(self.calculator.degree(9999999, math.inf), math.inf)
    
    def test_degree_inf_int(self):
        self.assertEqual(self.calculator.degree(math.inf, 9999999), math.inf)
    
    def test_degree_infs(self):
        self.assertEqual(self.calculator.degree(math.inf, math.inf), math.inf)
    
    def test_degree_strings(self):
        self.assertRaises(TypeError, self.calculator.degree, 'a', 'b')
    
    def test_degree_lists(self):
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], [3, 4])
    
    def test_degree_tuples(self):
        self.assertRaises(TypeError, self.calculator.degree, (1, 2), (3, 4))
    
    def test_degree_sets(self):
        self.assertRaises(TypeError, self.calculator.degree, {1, 2}, {3, 4})

    def test_degree_dicts(self):
        self.assertRaises(TypeError, self.calculator.degree, {'a': 1}, {'b': 2})
    

    def test_ln_e_degree(self):
        self.assertAlmostEqual(self.calculator.ln(math.e ** 5), 5.0)
    
    def test_ln_one(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0.0)
    
    def test_ln_inf(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
    
    def test_ln_strings(self):
        self.assertRaises(TypeError, self.calculator.ln, 'a')
    
    def test_ln_lists(self):
        self.assertRaises(TypeError, self.calculator.ln, [1, 2])
    
    def test_ln_tuples(self):
        self.assertRaises(TypeError, self.calculator.ln, (1, 2))
    
    def test_ln_sets(self):
        self.assertRaises(TypeError, self.calculator.ln, {1, 2})

    def test_ln_dicts(self):
        self.assertRaises(TypeError, self.calculator.ln, {'a': 1})
    
    
    def test_log_perfect_dergree(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3.0)
    
    def test_log_one(self):
        self.assertAlmostEqual(self.calculator.log(1, 5), 0.0)
    
    def test_log_int_inf(self):
        self.assertAlmostEqual(self.calculator.log(math.inf, 9999999), math.inf)

    def test_log_inf_int(self):
        self.assertEqual(self.calculator.log(9, math.inf), 0.0)
    
    def test_log_strings(self):
        self.assertRaises(TypeError, self.calculator.log, 'a', 'b')
    
    def test_log_lists(self):
        self.assertRaises(TypeError, self.calculator.log, [1, 2], [3, 4])
    
    def test_log_tuples(self):
        self.assertRaises(TypeError, self.calculator.log, (1, 2), (3, 4))
    
    def test_log_sets(self):
        self.assertRaises(TypeError, self.calculator.log, {1, 2}, {3, 4})

    def test_log_dicts(self):
        self.assertRaises(TypeError, self.calculator.log, {'a': 1}, {'b': 2})
    

    def test_sqrt_int_perfect_square(self):
        self.assertAlmostEqual(self.calculator.sqrt(25), 5.0)

    def test_sqrt_float_perfect_square(self):
        self.assertAlmostEqual(self.calculator.sqrt(0.25), 0.5)
    
    def test_sqrt_one(self):
        self.assertAlmostEqual(self.calculator.sqrt(1), 1)
    
    def test_sqrt_zero(self):
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_inf(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
    
    def test_sqrt_strings(self):
        self.assertRaises(TypeError, self.calculator.sqrt, 'a')
    
    def test_sqrt_lists(self):
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2])
    
    def test_sqrt_tuples(self):
        self.assertRaises(TypeError, self.calculator.sqrt, (1, 2))
    
    def test_sqrt_sets(self):
        self.assertRaises(TypeError, self.calculator.sqrt, {1, 2})

    def test_sqrt_dicts(self):
        self.assertRaises(TypeError, self.calculator.sqrt, {'a': 1})

    
    def test_nth_root_int_perfect_degree(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2.0)
    
    def test_nth_root_1(self):
        self.assertAlmostEqual(self.calculator.nth_root(1, 3), 1.0)
    
    def test_nth_root_int_perfect_degree(self):
        self.assertAlmostEqual(self.calculator.nth_root(0, 3), 0.0)
    
    def test_degree_int_inf(self):
        self.assertAlmostEqual(self.calculator.nth_root(9999999, math.inf), 1.0)
    
    def test_degree_inf_int(self):
        self.assertEqual(self.calculator.nth_root(math.inf, 9999999), math.inf)
    
    def test_degree_infs(self):
        self.assertAlmostEqual(self.calculator.nth_root(math.inf, math.inf), 1.0)

    def test_nth_root_strings(self):
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 'b')
    
    def test_nth_root_lists(self):
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2], [3, 4])
    
    def test_nth_root_tuples(self):
        self.assertRaises(TypeError, self.calculator.nth_root, (1, 2), (3, 4))
    
    def test_nth_root_sets(self):
        self.assertRaises(TypeError, self.calculator.nth_root, {1, 2}, {3, 4})

    def test_nth_root_dicts(self):
        self.assertRaises(TypeError, self.calculator.nth_root, {'a': 1}, {'b': 2})

if __name__ == "__main__":
    unittest.main()
