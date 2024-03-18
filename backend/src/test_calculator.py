import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(1,   2),  3)
        self.assertEqual(self.calculator.addition(1.4,   1.6),  3)


        self.assertEqual(self.calculator.addition(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.addition(float('-inf'), 2), float('-inf'))
        self.assertEqual(self.calculator.addition(0, 0), 0)

        with self.assertRaises(TypeError):
            self.calculator.addition({}, 2)
        
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)
        self.assertAlmostEqual(self.calculator.subtraction(1.5, 1.6), -0.1)


        self.assertEqual(self.calculator.subtraction(float('inf'), 1), float('inf'))
        self.assertTrue(math.isnan(self.calculator.subtraction(float('-inf'), float('-inf'))) and math.isnan(float('nan')))
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

        with self.assertRaises(TypeError):
            self.calculator.subtraction({}, 2)
    
    def test_division(self):
        self.assertEqual(self.calculator.division(6, 3), 2)
        self.assertEqual(self.calculator.division(1, 0), None)
        self.assertEqual(self.calculator.division(1, -1), -1)
        self.assertEqual(self.calculator.division(-1, -1), 1)
        self.assertAlmostEqual(self.calculator.division(0.63241, 0.12312), 5.13653346328785)


        self.assertEqual(self.calculator.division(float('inf'), 2), float('inf'))
        self.assertEqual(self.calculator.division(float('-inf'), -2), float('inf'))
        self.assertEqual(self.calculator.division(float('-inf'), 2), float('-inf'))
        self.assertEqual(self.calculator.division(float('inf'), 0), None)
        self.assertEqual(self.calculator.division(0, 0), None)

        with self.assertRaises(TypeError):
            self.calculator.division({}, 2)

    def test_adsolute(self):
        self.assertEqual(self.calculator.adsolute(-100), 100)
        self.assertEqual(self.calculator.adsolute(-1), 1)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(float('inf')), float('inf'))
        self.assertEqual(self.calculator.adsolute(float('-inf')), float('inf'))

        with self.assertRaises(TypeError):
            self.calculator.adsolute({})

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(123331, 0), 1)
        self.assertEqual(self.calculator.degree(2, -2), 0.25)

        self.assertEqual(self.calculator.degree(0, 0), 1)
        self.assertEqual(self.calculator.degree(float('inf'), float('inf')), float('inf'))

        with self.assertRaises(TypeError):
            self.calculator.degree({}, 2)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

        self.assertEqual(self.calculator.ln(float('inf')), float('inf'))
        self.assertAlmostEqual(self.calculator.ln(3), 1.0986122886681098)
        self.assertAlmostEqual(self.calculator.ln(13), 2.5649493574615367)

        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(ValueError, self.calculator.ln, -8)

        with self.assertRaises(TypeError):
            self.calculator.ln({})

    def test_log(self):
        self.assertEqual(self.calculator.log(8, 2), 3)
        self.assertRaises(ValueError, self.calculator.log, 8, -2)
        self.assertAlmostEqual(self.calculator.log(8, 3), 1.892789260714372)

        with self.assertRaises(TypeError):
            self.calculator.log({})

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(9), 3)
        self.assertAlmostEqual(self.calculator.sqrt(7), 2.6457513110645907)


        with self.assertRaises(TypeError):
            self.calculator.sqrt({})

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(64, 2), 8)

        with self.assertRaises(TypeError):
            self.calculator.nth_root({})
        
        self.assertEqual(self.calculator.nth_root(0, 12342), 0)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiplication(8, 8), 64)
        self.assertEqual(self.calculator.multiplication(-8, 8), -64)
        
        self.assertEqual(self.calculator.multiplication(float('inf'), 8), float('inf'))
        self.assertEqual(self.calculator.multiplication(float('-inf'), -8), float('inf'))
        self.assertEqual(self.calculator.multiplication(float('inf'), -8), float('-inf'))
        self.assertEqual(self.calculator.multiplication(float('inf'), float('inf')), float('inf'))
        self.assertEqual(self.calculator.multiplication(0, 5), 0)
        self.assertAlmostEqual(self.calculator.multiplication(25.23, 15.12), 381.4776)

        with self.assertRaises(TypeError):
            self.calculator.multiplication({})
if __name__ == "__main__":
    unittest.main()