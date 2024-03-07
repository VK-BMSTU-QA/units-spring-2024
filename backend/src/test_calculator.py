import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_addition__negative_numbers(self):
        self.assertEqual(self.calculator.addition(-3, -5), -8)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)

    def test_subtraction__negative_number(self):
        self.assertEqual(self.calculator.subtraction(5, -3), 8)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2)

    def test_division__zero(self):
        self.assertIsNone(self.calculator.division(6, 0))

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(-5), 5)

    def test_absolute__zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)

    def test_degree__negative_in_value(self):
        self.assertEqual(self.calculator.degree(-3, 2), 9)

    def test_degree__negative_in_degree(self):
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

    def test_degree__negative_in_degree_and_value(self):
        self.assertEqual(self.calculator.degree(-2, -2), -0.25)

    def test_degree__zero_in_value(self):
        self.assertEqual(self.calculator.degree(0, 6), 0)

    def test_degree__zero_in_degree(self):
        self.assertEqual(self.calculator.degree(2, 0), 1)

    def test_degree__zero_in_degree_and_value(self):
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)

    def test_log_negative_argument(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-10, 2)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(9), 3)

    def test_sqrt__zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_negative_number(self):
        with self.assertRaises(ValueError):
            self.calculator.sqrt(-9)

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)

if __name__ == "__main__":
    unittest.main()
