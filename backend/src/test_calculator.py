import unittest
# from src.calculator import Calculator
from calculator import Calculator
from math import exp, sqrt


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 2), 1)
        self.assertEqual(self.calculator.addition(0, 2), 2)

    def test_mult(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
    
    def test_subt(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(1, 1), 0)
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
    
    def test_div(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        # типа проверяем деление с конечной точнотью 
        self.assertAlmostEqual(self.calculator.division(4, 3), 4/3, places=2)
        self.assertAlmostEqual(self.calculator.division(4, 3), 4/3, places=2)
        self.assertIsNone(self.calculator.division(4, 0))

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(4), 4)
        self.assertEqual(self.calculator.adsolute(-4), 4)
    
    def test_deg(self):
        self.assertEqual(self.calculator.degree(2, 1), 2)
        self.assertEqual(self.calculator.degree(2, 2), 4)
        self.assertEqual(self.calculator.degree(2, 0), 1)
    
    def test_ln(self):
        self.assertEqual(self.calculator.ln(exp(2)), 2)
        self.assertEqual(self.calculator.ln(exp(0)), 0)
        self.assertEqual(self.calculator.ln(exp(-1)), -1)

    def test_log(self):
        self.assertEqual(self.calculator.log(2**1, 2), 1)
        self.assertEqual(self.calculator.log(2**5, 2), 5)
        self.assertEqual(self.calculator.log(2**0, 2), 0)
    
    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(3), sqrt(3))
    

if __name__ == "__main__":
    unittest.main()
