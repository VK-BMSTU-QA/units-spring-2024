import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_add_type_string(self):
        with self.assertRaises(Exception):
            self.calculator.addition("5", 3)

    def test_add_type_list(self):     
        with self.assertRaises(Exception):
            self.calculator.addition([], 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(5,4), 20)
        self.assertEqual(self.calculator.multiplication(4, 5), 20)
        self.assertEqual(self.calculator.multiplication(228, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 228), 0)
        self.assertEqual(self.calculator.multiplication(5, 1), 5)
        self.assertEqual(self.calculator.multiplication(1, 5), 5)
        self.assertEqual(self.calculator.multiplication(-5, 4), -20)
        self.assertEqual(self.calculator.multiplication(-5, -4), 20)

    # def test_multiplication_type_string(self):
    #     with self.assertRaises(Exception):
    #         self.calculator.multiplication("5", 3)

    # def test_multiplication_type_list(self):      
    #     with self.assertRaises(Exception):
    #         self.calculator.multiplication([], 3)
    
    def test_substraction(self):
        self.assertEqual(self.calculator.subtraction(5, 4), 1)
        self.assertEqual(self.calculator.subtraction(4, 5), -1)

    def test_substraction_type_string(self):
        with self.assertRaises(Exception):
            self.calculator.subtraction("5", 3)
    def test_substraction_type_list(self):
        with self.assertRaises(Exception):
            self.calculator.subtraction([], 3)

    def test_division(self):
        self.assertEqual(self.calculator.division(1, 5), 0.2)
        self.assertEqual(self.calculator.division(5, 1), 5)

    def test_division_type_string(self):
        with self.assertRaises(Exception):
            self.calculator.division("5", 3)
    def test_division_type_list(self):
        with self.assertRaises(Exception):
            self.calculator.division([], 3)
    # def test_division_denominator_zero(self):
    #     with self.assertRaises(Exception):
    #         self.calculator.division(7, 0)

    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(5), 5)

    def test_absolute_type_list(self):
        with self.assertRaises(Exception):
            self.calculator.adsolute([])

    def test_absolute_type_string(self):
        with self.assertRaises(Exception):
            self.calculator.adsolute("3") 

    def test_degree(self):
        self.assertEqual(self.calculator.degree(5, 3), 125)
        self.assertEqual(self.calculator.degree(1, 9999), 1)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertEqual(self.calculator.degree(2, -2), 0.25)
        self.assertEqual(self.calculator.degree(0, 0), 1)
    
    def test_degree_type_string(self):
        with self.assertRaises(Exception):
            self.calculator.degree("3", 3)
    
    def test_degree_type_list(self):
        with self.assertRaises(Exception):
            self.calculator.degree([], 3)
        
    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(5), 1.6, delta=0.1)
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_zero(self):
        with self.assertRaises(Exception):
            self.calculator.ln(0)

    def test_ln_negative(self):
        with self.assertRaises(Exception):
            self.calculator.ln(-3)
            
    def test_log(self):
        self.assertEqual(self.calculator.log(10, 10), 1)
        self.assertAlmostEqual(self.calculator.log(5, math.e), 1.6, delta=0.1)
        self.assertEqual(self.calculator.log(1, 7), 0)

    def test_log_zero(self):
        with self.assertRaises(Exception):
            self.calculator.log(0, 5)

    def test_log_one_base(self):
        with self.assertRaises(Exception):
            self.calculator.log(5, 1)

    def test_log_negative(self):
        with self.assertRaises(Exception):
            self.calculator.log(-3, 3)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(0), 0)
        
    # def test_sqrt_negative(self):
    #     with self.assertRaises(Exception):
    #         self.calculator.sqrt(-3)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(9, 2), 3)
        self.assertEqual(self.calculator.nth_root(1, 2), 1)
        self.assertEqual(self.calculator.nth_root(0, 9), 0)
        self.assertEqual(self.calculator.nth_root(10, 1), 10)
        self.assertEqual(self.calculator.nth_root(10, 0.5), 100)
        self.assertEqual(self.calculator.nth_root(16, -2), 0.25)
        
    # def test_nth_root_negative(self):
    #     with self.assertRaises(Exception):
    #         self.calculator.nth_root(-3, 4)


    
    # def test_substraction(self):
    #     self.assertAlmostEqual

if __name__ == "__main__":
    unittest.main()
