import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
    
    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(5, 6), 30)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(20, 27), -7)

    def test_div(self):
        self.assertEqual(self.calculator.division(30, 6), 5)
        self.assertEqual(self.calculator.division(30, 0), None)

    def test_abs(self):
        self.assertEqual(self.calculator.absolute(4), 4)
        self.assertEqual(self.calculator.absolute(-7), 7)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 10), 1024)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertEqual(self.calculator.log(64, 4), 3)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(625), 25)

    def test_nth_sqrt(self):
        self.assertEqual(self.calculator.nth_root(0, 36), 0)


if __name__ == "__main__":
    unittest.main()
