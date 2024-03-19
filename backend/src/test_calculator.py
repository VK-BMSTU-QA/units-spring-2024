import unittest
import math
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition('a', 'b'), 'ab')
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.1), 3.2, places=3)
        self.assertRaises(TypeError, self.calculator.addition, {1}, {1})
        self.assertRaises(TypeError, self.calculator.addition, {1}, 1)
        self.assertRaises(TypeError, self.calculator.addition("a", 3))
        self.assertRaises(TypeError, self.calculator.addition, None, 1)
        self.assertRaises(TypeError, self.calculator.addition, None, None)
            

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3,1), 2)
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertRaises(TypeError, self.calculator.subtraction, None, 3)
        self.assertRaises(TypeError, self.calculator.subtraction, None, None)
        self.assertRaises(TypeError, self.calculator.subtraction, "3", 3)
        self.assertRaises(TypeError, self.calculator.subtraction, "3", "3")
        self.assertRaises(TypeError, self.calculator.subtraction, [3], 3)
        self.assertRaises(TypeError, self.calculator.subtraction, [3], [3])
        self.assertEqual(self.calculator.subtraction((3), 3), 0)
        self.assertEqual(self.calculator.subtraction((3), (3)), 0)
        self.assertEqual(self.calculator.subtraction({3}, {3}), set())
        self.assertRaises(TypeError, self.calculator.subtraction, {3}, 3)

    def test_mltpl(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertRaises(TypeError, self.calculator.multiplication, None, 3)
        self.assertRaises(TypeError, self.calculator.multiplication, None, None)
        self.assertEqual(self.calculator.multiplication("3", 3), "333")
        self.assertRaises(TypeError, self.calculator.multiplication, "3", "3")
        self.assertEqual(self.calculator.multiplication([3], 3), [3, 3, 3])
        self.assertRaises(TypeError, self.calculator.multiplication, [3], [3])
        self.assertEqual(self.calculator.multiplication((3), 3), 9)
        self.assertEqual(self.calculator.multiplication((3), (3)), 9)
        self.assertRaises(TypeError, self.calculator.multiplication, {3}, {3})
        self.assertRaises(TypeError, self.calculator.multiplication, {3}, 3)

    def test_div(self):
        self.assertEqual(self.calculator.division(4, 2), 2)
        self.assertAlmostEqual(self.calculator.division(4, 3), 1.33333, places=5)
        self.assertIsNone(self.calculator.division(4, 0))
        self.assertEqual(self.calculator.division(0, 2), 0)
        self.assertAlmostEqual(self.calculator.division(1, 3), 0.33333, places=5)
        self.assertRaises(TypeError, self.calculator.division, None, 3)
        self.assertRaises(TypeError, self.calculator.division, None, None)
        self.assertRaises(TypeError, self.calculator.division, "3", 3)
        self.assertRaises(TypeError, self.calculator.division, "3", "3")
        self.assertRaises(TypeError, self.calculator.division, [3], 3)
        self.assertRaises(TypeError, self.calculator.division, [3], [3])
        self.assertEqual(self.calculator.division((3), 3), 1)
        self.assertEqual(self.calculator.division((3), (3)), 1)
        self.assertRaises(TypeError, self.calculator.division, {3}, {3})
        self.assertRaises(TypeError, self.calculator.division, {3}, 3)
    
    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(4), 4)
        self.assertEqual(self.calculator.adsolute(-4), 4)
        self.assertRaises(TypeError, self.calculator.adsolute, None, 3)
        self.assertRaises(TypeError, self.calculator.adsolute, None, None)
        self.assertRaises(TypeError, self.calculator.adsolute, "3", 3)
        self.assertRaises(TypeError, self.calculator.adsolute, "3", "3")
        self.assertRaises(TypeError, self.calculator.adsolute, [3], 3)
        self.assertRaises(TypeError, self.calculator.adsolute, [3], [3])
        self.assertRaises(TypeError, self.calculator.adsolute, (3), 3)
        self.assertRaises(TypeError, self.calculator.adsolute, (3), (3))
        self.assertRaises(TypeError, self.calculator.adsolute, {3}, {3})
        self.assertRaises(TypeError, self.calculator.adsolute, {3}, 3)
        
    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 1), 2)
        self.assertEqual(self.calculator.degree(2, 2), 4)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(4, 0.5), 2)
        self.assertEqual(self.calculator.degree(2, -1), 0.5)
        self.assertRaises(TypeError, self.calculator.degree, None, 3)
        self.assertRaises(TypeError, self.calculator.degree, None, None)
        self.assertRaises(TypeError, self.calculator.degree, "3", 3)
        self.assertRaises(TypeError, self.calculator.degree, "3", "3")
        self.assertRaises(TypeError, self.calculator.degree, [3], 3)
        self.assertRaises(TypeError, self.calculator.degree, [3], [3])
        self.assertEqual(self.calculator.degree((3), 3), 27)
        self.assertEqual(self.calculator.degree((3), (3)), 27)
        self.assertRaises(TypeError, self.calculator.degree, {3}, {3})
        self.assertRaises(TypeError, self.calculator.degree, {3}, 3)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.exp(2)), 2)
        self.assertEqual(self.calculator.ln(math.exp(0)), 0)
        self.assertEqual(self.calculator.ln(math.exp(-1)), -1)
        self.assertRaises(ValueError, self.calculator.ln, -1)
        self.assertRaises(TypeError, self.calculator.ln, None)
        self.assertRaises(TypeError, self.calculator.ln, "3")
        self.assertRaises(TypeError, self.calculator.ln, [3])
        self.assertRaises(TypeError, self.calculator.ln, {3})

    def test_log(self):
        self.assertEqual(self.calculator.log(2**1, 2), 1)
        self.assertEqual(self.calculator.log(2**5, 2), 5)
        self.assertEqual(self.calculator.log(2**0, 2), 0)
        self.assertEqual(self.calculator.log(2**-1, 2), -1)
        self.assertAlmostEqual(self.calculator.log(2**0.2, 2), 0.2, places=2)
        self.assertRaises(TypeError, self.calculator.log, None, 3)
        self.assertRaises(TypeError, self.calculator.log, None, None)
        self.assertRaises(TypeError, self.calculator.log, "3", 3)
        self.assertRaises(TypeError, self.calculator.log, "3", "3")
        self.assertRaises(TypeError, self.calculator.log, [3], 3)
        self.assertRaises(TypeError, self.calculator.log, [3], [3])
        self.assertRaises(TypeError, self.calculator.log, {3}, {3})
        self.assertRaises(TypeError, self.calculator.log, {3}, 3)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertAlmostEqual(self.calculator.sqrt(3), 1.73205, places=5)
        self.assertAlmostEqual(self.calculator.sqrt(0.5), 0.7071067, places=5)
        self.assertAlmostEqual(self.calculator.sqrt(1.148),  1.071447, places=2)
        self.assertRaises(TypeError, self.calculator.sqrt, None)
        self.assertRaises(TypeError, self.calculator.sqrt, "3")
        self.assertRaises(TypeError, self.calculator.sqrt, [3])
        self.assertRaises(TypeError, self.calculator.sqrt, {3})

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(1, 0)


if __name__ == "__main__":
    unittest.main()
