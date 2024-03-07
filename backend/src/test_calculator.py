import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(0, 90), 90)
        self.assertEqual(self.calculator.addition(34789, -30), 34759)
        self.assertEqual(self.calculator.addition(77447, 677889), 755336)

    def test_multiplicat(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 1), 0)
        self.assertEqual(self.calculator.multiplication(34789, -30), -1043670)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtraction(1, 2), 2)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(0, 1), 0)
        self.assertEqual(self.calculator.subtraction(34789, -30), -1043670)

    def test_divis(self):
        self.assertEqual(self.calculator.division(1, 2), 2)
        self.assertEqual(self.calculator.division(0, 0), 0)
        self.assertEqual(self.calculator.division(0, 1), 0)
        self.assertEqual(self.calculator.division(34789, -30), -1043670)

    def test_deg(self):
        self.assertEqual(self.calculator.degree(1, 2), 2)
        self.assertEqual(self.calculator.degree(0, 0), 0)
        self.assertEqual(self.calculator.degree(0, 1), 0)
        self.assertEqual(self.calculator.degree(34789, -30), -1043670)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1, 2), 2)
        self.assertEqual(self.calculator.ln(0, 0), 0)
        self.assertEqual(self.calculator.ln(0, 1), 0)
        self.assertEqual(self.calculator.ln(34789, -30), -1043670)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(1, 2), 2)
        self.assertEqual(self.calculator.sqrt(0, 0), 0)
        self.assertEqual(self.calculator.sqrt(0, 1), 0)
        self.assertEqual(self.calculator.sqrt(34789, -30), -1043670)

    def nth_root(self):
        self.assertEqual(self.calculator.nth_root(1, 2), 2)
        self.assertEqual(self.calculator.nth_root(0, 0), 0)
        self.assertEqual(self.calculator.nth_root(0, 1), 0)
        self.assertEqual(self.calculator.nth_root(34789, -30), -1043670)


if __name__ == "__main__":
    unittest.main()
