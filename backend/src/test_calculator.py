import unittest
import math
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition('a', 'b'), 'ab')
    
        with self.assertRaises(TypeError):
            self.calculator.addition('a', 3)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3,1), 2)

    def test_mltpl(self):
        self.assertEqual(self.calculator.multiplication(3,2), 6)

    def test_div(self):
        self.assertEqual(self.calculator.division(8, 4), 2)
        self.assertEqual(self.calculator.division(5, 0), None)
    
    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(6), 6)
        self.assertEqual(self.calculator.adsolute(-6), 6)
        
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 5), 32)
        self.assertEqual(self.calculator.degree(4, -1), 0.25)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.exp(1)), 1)

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(16), 4)

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(1, 0)


if __name__ == "__main__":
    unittest.main()
