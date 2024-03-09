import math
import unittest
from .calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertRaises(TypeError, self.calculator.addition, None, None)
        self.assertEqual(self.calculator.addition(math.inf, math.inf), math.inf)
        self.assertEqual(self.calculator.addition(1.2, 3.5), 4.7)
        self.assertRaises(TypeError, self.calculator.addition, "1", 1)
        self.assertEqual(self.calculator.addition("1", "3"), "13")
    
    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)
        self.assertEqual(self.calculator.multiplication(-3, -2), 6)
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)
        self.assertEqual(self.calculator.multiplication(math.inf, math.inf), math.inf)
        self.assertEqual(self.calculator.multiplication(1.2, 3.5), 4.2)
        self.assertEqual(self.calculator.multiplication(3, 1.5), 4.5)
        self.assertEqual(self.calculator.multiplication("3", 2), "33")
        self.assertRaises(TypeError, self.calculator.multiplication, "1", "1")

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(4, 2), 2)
        self.assertEqual(self.calculator.subtraction(-4, -2), -2)
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)
        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)
        self.assertAlmostEqual(self.calculator.subtraction(4.2, 2.1), 2.1)
        self.assertRaises(TypeError, self.calculator.subtraction, "1", 1)

    def test_division(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertEqual(self.calculator.division(-4, -2), 2)
        self.assertEqual(self.calculator.division(4, -2), -2)
        self.assertEqual(self.calculator.division(-4, 0), None)
        self.assertRaises(TypeError, self.calculator.division, None, None)
        self.assertAlmostEqual(self.calculator.division(2, math.inf), 0)
        self.assertAlmostEqual(self.calculator.division(4.5, 1.5), 3)
        self.assertRaises(TypeError, self.calculator.division, "1", 1)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(4), 4)
        self.assertEqual(self.calculator.adsolute(-4), 4)
        self.assertRaises(TypeError, self.calculator.adsolute, None)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.adsolute(4.2), 4.2)
        self.assertRaises(TypeError, self.calculator.adsolute, "1")

    def test_degree(self):
        self.assertEqual(self.calculator.degree(4, 2), 16)
        self.assertEqual(self.calculator.degree(-4, 2), 16)
        self.assertEqual(self.calculator.degree(5, -2), 0.04)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertRaises(TypeError, self.calculator.degree, None, None)
        self.assertEqual(self.calculator.degree(math.inf, math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.degree(4.2, 2.1), 20.3621443)
        self.assertRaises(TypeError, self.calculator.degree, "1", 1)				

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertRaises(ValueError, self.calculator.ln, -10)
        self.assertRaises(TypeError, self.calculator.ln, None)
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.ln, "1")

    def test_log(self):
        self.assertEqual(self.calculator.log(4, 4), 1)
        self.assertRaises(ValueError, self.calculator.log, -4, -4)
        self.assertRaises(TypeError, self.calculator.log, None, None)
        self.assertEqual(self.calculator.log(math.inf, 3), math.inf)
        self.assertAlmostEqual(self.calculator.log(4.2, 2.1), 1.9342395088803244)
        self.assertRaises(TypeError, self.calculator.log, "1", "2")

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(-4), 1.2246467991473532e-16+2j)
        self.assertRaises(TypeError, self.calculator.sqrt, None)
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.sqrt(4.2), 2.04939015319192)
        self.assertRaises(TypeError, self.calculator.sqrt, "1")

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(4, 2), 2)
        self.assertEqual(self.calculator.nth_root(-4, 2), 1.2246467991473532e-16+2j)
        self.assertRaises(TypeError, self.calculator.nth_root, None, None)
        self.assertEqual(self.calculator.nth_root(math.inf, 10), math.inf)
        self.assertAlmostEqual(self.calculator.nth_root(4.2, 2), 2.04939015)
        self.assertRaises(TypeError, self.calculator.nth_root, "1", 1)



if __name__ == "__main__":
    unittest.main()
