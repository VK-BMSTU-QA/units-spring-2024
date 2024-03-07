import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(5, 2), 10)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(50, 5), 45)
    
    def test_division(self):
        self.assertEqual(self.calculator.division(45, 5), 9)
    
    def test_division_null(self):
        self.assertEqual(self.calculator.division(45, 0), None)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-65), 65)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 10), 1024)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertEqual(self.calculator.log(3, 9), 0.5)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
    
    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(16, 4), 2)

if __name__ == "__main__":
    unittest.main()
