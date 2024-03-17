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
            [[0, -9], -9, int],
            [[-9, 0], -9, int],
            [[0, 0], 0, int],
        ]

        for test in tests:
            result = self.calculator.addition(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_add_float(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        nan = float("nan")
        tests = [
            [[0.2, 0.3], 0.5, float],
            [[0.3, 0.2], 0.5, float],
            [[-0.3, 0.2], -0.1, float],
            [[-0.3, -0.3], -0.6, float],
            [[-0.3, 0], -0.3, float],
            [[0.0, -0.3], -0.3, float],
            [[0.0, 0.0], 0, float],
            [[pos_inf, pos_inf], pos_inf, float],
            [[neg_inf, neg_inf], neg_inf, float],
            [[pos_inf, 25], pos_inf, float],
            [[26, pos_inf], pos_inf, float],
            [[-1e100, pos_inf], pos_inf, float],
            [[pos_inf, -1e100], pos_inf, float],
            [[neg_inf, 25], neg_inf, float],
            [[26, neg_inf], neg_inf, float],
            [[1e100, neg_inf], neg_inf, float],
            [[neg_inf, 1e100], neg_inf, float],
        ]

        for test in tests:
            result = self.calculator.addition(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_add_nan(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [pos_inf, neg_inf],
            [neg_inf, pos_inf],
        ]

        for test in tests:
            result = self.calculator.addition(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_add_types(self):
        tests = [
            [[3, "3"], TypeError],
            [["3", 3], TypeError],
            [["3", {}], TypeError],
            [[{}, "3"], TypeError],
            [[{}, 2], TypeError],
            [[2, {}], TypeError],
            [[[], "3"], TypeError],
            [["3", []], TypeError],
            [[[], {}], TypeError],
            [[{}, []], TypeError],
            [[[], 2], TypeError],
            [[2, []], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.addition, *test[0])


    def test_mul_int(self):
        tests = [
            [[2, 7], 14, int],
            [[7, 2], 14, int],
            [[-5, 3], -15, int],
            [[-5, -3], 15, int],
            [[5, 0], 0, int],
            [[0, 5], 0, int],
            [[-5, 0], 0, int],
            [[0, -5], 0, int],
            [[0, 0], 0, int],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_mul_float(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [[1/3, 3], 1, float],
            [[3.2, -2], -6.4, float],
            [[-3.2, -2], 6.4, float],
            [[-3.2, 0.0], 0.0, float],
            [[0.0, -3.2], 0.0, float],
            [[0.0, 0.0], 0.0, float],
            [[pos_inf, 0.25], pos_inf, float],
            [[0.25, pos_inf], pos_inf, float],
            [[-2, pos_inf], neg_inf, float],
            [[pos_inf, -2], neg_inf, float],
            [[neg_inf, 0.25], neg_inf, float],
            [[0.25, neg_inf], neg_inf, float],
            [[-2, neg_inf], pos_inf, float],
            [[neg_inf, -2], pos_inf, float],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_mul_nan(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [pos_inf, 0],
            [neg_inf, 0],
            [0, pos_inf],
            [0, neg_inf],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_mul_types(self):
        tests = [
            [["3", {}], TypeError],
            [[{}, "3"], TypeError],
            [[{}, 2], TypeError],
            [[2, {}], TypeError],
            [[[], "3"], TypeError],
            [["3", []], TypeError],
            [[[], {}], TypeError],
            [[{}, []], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.multiplication, *test[0])


    def test_sub_int(self):
        tests = [
            [[2, 7], -5, int],
            [[7, 2], 5, int],
            [[-5, 3], -8, int],
            [[-5, -3], -2, int],
            [[0, -3], 3, int],
            [[-3, 0], -3, int],
            [[0, 0], 0, int],
        ]

        for test in tests:
            result = self.calculator.subtraction(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_sub_float(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        nan = float("nan")
        tests = [
            [[0.2, 0.3], -0.1, float],
            [[0.2, -0.3], 0.5, float],
            [[-0.2, -0.3], 0.1, float],
            [[-0.2, 0.3], -0.5, float],
            [[0.0, 0.3], -0.3, float],
            [[0.3, 0.0], 0.3, float],
            [[0.0, 0.0], 0.0, float],
            [[pos_inf, neg_inf], pos_inf, float],
            [[neg_inf, pos_inf], neg_inf, float],
            [[pos_inf, 25], pos_inf, float],
            [[26, pos_inf], neg_inf, float],
            [[1e100, pos_inf], neg_inf, float],
            [[pos_inf, 1e100], pos_inf, float],
            [[neg_inf, 25], neg_inf, float],
            [[25, neg_inf], pos_inf, float],
            [[1e100, neg_inf], pos_inf, float],
            [[neg_inf, -1e100], neg_inf, float],
        ]

        for test in tests:
            result = self.calculator.subtraction(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])
    
    def test_sub_nan(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [pos_inf, pos_inf],
            [neg_inf, neg_inf],
        ]

        for test in tests:
            result = self.calculator.subtraction(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_sub_types(self):
        tests = [
            [[3, "3"], TypeError],
            [["3", 3], TypeError],
            [["3", {}], TypeError],
            [[{}, "3"], TypeError],
            [[{}, 2], TypeError],
            [[2, {}], TypeError],
            [[[], "3"], TypeError],
            [["3", []], TypeError],
            [[[], {}], TypeError],
            [[{}, []], TypeError],
            [[[], 2], TypeError],
            [[2, []], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.subtraction, *test[0])


    def test_div(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [[1, 3], 1/3, float],
            [[0.2, 0.3], 2/3, float],
            [[-7, -2], 3.5, float],
            [[7, -2], -3.5, float],
            [[-7, 2], -3.5, float],
            [[0, 2], 0, float],
            [[0, -2], 0, float],
            [[pos_inf, 25], pos_inf, float],
            [[26, pos_inf], 0, float],
            [[neg_inf, 25], neg_inf, float],
            [[25, neg_inf], 0, float],
            [[1e100, pos_inf], 0, float],
            [[pos_inf, 1e100], pos_inf, float],
            [[1e100, neg_inf], 0, float],
            [[neg_inf, -1e100], pos_inf, float],
        ]

        for test in tests:
            result = self.calculator.division(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_div_nan(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [pos_inf, pos_inf],
            [neg_inf, neg_inf],
            [neg_inf, pos_inf],
            [pos_inf, neg_inf],
        ]

        for test in tests:
            result = self.calculator.division(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_div_zero(self):
        self.assertIsNone(self.calculator.division(3.0, 0))
    
    def test_div_types(self):
        tests = [
            [[3, "3"], TypeError],
            [["3", 3], TypeError],
            [["3", {}], TypeError],
            [[{}, "3"], TypeError],
            [[{}, 2], TypeError],
            [[2, {}], TypeError],
            [[[], "3"], TypeError],
            [["3", []], TypeError],
            [[[], {}], TypeError],
            [[{}, []], TypeError],
            [[[], 2], TypeError],
            [[2, []], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.division, *test[0])


    def test_abs_int(self):
        tests = [
            [[4], 4, int],
            [[-4], 4, int],
            [[0], 0, int],
        ]

        for test in tests:
            result = self.calculator.adsolute(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_abs_float(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [[-3.2], 3.2, float],
            [[3.2], 3.2, float],
            [[0.0], 0.0, float],
            [[pos_inf], pos_inf, float],
            [[neg_inf], pos_inf, float],
        ]

        for test in tests:
            result = self.calculator.adsolute(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_abs_nan(self):
        nan = float("nan")
        tests = [
            [nan],
        ]

        for test in tests:
            result = self.calculator.adsolute(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_abs_types(self):
        tests = [
            [["3"], TypeError],
            [[{}], TypeError],
            [[[]], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.adsolute, *test[0])

    
    def test_deg_int(self):
        tests = [
            [[1, 219465322], 1, int],
            [[0, 219465322], 0, int],
            [[219465322, 0], 1, int],
            [[2, 8], 256, int],
        ]

        for test in tests:
            result = self.calculator.degree(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_deg_float(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        nan = float("nan")
        tests = [
            [[3, -1], 1/3, float],
            [[0.1, 2], 0.01, float],
            [[1, -219465322], 1, float],
            [[pos_inf, 2], pos_inf, float],
            [[2, pos_inf], pos_inf, float],
            [[pos_inf, -2], 0, float],
            [[-2, pos_inf], pos_inf, float],
            [[neg_inf, 2], pos_inf, float],
            [[2, neg_inf], 0, float],
            [[neg_inf, -2], 0, float],
            [[-2, neg_inf], 0, float],
            [[neg_inf, pos_inf], pos_inf, float],
            [[pos_inf, pos_inf], pos_inf, float],
            [[pos_inf, neg_inf], 0, float],
            [[neg_inf, neg_inf], 0, float],
            [[pos_inf, 0], 1, float],
            [[neg_inf, 0], 1, float],
            [[0, pos_inf], 0, float],
            [[0, neg_inf], pos_inf, float],
            [[nan, 0], 1, float],
        ]

        for test in tests:
            result = self.calculator.degree(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])
    
    def test_deg_nan(self): 
        nan = float("nan")
        tests = [
            [nan, nan],
            [2, nan],
            [nan, 2],
            [0, nan],
        ]

        for test in tests:
            result = self.calculator.degree(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_deg_types(self):
        tests = [
            [[3, "3"], TypeError],
            [["3", 3], TypeError],
            [["3", {}], TypeError],
            [[{}, "3"], TypeError],
            [[{}, 2], TypeError],
            [[2, {}], TypeError],
            [[[], "3"], TypeError],
            [["3", []], TypeError],
            [[[], {}], TypeError],
            [[{}, []], TypeError],
            [[[], 2], TypeError],
            [[2, []], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.degree, *test[0])


    def test_ln(self):
        pos_inf = float("inf")
        tests = [
            [[3], math.log(3), float],
            [[0.5], math.log(0.5), float],
            [[1], 0, float],
            [[pos_inf], pos_inf, float],
        ]

        for test in tests:
            result = self.calculator.ln(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])
    
    def test_ln_nan(self): 
        nan = float("nan")
        tests = [
            [nan],
        ]

        for test in tests:
            result = self.calculator.ln(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_ln_wrong_values(self):
        self.assertRaises(ValueError, self.calculator.ln, -4)
        self.assertRaises(ValueError, self.calculator.ln, float("-inf"))

    def test_ln_types(self):
        tests = [
            [["3"], TypeError],
            [[{}], TypeError],
            [[[]], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.ln, *test[0])


    def test_log(self):
        tests = [
            [[3, 5], math.log(3, 5), float],
            [[0.5, 10], math.log(0.5, 10), float],
            [[1, 25], 0.0, float],
        ]

        for test in tests:
            result = self.calculator.log(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_log_nan(self): 
        pos_inf = float("inf")
        nan = float("nan")
        tests = [
            [pos_inf, pos_inf],
            [2, nan],
            [nan, 2],
        ]

        for test in tests:
            result = self.calculator.log(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_log_types(self):
        tests = [
            [[3, "3"], TypeError],
            [["3", 3], TypeError],
            [["3", {}], TypeError],
            [[{}, "3"], TypeError],
            [[{}, 2], TypeError],
            [[2, {}], TypeError],
            [[[], "3"], TypeError],
            [["3", []], TypeError],
            [[[], {}], TypeError],
            [[{}, []], TypeError],
            [[[], 2], TypeError],
            [[2, []], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.log, *test[0])

    def test_log_wrong_values(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [[3, -1], ValueError],
            [[0, 2], ValueError],
            [[neg_inf, neg_inf], ValueError],
            [[neg_inf, pos_inf], ValueError],
            [[pos_inf, neg_inf], ValueError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.log, *test[0])


    def test_sqrt(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        tests = [
            [[25], 5.0, float],
            [[1], 1.0, float],
            [[0.64], 0.8, float],
            [[4.84], 2.2, float],
            [[0], 0.0, float],
            [[pos_inf], pos_inf, float],
            [[neg_inf], pos_inf, float],
        ]

        for test in tests:
            result = self.calculator.sqrt(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])
    
    def test_sqrt_nan(self): 
        nan = float("nan")
        tests = [
            [nan],
        ]

        for test in tests:
            result = self.calculator.sqrt(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_sqrt_types(self):
        tests = [
            [["3"], TypeError],
            [[{}], TypeError],
            [[[]], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.sqrt, *test[0])


    def test_nth_root(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        nan = float("nan")
        tests = [
            [[32, 22], 32 ** (1.0 / 22), float],
            [[14.21, 53.22], 14.21 ** (1.0 / 53.22), float],
            [[16, 4], 2, float],
            [[1.331, 3], 1.1, float],
            [[0, 2], 0, float],
            [[pos_inf, 10], pos_inf, float],
            [[neg_inf, 10], pos_inf, float],
            [[pos_inf, -10], 0, float],
            [[neg_inf, -10], 0, float],
            [[10, pos_inf], 1, float],
            [[-10, pos_inf], 1, float],
            [[10, neg_inf], 1, float],
            [[-10, neg_inf], 1, float],
            [[pos_inf, pos_inf], 1, float],
            [[pos_inf, neg_inf], 1, float],
            [[neg_inf, pos_inf], 1, float],
            [[pos_inf, neg_inf], 1, float],
            [[nan, neg_inf], 1, float],
            [[nan, pos_inf], 1, float],
        ]

        for test in tests:
            result = self.calculator.nth_root(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])
    
    def test_nth_root_nan(self):
        pos_inf = float("inf")
        neg_inf = float("-inf")
        nan = float("nan")
        tests = [
            [2, nan],
            [pos_inf, nan],
            [neg_inf, nan],
        ]

        for test in tests:
            result = self.calculator.nth_root(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_nth_root_wrong_values(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 32, 0.0)
    
    def test_nth_types(self):
        tests = [
            [[3, "3"], TypeError],
            [["3", 3], TypeError],
            [["3", {}], TypeError],
            [[{}, "3"], TypeError],
            [[{}, 2], TypeError],
            [[2, {}], TypeError],
            [[[], "3"], TypeError],
            [["3", []], TypeError],
            [[[], {}], TypeError],
            [[{}, []], TypeError],
            [[[], 2], TypeError],
            [[2, []], TypeError],
        ]

        for test in tests:
            self.assertRaises(test[1], self.calculator.nth_root, *test[0])



if __name__ == "__main__":
    unittest.main()
