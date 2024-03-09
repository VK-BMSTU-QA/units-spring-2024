import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(3, 5), 8)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 5), 15)
        self.assertEqual(self.calculator.multiplication(-2, 4), -8)
        self.assertEqual(self.calculator.multiplication(0, 10), 0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
        self.assertEqual(self.calculator.subtraction(3, 5), -2)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 5), 2)
        self.assertEqual(self.calculator.division(7, 2), 3.5)
        self.assertIsNone(self.calculator.division(10, 0))

    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(5), 5)
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(3, -1), 1/3)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0.0)  
        self.assertAlmostEqual(self.calculator.ln(math.e), 1.0) 
        self.assertEqual(self.calculator.ln(10), math.log(10))

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3.0) 
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3.0)  
        self.assertRaises(ValueError, self.calculator.log, 1, -1)
            

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(4), 2.0)  
        self.assertAlmostEqual(self.calculator.sqrt(2), math.sqrt(2)) 

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2.0) 
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3.0) 

if __name__ == "__main__":
    unittest.main()
