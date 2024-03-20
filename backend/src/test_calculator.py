import math
import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.9), 4.0)
        self.assertEqual(self.calculator.addition(-2, 2), 0)
        self.assertEqual(self.calculator.addition('a', 'b'), 'ab')
        self.assertEqual(self.calculator.addition([1, 2], [3]), [1, 2, 3])
        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)
        self.assertRaises(TypeError, self.calculator.addition, 1, 'string')
        self.assertRaises(TypeError, self.calculator.addition, 1, [2, 3])

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)
        self.assertEqual(self.calculator.multiplication(3, 's'), 'sss')
        self.assertEqual(self.calculator.multiplication(3, [0]), [0, 0, 0])
        self.assertEqual(self.calculator.multiplication(2, math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.multiplication(1.1, 2.5), 2.75)

        self.assertRaises(TypeError, self.calculator.multiplication, 'a', 'string')
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 3], [2, 4])

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 2), 0)
        self.assertEqual(self.calculator.subtraction(2, -2), 4)
        self.assertEqual(self.calculator.subtraction(-2, -2), 0)
        self.assertEqual(self.calculator.subtraction(-2, math.inf), -math.inf)

        self.assertAlmostEqual(self.calculator.subtraction(2.1, 2.1), 0.0)
        self.assertAlmostEqual(self.calculator.subtraction(2.1, -2.1), 4.2)

        self.assertRaises(TypeError, self.calculator.subtraction, 1, 'string')
        self.assertRaises(TypeError, self.calculator.subtraction, 'a', 'string')
        self.assertRaises(TypeError, self.calculator.subtraction, 1, [2, 3])
        self.assertRaises(TypeError, self.calculator.subtraction, [1], [2, 3])

    def test_division(self):
        self.assertEqual(self.calculator.division(8, 2), 4)
        self.assertEqual(self.calculator.division(-8, 2), -4)
        self.assertEqual(self.calculator.division(-8, -2), 4)
        self.assertEqual(self.calculator.division(math.inf, 5), math.inf)
        self.assertAlmostEqual(self.calculator.division(-8, math.inf), 0)
        self.assertAlmostEqual(self.calculator.division(8.4, 4.2), 2.0)
        self.assertAlmostEqual(self.calculator.division(1, 3), 0.3333, places=4)
        self.assertIsNone(self.calculator.division(8, 0))
        self.assertRaises(TypeError, self.calculator.division, 1, 'string')
        self.assertRaises(TypeError, self.calculator.division, 'a', 'string')
        self.assertRaises(TypeError, self.calculator.division, 1, [2, 3])
        self.assertRaises(TypeError, self.calculator.division, [1], [2, 3])

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(5), 5)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

        self.assertAlmostEqual(self.calculator.adsolute(-5.1), 5.1)

        self.assertRaises(TypeError, self.calculator.adsolute, 'string')
        self.assertRaises(TypeError, self.calculator.adsolute, [1, 2])

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(-2, 0), 1)
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertAlmostEqual(self.calculator.degree(2, -1), 0.5)
        self.assertAlmostEqual(self.calculator.degree(2, 1.1), 2.14355, places=5)
        self.assertAlmostEqual(self.calculator.degree(1.1, 1.1), 1.11053, places=5)
        self.assertRaises(TypeError, self.calculator.degree, 1, 'string')
        self.assertRaises(TypeError, self.calculator.degree, 'a', 'string')
        self.assertRaises(TypeError, self.calculator.degree, 'a', 1)
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], 1)
        self.assertRaises(TypeError, self.calculator.degree, [1, 2], [1, 2])
        self.assertRaises(TypeError, self.calculator.degree, 1, [1, 2])

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)
        self.assertAlmostEqual(self.calculator.ln(math.e), 1)
        self.assertAlmostEqual(self.calculator.ln(math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.ln(2.71), 0.9969, places=4)

        self.assertRaises(TypeError, self.calculator.ln, 'string')
        self.assertRaises(TypeError, self.calculator.ln, [1, 2])
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(ValueError, self.calculator.ln, -math.inf)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(100, 10), 2)
        self.assertAlmostEqual(self.calculator.log(1.1, 2), 0.1375, places=4)
        self.assertAlmostEqual(self.calculator.log(1.1, 2.2), 0.1209, places=4)
        self.assertAlmostEqual(self.calculator.log(100, math.inf), 0)
        self.assertAlmostEqual(self.calculator.log(math.inf, 2), math.inf)
        self.assertRaises(ValueError, self.calculator.log, -1, 10)
        self.assertRaises(ValueError, self.calculator.log, 0, 10)
        self.assertRaises(ValueError, self.calculator.log, 10, 0)
        self.assertRaises(ValueError, self.calculator.log, -1, 10)
        self.assertRaises(ValueError, self.calculator.log, 10, -1)
        self.assertRaises(ValueError, self.calculator.log, -10.1, 1)
        self.assertRaises(TypeError, self.calculator.log, 1, 'string')
        self.assertRaises(TypeError, self.calculator.log, 'a', 1)
        self.assertRaises(TypeError, self.calculator.log, 1, [1, 2])
        self.assertRaises(TypeError, self.calculator.log, [1, 2], [1, 2])

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(9.1), 3.0166, places=4)
        self.assertAlmostEqual(self.calculator.sqrt(10), 3.16227, places=4)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.sqrt(-math.inf), math.inf)
        self.assertAlmostEqual(self.calculator.sqrt(-1), complex(6.123233995736766e-17, 1))
        self.assertRaises(TypeError, self.calculator.sqrt, 'string')
        self.assertRaises(TypeError, self.calculator.sqrt, [1, 2])

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(self.calculator.nth_root(8.1, 3.2), 1.92265, places=4)
        self.assertAlmostEqual(self.calculator.nth_root(-8.1, 3.2), complex(1.0681703947507033, 1.5986299682925724))
        self.assertAlmostEqual(self.calculator.nth_root(math.inf, 3), math.inf)
        self.assertAlmostEqual(self.calculator.nth_root(math.inf, math.inf), 1)
        self.assertAlmostEqual(self.calculator.nth_root(-math.inf, math.inf), 1)
        self.assertAlmostEqual(self.calculator.nth_root(-math.inf, -math.inf), 1)
        self.assertRaises(TypeError, self.calculator.nth_root, 1, 'string')
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 'string')
        self.assertRaises(TypeError, self.calculator.nth_root, 'a', 1)
        self.assertRaises(TypeError, self.calculator.nth_root, 1, [1, 2])
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2], 1)
        self.assertRaises(TypeError, self.calculator.nth_root, [1, 2], [1, 2])
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 1, 0)


if __name__ == "__main__":
    unittest.main()
