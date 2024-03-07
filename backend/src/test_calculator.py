import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(-1, 5), 4)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(-5, -10), -15)
        self.assertEqual(self.calculator.addition(10, -10), 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)
        self.assertEqual(self.calculator.multiplication(5, 0), 0)
        self.assertEqual(self.calculator.multiplication(-2, 4), -8)
        self.assertEqual(self.calculator.multiplication(0, 10), 0)
        self.assertEqual(self.calculator.multiplication(-3, -5), 15)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 2), 3)
        self.assertEqual(self.calculator.subtraction(-1, -5), 4)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(10, -10), 20)
        self.assertEqual(self.calculator.subtraction(-10, -5), -5)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertIsNone(self.calculator.division(6, 0))
        self.assertAlmostEqual(self.calculator.division(10, 3), 10/3)
        self.assertAlmostEqual(self.calculator.division(-6, 2), -3)
        self.assertAlmostEqual(self.calculator.division(-6, -2), 3)

    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(10), 10)
        self.assertEqual(self.calculator.adsolute(-100), 100)
        self.assertEqual(self.calculator.adsolute(0.5), 0.5)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(0, 2), 0)
        self.assertEqual(self.calculator.degree(1, 100), 1)
        self.assertEqual(self.calculator.degree(-2, 3), -8)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(2.718281828), 1)
        self.assertAlmostEqual(self.calculator.ln(10), 2.302585093)
        self.assertAlmostEqual(self.calculator.ln(100), 4.605170186)
        self.assertAlmostEqual(self.calculator.ln(0.5), -0.693147181)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(1, 10), 0)
        self.assertAlmostEqual(self.calculator.log(10, 10), 1)
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3)
        self.assertAlmostEqual(self.calculator.log(1, 2), 0)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(16), 4)
        self.assertAlmostEqual(self.calculator.sqrt(25), 5)
        self.assertAlmostEqual(self.calculator.sqrt(36), 6)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(self.calculator.nth_root(27, 3), 3)
        self.assertAlmostEqual(self.calculator.nth_root(64, 3), 4)
        self.assertAlmostEqual(self.calculator.nth_root(125, 3), 5)
        self.assertAlmostEqual(self.calculator.nth_root(0, 5), 0)

if __name__ == "__main__":
    unittest.main()
