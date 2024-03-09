import unittest
import math
from src.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_int(self):
        tests = [
            [[1, 2], 3, int],
            [[2, 1], 3, int],
            [[-6, 17], 11, int],
            [[-3, -4], -7, int],
        ]

        for test in tests:
            result = self.calculator.addition(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_add_float(self):
        tests = [
            [[0.2, 0.3], 0.5, float],
            [[0.3, 0.2], 0.5, float],
            [[-0.3, 0.2], -0.1, float],
            [[-0.3, -0.3], -0.6, float],
        ]

        for test in tests:
            result = self.calculator.addition(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_add_types(self):
        self.assertRaises(TypeError, self.calculator.addition, 1, "123")


    def test_mul_int(self):
        tests = [
            [[2, 7], 14, int],
            [[7, 2], 14, int],
            [[-5, 3], -15, int],
            [[-5, -3], 15, int],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_mul_float(self):
        tests = [
            [[1/3, 3], 1, float],
            [[3.2, -2], -6.4, float],
            [[-3.2, -2], 6.4, float],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_mul_types(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 3.0, "ab")


    def test_sub_int(self):
        tests = [
            [[2, 7], -5, int],
            [[7, 2], 5, int],
            [[-5, 3], -8, int],
            [[-5, -3], -2, int],
        ]

        for test in tests:
            result = self.calculator.subtraction(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_sub_float(self):
        tests = [
            [[0.2, 0.3], -0.1, float],
            [[0.2, -0.3], 0.5, float],
            [[-0.2, -0.3], 0.1, float],
            [[-0.2, 0.3], -0.5, float],
        ]

        for test in tests:
            result = self.calculator.subtraction(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_sub_types(self):
        self.assertRaises(TypeError, self.calculator.subtraction, 3.0, "ab")


    def test_div(self):
        tests = [
            [[1, 3], 1/3, float],
            [[0.2, 0.3], 2/3, float],
            [[-7, -2], 3.5, float],
            [[7, -2], -3.5, float],
            [[-7, 2], -3.5, float],
        ]

        for test in tests:
            result = self.calculator.division(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_div_types(self):
        self.assertRaises(TypeError, self.calculator.division, 3.0, "ab")

    def test_div_zero(self):
        self.assertIsNone(self.calculator.division(3.0, 0))
    

    def test_abs_int(self):
        tests = [
            [[4], 4, int],
            [[-4], 4, int],
        ]

        for test in tests:
            result = self.calculator.adsolute(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_abs_float(self):
        tests = [
            [[-3.2], 3.2, float],
            [[3.2], 3.2, float],
        ]

        for test in tests:
            result = self.calculator.adsolute(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    
    def test_deg_int(self):
        tests = [
            [[1, 219465322], 1, int],
            [[2, 8], 256, int],
        ]

        for test in tests:
            result = self.calculator.degree(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_deg_float(self):
        tests = [
            [[3, -1], 1/3, float],
            [[0.1, 2], 0.01, float],
        ]

        for test in tests:
            result = self.calculator.degree(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])


    def test_ln_1(self):
        self.assertAlmostEqual(self.calculator.ln(3), math.log(3))

    def test_ln_2(self):
        self.assertRaises(ValueError, self.calculator.ln, -4)


    def test_log(self):
        tests = [
            [[3, 5], math.log(3, 5), float],
            [[1, 25], 0.0, float],
        ]

        for test in tests:
            result = self.calculator.log(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_log_wrong_values(self):
        self.assertRaises(ValueError, self.calculator.log, 3, -1)


    def test_sqrt(self):
        tests = [
            [[25], 5.0, float],
            [[1], 1.0, float],
            [[0], 0.0, float],
        ]

        for test in tests:
            result = self.calculator.sqrt(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])


    def test_nth_root_1(self):
        self.assertAlmostEqual(self.calculator.nth_root(32, 22), 32 ** (1. / 22))
    def test_nth_root_2(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 32, 0.0)




if __name__ == "__main__":
    unittest.main()
