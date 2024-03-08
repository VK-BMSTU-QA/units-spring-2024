import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 4), 5)
        self.assertEqual(self.calculator.addition(2, 1), 3)
        self.assertEqual(self.calculator.addition(-100, 300), 200)
        self.assertEqual(self.calculator.addition(-50, 50), 0)
        self.assertEqual(self.calculator.addition(-2, 1), -1)
        self.assertEqual(self.calculator.addition(1, 0), 1)
        self.assertAlmostEqual(self.calculator.addition(0.1, 1), 1.1, places=7)
        self.assertAlmostEqual(self.calculator.addition(-0.1, 1.1), 1, places=7)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 1)
        self.assertEqual(self.calculator.subtraction(2, 3), -1)
        self.assertEqual(self.calculator.subtraction(3, -2), 5)
        self.assertEqual(self.calculator.subtraction(3, 0), 3)
        self.assertAlmostEqual(self.calculator.subtraction(3, 0.2), 2.8, places=7)
        self.assertAlmostEqual(self.calculator.subtraction(3, -0.2), 3.2, places=7)
        self.assertAlmostEqual(self.calculator.subtraction(3.2, 0.2), 3, places=7)
        self.assertAlmostEqual(self.calculator.subtraction(3.2, -0.2), 3.4, places=7)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(7, 5), 35)
        self.assertEqual(self.calculator.multiplication(8, 5), 40)
        self.assertEqual(self.calculator.multiplication(7, 9), 63)
        self.assertEqual(self.calculator.multiplication(1000, 0), 0)
        self.assertEqual(self.calculator.multiplication(9, -3), -27)
        self.assertEqual(self.calculator.multiplication(2, -1), -2)
        self.assertAlmostEqual(self.calculator.multiplication(2, 0.5), 1, places=7)
        self.assertAlmostEqual(self.calculator.multiplication(2, -0.5), -1, places=7)
        self.assertAlmostEqual(self.calculator.multiplication(2, 0.7), 1.4, places=7)
        self.assertAlmostEqual(self.calculator.multiplication(2, -0.7), -1.4, places=7)

    def test_division(self):
        self.assertEqual(self.calculator.division(3, 3), 1)
        self.assertEqual(self.calculator.division(6, 3), 2)
        self.assertEqual(self.calculator.division(5, 1), 5)
        self.assertEqual(self.calculator.division(0, 5), 0)
        self.assertEqual(self.calculator.division(6, -3), -2)
        self.assertEqual(self.calculator.division(-6, 3), -2)
        self.assertEqual(self.calculator.division(3, 0), None)
        self.assertAlmostEqual(self.calculator.division(5, 2.5), 2, places=7)
        self.assertAlmostEqual(self.calculator.division(5, 2), 2.5, places=7)
        self.assertAlmostEqual(self.calculator.division(2, 5), 0.4, places=7)
        self.assertAlmostEqual(self.calculator.division(5, -2.5), -2, places=7)
        self.assertAlmostEqual(self.calculator.division(-5, 2.5), -2, places=7)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(3), 3)
        self.assertEqual(self.calculator.adsolute(-3), 3)
        self.assertAlmostEqual(self.calculator.adsolute(3.2), 3.2)
        self.assertAlmostEqual(self.calculator.adsolute(-3.2), 3.2)

    def test_degree(self):
        #self.assertEqual(self.calculator.degree(-4, 0.5), None)
        self.assertAlmostEqual(self.calculator.degree(1, 2), 1)
        self.assertAlmostEqual(self.calculator.degree(3, 2), 9)
        self.assertAlmostEqual(self.calculator.degree(3, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(3, 1), 3)
        self.assertAlmostEqual(self.calculator.degree(9, 0.5), 3)
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)
        self.assertAlmostEqual(self.calculator.degree(-2, 2), 4)
        self.assertAlmostEqual(self.calculator.degree(-2, -2), 0.25)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

        self.assertAlmostEqual(self.calculator.ln(math.exp(1)), 1)
        self.assertAlmostEqual(self.calculator.ln(math.exp(2)), 2)

        with self.assertRaises(Exception) as cm:
            self.calculator.ln(-1)

        with self.assertRaises(Exception) as cm:
            self.calculator.ln(0)

    def test_log(self):
        self.assertEqual(self.calculator.log(2, 2), 1)
        self.assertEqual(self.calculator.log(4, 2), 2)
        self.assertEqual(self.calculator.log(1, 2), 0)

        self.assertAlmostEqual(self.calculator.log(2, 4), 0.5)
        self.assertAlmostEqual(self.calculator.log(0.5, 2), -1)
        self.assertAlmostEqual(self.calculator.log(2, 0.5), -1)
        self.assertAlmostEqual(self.calculator.log(math.exp(2), math.exp(1)), 2)
        self.assertAlmostEqual(self.calculator.log(math.exp(1), math.exp(2)), 0.5)

        with self.assertRaises(Exception) as cm:
            self.calculator.log(0, 2)

        with self.assertRaises(Exception) as cm:
            self.calculator.log(2, 1)

    def test_sqrt(self):
        #self.assertEqual(self.calculator.sqrt(-1), None)
        self.assertAlmostEqual(self.calculator.sqrt(4), 2)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(1), 1)
        self.assertAlmostEqual(self.calculator.sqrt(0.25), 0.5)

    def test_nth_root(self):
        #self.assertEqual(self.calculator.sqrt(-1), None)
        self.assertAlmostEqual(self.calculator.nth_root(4, 2), 2)
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(self.calculator.nth_root(0, 3), 0)
        self.assertAlmostEqual(self.calculator.nth_root(1, 4), 1)
        self.assertAlmostEqual(self.calculator.nth_root(0.25, 2), 0.5)
        self.assertAlmostEqual(self.calculator.nth_root(0.125, 3), 0.5)


if __name__ == "__main__":
    unittest.main()
