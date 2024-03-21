import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(0, 90), 90)
        self.assertEqual(self.calculator.addition(34789, -30), 34759)
        self.assertEqual(self.calculator.addition(77447, 677889), 755336)
        self.assertEqual(self.calculator.addition("34789", "-30"), "34789-30")
        self.assertEqual(self.calculator.addition("test", "python"), "testpython")
        self.assertEqual(self.calculator.addition(math.inf, 5404), math.inf)
        self.assertEqual(self.calculator.addition(math.inf, -470067004), math.inf)
        self.assertAlmostEqual(self.calculator.addition(123.99, 0.01), 124)
        self.assertAlmostEqual(self.calculator.addition(12.7, 0.01), 12.71)

    def test_multiplicat(self):
        self.assertEqual(self.calculator.multiplication(1, 4), 4)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 789), 0)
        self.assertEqual(self.calculator.multiplication(34789, -30), -1043670)
        self.assertEqual(self.calculator.multiplication("jjilo", 2), "jjilojjilo")
        self.assertEqual(self.calculator.multiplication(["hello"], 3), ["hello", "hello", "hello"])
        self.assertEqual(self.calculator.multiplication([1, 2], 2), [1, 2, 1, 2])
        self.assertRaises(TypeError, self.calculator.multiplication, "test", "python")
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2, 3], [4, 5, 6])
        self.assertAlmostEqual(self.calculator.multiplication(323.85, 47.8), 15480.03)
        self.assertEqual(self.calculator.multiplication(math.inf, 100), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, -2), -math.inf)
        self.assertTrue(math.isnan(self.calculator.multiplication(math.inf, 0)))

    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(0, 1), -1)
        self.assertEqual(self.calculator.subtraction(34789, -30), 34819)
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2], [1, 2, 1, 2])
        self.assertRaises(TypeError, self.calculator.subtraction, "test", "python")
        self.assertAlmostEqual(self.calculator.subtraction(323.85, 35), 288.85)
        self.assertAlmostEqual(self.calculator.subtraction(12.543, 9.5), 3.043)
        self.assertEqual(self.calculator.subtraction(math.inf, 100), math.inf)
        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))

    def test_div(self):
        self.assertIsNone(self.calculator.division(1, 0), 0)
        self.assertAlmostEqual(self.calculator.division(0, 1), 0)
        self.assertAlmostEqual(self.calculator.division(2, 1), 2)
        self.assertAlmostEqual(self.calculator.division(1, 2), 0.5)
        self.assertAlmostEqual(self.calculator.division(9, 3), 3)
        self.assertAlmostEqual(self.calculator.division(354, 8), 44.25)
        self.assertAlmostEqual(self.calculator.division(58, 7), 8.285714, places=6)
        self.assertAlmostEqual(self.calculator.division(100, 3), 33.3, places=1)
        self.assertRaises(TypeError, self.calculator.division, [1, 2], [1, 2, 1, 2])
        self.assertRaises(TypeError, self.calculator.division, "test", "python")

    def test_deg(self):
        self.assertAlmostEqual(self.calculator.degree(1, 1), 1)
        self.assertAlmostEqual(self.calculator.degree(1, 2), 1)
        self.assertAlmostEqual(self.calculator.degree(2, 1), 2)
        self.assertAlmostEqual(self.calculator.degree(0, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)
        self.assertAlmostEqual(self.calculator.degree(-2, 9), -512)
        self.assertAlmostEqual(self.calculator.degree(81, 0.5), 9)
        self.assertAlmostEqual(self.calculator.degree(789008, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(3, -3.2), 0.02973, places=4)
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], [1, 2, 1, 2])
        self.assertRaises(TypeError, self.calculator.degree, "test", "python")

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertAlmostEqual(self.calculator.ln(math.e ** 2), 2)
        self.assertEqual(self.calculator.ln(math.inf), math.inf)
        self.assertRaises(ValueError, self.calculator.ln, -math.inf)
        self.assertRaises(TypeError, self.calculator.ln, [1, 2], [1, 2, 1, 2])
        self.assertRaises(TypeError, self.calculator.ln, "test", "python")

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(4, 2), 2)
        self.assertAlmostEqual(self.calculator.log(6.25, 2.5), 2)
        self.assertAlmostEqual(self.calculator.log(2, 4), 0.5)
        self.assertAlmostEqual(self.calculator.log(0.5, 2), -1)
        self.assertAlmostEqual(self.calculator.log(0.5, 4), -0.5)
        self.assertRaises(ValueError, self.calculator.log, 0, 1)
        self.assertRaises(ValueError, self.calculator.log, 1, 0)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 1, 1)
        self.assertRaises(ValueError, self.calculator.log, -1, 577)
        self.assertRaises(TypeError, self.calculator.log, [1, 2], [1, 2, 1, 2])
        self.assertRaises(TypeError, self.calculator.log, "test", "python")


    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(1), 1)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(6.25), 2.5)
        self.assertAlmostEqual(self.calculator.sqrt(0.25), 0.5)
        self.assertAlmostEqual(self.calculator.sqrt(13), 3.60555, places=4)
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2])
        self.assertRaises(TypeError, self.calculator.sqrt, "test")

    def nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(1, 2), 1)
        self.assertAlmostEqual(self.calculator.nth_root(1, -2), 1)
        self.assertAlmostEqual(self.calculator.nth_root(4, 2), 2)
        self.assertAlmostEqual(self.calculator.nth_root(4, -2), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(6.25, -2), 0.4)
        self.assertAlmostEqual(self.calculator.nth_root(3.2, 8.7), 1.1430447, places=6)
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2], [1, 2, 1, 2])
        self.assertRaises(TypeError, self.calculator.nth_root, "test", "python")

if __name__ == "__main__":
    unittest.main()
