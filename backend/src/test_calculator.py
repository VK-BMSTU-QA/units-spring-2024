import unittest
import math
from .calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertAlmostEqual(self.calculator.addition(1.5, 1.5), 3)
        self.assertEqual(self.calculator.addition(math.inf, 5), math.inf)
        self.assertRaises(TypeError, self.calculator.adsolute, 1, None)
        self.assertRaises(TypeError, self.calculator.adsolute, '1', '12')
        
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(5, 5), 25)
        self.assertEqual(self.calculator.multiplication(-1, -1), 1)
        self.assertAlmostEqual(self.calculator.multiplication(2.5, 2), 5)
        self.assertEqual(self.calculator.multiplication(100, 0), 0)
        self.assertEqual(self.calculator.multiplication(math.inf, 2), math.inf)
        self.assertRaises(TypeError, self.calculator.multiplication, 1, None)
        
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(10, 5), 5)
        self.assertEqual(self.calculator.subtraction(-1, -1), 0)
        self.assertAlmostEqual(self.calculator.subtraction(1, 0.5), 0.5)
        self.assertAlmostEqual(self.calculator.subtraction(math.inf, 0.5), math.inf)
        self.assertRaises(TypeError, self.calculator.subtraction, 1, None)
        self.assertRaises(TypeError, self.calculator.subtraction, '1', 2)
        
    def test_division(self):
        self.assertEqual(self.calculator.division(10, 5), 2)
        self.assertEqual(self.calculator.division(5, 0), None)
        self.assertEqual(self.calculator.division(10, math.inf), 0)
        self.assertRaises(TypeError, self.calculator.division, None, 1)
        self.assertRaises(TypeError, self.calculator.division, '11', 1)
        
    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(-1), 1)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(1), 1)
        self.assertRaises(TypeError, self.calculator.adsolute, '-1')
        
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertAlmostEqual(self.calculator.degree(4.0, 0.5), 2.0)
        self.assertAlmostEqual(self.calculator.degree(4.0, -1), 0.25)
        self.assertRaises(TypeError, self.calculator.degree, '1', 2)
        self.assertRaises(TypeError, self.calculator.degree, 1, None)
        
    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(TypeError, self.calculator.ln, None)
        self.assertRaises(TypeError, self.calculator.ln, '12')
            
    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)
        self.assertRaises(ValueError, self.calculator.log, -10, 1)
        self.assertRaises(ValueError, self.calculator.log, 10, 0)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 4, 1)
        self.assertRaises(TypeError, self.calculator.log, '123', 1)
        self.assertRaises(TypeError, self.calculator.log, None, 1)
            
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertRaises(TypeError, self.calculator.sqrt, None)
            
    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3)
        self.assertAlmostEqual(self.calculator.nth_root(16, 0.5), 256)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 16, 0)
