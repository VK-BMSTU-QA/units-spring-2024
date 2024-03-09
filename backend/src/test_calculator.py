import math
import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add1(self):
        self.assertEqual(self.calculator.addition(1, 2), 1 + 2)

    def test_add2(self):
        self.assertEqual(self.calculator.addition(2, 1), 2 + 1)

    def test_add3(self):
        self.assertEqual(self.calculator.addition(-1, 2), -1 + 2)

    def test_add4(self):
        self.assertEqual(self.calculator.addition(2, -1), 2 + -1)

    def test_add5(self):
        self.assertEqual(self.calculator.addition(2, 0), 2 + 0)

    def test_add6(self):
        self.assertAlmostEqual(self.calculator.addition(2.3, 3), 2.3 + 3)

    def test_add7(self):
        self.assertAlmostEqual(self.calculator.addition(2.3, 3.1), 2.3 + 3.1)

    def test_mul1(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 3 * 2)

    def test_mul2(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 2 * 3)

    def test_mul3(self):
        self.assertEqual(self.calculator.multiplication(10, 0), 10 * 0)

    def test_mul4(self):
        self.assertAlmostEqual(self.calculator.multiplication(10.1, 2), 10.1 * 2)

    def test_mul5(self):
        self.assertAlmostEqual(self.calculator.multiplication(10.1, 2.1), 10.1 * 2.1)

    def test_mul6(self):
        self.assertEqual(self.calculator.multiplication(-10, 2), -10 * 2)

    def test_mul7(self):
        self.assertAlmostEqual(self.calculator.multiplication(-10.2, 2), -10.2 * 2)

    def test_mul8(self):
        self.assertAlmostEqual(self.calculator.multiplication(-10.2, 2.1), -10.2 * 2.1)

    def test_mul9(self):
        self.assertAlmostEqual(self.calculator.multiplication(-10.2, -2.1), -10.2 * -2.1)

    def test_sub1(self):
        self.assertEqual(self.calculator.subtraction(3, 2), 3 - 2)

    def test_div1(self):
        self.assertAlmostEqual(self.calculator.division(3, 2), 3 / 2)

    def test_div2(self):
        self.assertAlmostEqual(self.calculator.division(3.2, 2), 3.2 / 2)
    
    def test_div3(self):
        self.assertAlmostEqual(self.calculator.division(-3, 2), -3 / 2)

    def test_div4(self):
        self.assertAlmostEqual(self.calculator.division(-3.2, 2), -3.2 / 2)

    def test_div5(self):
        self.assertAlmostEqual(self.calculator.division(-3.2, -2), -3.2 / -2)

    def test_div6(self):
        self.assertAlmostEqual(self.calculator.division(-3.2, -2.2), -3.2 / -2.2)

    def test_div7(self):
        self.assertEqual(self.calculator.division(10, 0), None)
    
    def test_abs1(self):
        self.assertEqual(self.calculator.adsolute(3), 3)

    def test_abs2(self):
        self.assertEqual(self.calculator.adsolute(-3), 3)

    def test_abs3(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_abs4(self):
        self.assertEqual(self.calculator.adsolute(3), 3)
        
    def test_deg(self):
        self.assertEqual(self.calculator.degree(3, 2), 3 ** 2)

    def test_deg1(self):
        self.assertAlmostEqual(self.calculator.degree(3, -2), 3 ** -2)

    def test_deg2(self):
        self.assertEqual(self.calculator.degree(-3, 2), (-3) ** 2)

    def test_deg3(self):
        self.assertAlmostEqual(self.calculator.degree(-3.1, -2), (-3.1) ** (-2))
        
    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(2), math.log(2))

    def test_ln1(self):
        self.assertAlmostEqual(self.calculator.ln(2.1), math.log(2.1))

    def test_log1(self):
        self.assertAlmostEqual(self.calculator.log(2, 1.1), math.log(2, 1.1))

    def test_log2(self):
        self.assertAlmostEqual(self.calculator.log(2, 2), math.log(2, 2))

    def test_log3(self):
        self.assertAlmostEqual(self.calculator.log(2, 1.5), math.log(2, 1.5))

    def test_log4(self):
        with self.assertRaises(ValueError): 
            self.calculator.log(1, -5)

    def test_log5(self):
        with self.assertRaises(ValueError): 
            self.calculator.log(-1, 5)

    def test_log6(self):
        with self.assertRaises(ValueError): 
            self.calculator.log(-1, -5)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(2), 2 ** 0.5)
    
    def test_sqrt1(self):
        self.assertAlmostEqual(self.calculator.sqrt(2.1), 2.1 ** 0.5)

    def test_sqrt2(self):
        self.assertAlmostEqual(self.calculator.sqrt(-2), (-2) ** 0.5)
    
    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(2, 1), 2 ** (1. / 1))

    def test_nth_root1(self):
        self.assertAlmostEqual(self.calculator.nth_root(-2, 1), (-2) ** (1. / 1))

    def test_nth_root2(self):
        self.assertAlmostEqual(self.calculator.nth_root(-2, -1), (-2) ** (1. / -1))

    def test_nth_root3(self):
        self.assertAlmostEqual(self.calculator.nth_root(2, 3.1), 2 ** (1. / 3.1))
    
    def test_nth_root4(self):
        self.assertAlmostEqual(self.calculator.nth_root(2.1, 3.1), 2.1 ** (1. / 3.1))

    def test_nth_root5(self):
        self.assertRaises(ValueError, self.calculator.log, 1, -5)
        


if __name__ == "__main__":
    unittest.main()
