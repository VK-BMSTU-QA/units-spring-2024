import math
import unittest
from src.calculator import Calculator


class Conditions:
    def __init__(self, x1, x2, y):
        self.x1 = x1
        self.x2 = x2
        self.y = y


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        conds = [
            Conditions(1, 2, 3),
            Conditions(0, 0, 0),
            Conditions(-2, 2, 0),
            Conditions(-2, -2, -4),
        ]

        for c in conds:
            self.assertEqual(self.calculator.addition(c.x1, c.x2), c.y)

    def test_multiplication(self):
        conds = [
            Conditions(1, 2, 2),
            Conditions(0, 0, 0),
            Conditions(-2, 2, -4),
            Conditions(-2, -2, 4),
        ]

        for c in conds:
            self.assertEqual(self.calculator.multiplication(c.x1, c.x2), c.y)

    def test_sub(self):
        conds = [
            Conditions(1, 2, -1),
            Conditions(0, 0, 0),
            Conditions(-2, 2, -4),
            Conditions(-2, -2, 0),
        ]

        for c in conds:
            self.assertEqual(self.calculator.subtraction(c.x1, c.x2), c.y)

    def test_division(self):
        conds = [
            Conditions(10, 2, 5),
            Conditions(10, -5, -2),
            Conditions(10, 0, None),
        ]

        for c in conds:
            self.assertEqual(self.calculator.division(c.x1, c.x2), c.y)

    def test_adsolute(self):
        conds = [
            (-1, 1),
            (2, 2),
            (0, 0),
        ]

        for c in conds:
            self.assertEqual(self.calculator.adsolute(c[0]), c[1])

    def test_degree(self):
        conds = [
            Conditions(2, 3, 8),
            Conditions(2, 0, 1),
            Conditions(4, -1, 1 / 4),
        ]

        for c in conds:
            self.assertEqual(self.calculator.degree(c.x1, c.x2), c.y)

    def test_ln(self):
        conds = [
            (math.e, 1),
            (1, 0),
        ]

        for c in conds:
            self.assertEqual(self.calculator.ln(c[0]), c[1])

    def test_log(self):
        conds = [
            Conditions(8, 2, 3),
            Conditions(1, 8, 0),
        ]

        for c in conds:
            self.assertEqual(self.calculator.log(c.x1, c.x2), c.y)

    def test_sqrt(self):
        conds = [
            (16, 4),
            (0, 0),
        ]

        for c in conds:
            self.assertEqual(self.calculator.sqrt(c[0]), c[1])

    def test_nth_root(self):
        conds = [
            Conditions(4, 2, 2),
            Conditions(8, 3, 2),
            Conditions(8, 1, 8),
        ]

        for c in conds:
            self.assertEqual(self.calculator.nth_root(c.x1, c.x2), c.y)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(8, 0)

if __name__ == "__main__":
    unittest.main()
