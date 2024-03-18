import unittest
import math
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition__int(self):
        tests = [
            [[1, 2], 3, int],
            [[2, 1], 3, int],
            [[-10, 2], -8, int],
            [[2, -10], -8, int],
            [[0, -10], -10, int],
            [[-10, 0], -10, int],
            [[0, 0], 0, int],
        ]

        for test in tests:
            result = self.calculator.addition(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_addition__float(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")

        tests = [
            [[0.2, 0.1], 0.3, float],
            [[0.1, 0.2], 0.3, float],
            [[-0.1, 0.2], 0.1, float],
            [[-0.2, -0.1], -0.3, float],
            [[-0.1, 0], -0.1, float],
            [[0.0, -0.2], -0.2, float],
            [[0.0, 0.0], 0, float],
            [[positive_inf, positive_inf], positive_inf, float],
            [[negative_inf, negative_inf], negative_inf, float],
            [[positive_inf, 1], positive_inf, float],
            [[1, positive_inf], positive_inf, float],
            [[-1e100, positive_inf], positive_inf, float],
            [[positive_inf, -1e100], positive_inf, float],
            [[negative_inf, 1], negative_inf, float],
            [[1, negative_inf], negative_inf, float],
            [[1e100, negative_inf], negative_inf, float],
            [[negative_inf, 1e100], negative_inf, float],
        ]

        for test in tests:
            result = self.calculator.addition(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_addition__nan(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        
        tests = [
            [positive_inf, negative_inf],
            [negative_inf, positive_inf],
        ]

        for test in tests:
            result = self.calculator.addition(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_addition__type_error(self):
        tests = [
            [2, "2"],
            ["2", 2],
            ["2", {}],
            [{}, "2"],
            [{}, 1],
            [1, {}],
            [[], "2"],
            ["2", []],
            [[], {}],
            [{}, []],
            [[], 1],
            [1, []],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.addition, *test)


    def test_multiplication__int(self):
        tests = [
            [[2, 3], 6, int],
            [[-2, 3], -6, int],
            [[-2, -3], 6, int],
            [[0, 3], 0, int],
            [[0, -3], 0, int],
            [[0, 0], 0, int],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_multiplication__float(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")

        tests = [
            [[2.5, 3], 7.5, float],
            [[-2.5, 3], -7.5, float],
            [[-2.5, -3], 7.5, float],
            [[0.0, 3], 0.0, float],
            [[0.0, -3], 0.0, float],
            [[0.0, 0], 0.0, float],
            [[positive_inf, 0.25], positive_inf, float],
            [[0.25, positive_inf], positive_inf, float],
            [[-2, positive_inf], negative_inf, float],
            [[positive_inf, -2], negative_inf, float],
            [[negative_inf, 0.25], negative_inf, float],
            [[0.25, negative_inf], negative_inf, float],
            [[-2, negative_inf], positive_inf, float],
            [[negative_inf, -2], positive_inf, float],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_multiplication__nan(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        
        tests = [
            [positive_inf, 0],
            [negative_inf, 0],
            [0, positive_inf],
            [0, negative_inf],
        ]

        for test in tests:
            result = self.calculator.multiplication(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_multiplication__type_error(self):
        tests = [
            ["2", {}],
            [{}, "2"],
            [{}, 1],
            [1, {}],
            [[], "2"],
            ["2", []],
            [[], {}],
            [{}, []],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.multiplication, *test)


    def test_subtraction__int(self):
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

    def test_subtraction__float(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        
        tests = [
            [[0.2, 0.3], -0.1, float],
            [[0.2, -0.3], 0.5, float],
            [[-0.2, -0.3], 0.1, float],
            [[-0.2, 0.3], -0.5, float],
            [[0.0, 0.3], -0.3, float],
            [[0.3, 0.0], 0.3, float],
            [[0.0, 0.0], 0.0, float],
            [[positive_inf, negative_inf], positive_inf, float],
            [[negative_inf, positive_inf], negative_inf, float],
            [[positive_inf, 25], positive_inf, float],
            [[26, positive_inf], negative_inf, float],
            [[1e100, positive_inf], negative_inf, float],
            [[positive_inf, 1e100], positive_inf, float],
            [[negative_inf, 25], negative_inf, float],
            [[25, negative_inf], positive_inf, float],
            [[1e100, negative_inf], positive_inf, float],
            [[negative_inf, -1e100], negative_inf, float],
        ]

        for test in tests:
            result = self.calculator.subtraction(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_subtraction__nan(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")

        tests = [
            [positive_inf, positive_inf],
            [negative_inf, negative_inf],
        ]

        for test in tests:
            result = self.calculator.subtraction(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_subtraction__type_error(self):
        tests = [
            [2, "2"],
            ["2", 2],
            ["2", {}],
            [{}, "2"],
            [{}, 1],
            [1, {}],
            [[], "2"],
            ["2", []],
            [[], {}],
            [{}, []],
            [[], 1],
            [1, []],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.subtraction, *test)


    def test_division__int(self):
        tests = [
            [[6, 3], 2, float],
            [[-6, 3], -2, float],
            [[-6, -3], 2, float],
            [[0, 3], 0, float],
        ]

        for test in tests:
            result = self.calculator.division(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_division__float(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        
        tests = [
            [[1, 3], 1/3, float],
            [[0.2, 0.3], 2/3, float],
            [[-7, -2], 3.5, float],
            [[7, -2], -3.5, float],
            [[-7, 2], -3.5, float],
            [[0, 2], 0, float],
            [[0, -2], 0, float],
            [[positive_inf, 25], positive_inf, float],
            [[26, positive_inf], 0, float],
            [[negative_inf, 25], negative_inf, float],
            [[25, negative_inf], 0, float],
            [[1e100, positive_inf], 0, float],
            [[positive_inf, 1e100], positive_inf, float],
            [[1e100, negative_inf], 0, float],
            [[negative_inf, -1e100], positive_inf, float],
        ]

        for test in tests:
            result = self.calculator.division(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_division__nan(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        tests = [
            [positive_inf, positive_inf],
            [negative_inf, negative_inf],
            [negative_inf, positive_inf],
            [positive_inf, negative_inf],
        ]

        for test in tests:
            result = self.calculator.division(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_division__zero(self):
        self.assertIsNone(self.calculator.division(3.0, 0))

    def test_division__type_error(self):
        tests = [
            [2, "2"],
            ["2", 2],
            ["2", {}],
            [{}, "2"],
            [{}, 1],
            [1, {}],
            [[], "2"],
            ["2", []],
            [[], {}],
            [{}, []],
            [[], 1],
            [1, []],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.division, *test)


    def test_absolute__int(self):
        tests = [
            [[-3], 3, int],
            [[-1], 1, int],
            [[0], 0, int],
        ]

        for test in tests:
            result = self.calculator.absolute(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_absolute__float(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        
        tests = [
            [[-3.2], 3.2, float],
            [[3.2], 3.2, float],
            [[0.0], 0.0, float],
            [[positive_inf], positive_inf, float],
            [[negative_inf], positive_inf, float],
        ]

        for test in tests:
            result = self.calculator.absolute(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_absolute__nan(self):
        nan = float("nan")

        tests = [
            [nan],
        ]

        for test in tests:
            result = self.calculator.absolute(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_absolute__type_error(self):
        tests = [
            ["2"],
            [[]],
            [{}],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.absolute, *test)


    def test_degree__int(self):
        tests = [
            [[2, 3], 8, int],
            [[-2, 3], -8, int],
            [[2, 0], 1, int],
            [[0, 3], 0, int],
            [[0, 0], 1, int],
        ]

        for test in tests:
            result = self.calculator.degree(*test[0])
            self.assertEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_degree__float(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        nan = float("nan")

        tests = [
            [[2.5, 2], 6.25, float],
            [[-2.5, 2], 6.25, float],
            [[2.5, 0.5], 1.5811388300841898, float],
            [[0.5, 2], 0.25, float],
            [[positive_inf, 2], positive_inf, float],
            [[2, positive_inf], positive_inf, float],
            [[positive_inf, -2], 0, float],
            [[-2, positive_inf], positive_inf, float],
            [[negative_inf, 2], positive_inf, float],
            [[2, negative_inf], 0, float],
            [[negative_inf, -2], 0, float],
            [[-2, negative_inf], 0, float],
            [[negative_inf, positive_inf], positive_inf, float],
            [[positive_inf, positive_inf], positive_inf, float],
            [[positive_inf, negative_inf], 0, float],
            [[negative_inf, negative_inf], 0, float],
            [[positive_inf, 0], 1, float],
            [[negative_inf, 0], 1, float],
            [[0, positive_inf], 0, float],
            [[0, negative_inf], positive_inf, float],
            [[nan, 0], 1, float],
        ]

        for test in tests:
            result = self.calculator.degree(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_degree__zero(self):
        tests = [
            [0, 0, 1],
            [0, 5, 0],
            [5, 0, 1],
        ]

        for test in tests:
            result = self.calculator.degree(test[0], test[1])
            self.assertEqual(result, test[2])

    def test_degree__nan(self):
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

    def test_degree__type_error(self):
        tests = [
            [2, "2"],
            ["2", 2],
            ["2", {}],
            [{}, "2"],
            [{}, 1],
            [1, {}],
            [[], "2"],
            ["2", []],
            [[], {}],
            [{}, []],
            [[], 1],
            [1, []],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.degree, *test)


    def test_ln__positive(self):
        tests = [
            [1, 0.0],
            [2.718281828459045, 1.0],
            [7.38905609893065, 2.0],
            [20.085536923187668, 3.0],
        ]

        for test in tests:
            result = self.calculator.ln(test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, float)

    def test_ln__nan(self):
        nan = float("nan")

        tests = [
            [nan],
        ]

        for test in tests:
            result = self.calculator.ln(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_ln__wrong_values(self):
        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(ValueError, self.calculator.ln, -4)
        self.assertRaises(ValueError, self.calculator.ln, float("-inf"))

    def test_ln__type_error(self):
        tests = [
            ["2"],
            [[]],
            [{}],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.ln, *test)


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

    def test_log__nan(self):
            positive_inf = float("inf")
            nan = float("nan")

            tests = [
                [positive_inf, positive_inf],
                [2, nan],
                [nan, 2],
            ]

            for test in tests:
                result = self.calculator.log(*test)
                self.assertTrue(math.isnan(result))
                self.assertIsInstance(result, float)

    def test_log__type_error(self):
        tests = [
            [2, "2"],
            ["2", 2],
            ["2", {}],
            [{}, "2"],
            [{}, 1],
            [1, {}],
            [[], "2"],
            ["2", []],
            [[], {}],
            [{}, []],
            [[], 1],
            [1, []],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.log, *test)

    def test_log__wrong_values(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")

        tests = [
            [3, -1],
            [0, 2],
            [negative_inf, negative_inf],
            [negative_inf, positive_inf],
            [positive_inf, negative_inf],
        ]

        for test in tests:
            self.assertRaises(ValueError, self.calculator.log, *test)


    def test_sqrt(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")

        tests = [
            [[25], 5.0, float],
            [[1], 1.0, float],
            [[0.64], 0.8, float],
            [[4.84], 2.2, float],
            [[0], 0.0, float],
            [[positive_inf], positive_inf, float],
            [[negative_inf], positive_inf, float],
        ]

        for test in tests:
            result = self.calculator.sqrt(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_sqrt__nan(self):
        nan = float("nan")

        tests = [
            [nan],
        ]

        for test in tests:
            result = self.calculator.sqrt(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_sqrt__type_error(self):
        tests = [
            ["2"],
            [[]],
            [{}],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.sqrt, *test)


    def test_nth_root(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        nan = float("nan")

        tests = [
            [[32, 22], 32 ** (1.0 / 22), float],
            [[14.21, 53.22], 14.21 ** (1.0 / 53.22), float],
            [[16, 4], 2, float],
            [[1.331, 3], 1.1, float],
            [[0, 2], 0, float],
            [[positive_inf, 10], positive_inf, float],
            [[negative_inf, 10], positive_inf, float],
            [[positive_inf, -10], 0, float],
            [[negative_inf, -10], 0, float],
            [[10, positive_inf], 1, float],
            [[-10, positive_inf], 1, float],
            [[10, negative_inf], 1, float],
            [[-10, negative_inf], 1, float],
            [[positive_inf, positive_inf], 1, float],
            [[positive_inf, negative_inf], 1, float],
            [[negative_inf, positive_inf], 1, float],
            [[positive_inf, negative_inf], 1, float],
            [[nan, negative_inf], 1, float],
            [[nan, positive_inf], 1, float],
        ]

        for test in tests:
            result = self.calculator.nth_root(*test[0])
            self.assertAlmostEqual(result, test[1])
            self.assertIsInstance(result, test[2])

    def test_nth_root__nan(self):
        positive_inf = float("inf")
        negative_inf = float("-inf")
        nan = float("nan")

        tests = [
            [2, nan],
            [positive_inf, nan],
            [negative_inf, nan],
        ]

        for test in tests:
            result = self.calculator.nth_root(*test)
            self.assertTrue(math.isnan(result))
            self.assertIsInstance(result, float)

    def test_nth_root__wrong_values(self):
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 32, 0.0)

    def test_nth_root__type_error(self):
        tests = [
            [2, "2"],
            ["2", 2],
            ["2", {}],
            [{}, "2"],
            [{}, 1],
            [1, {}],
            [[], "2"],
            ["2", []],
            [[], {}],
            [{}, []],
            [[], 1],
            [1, []],
        ]

        for test in tests:
            self.assertRaises(TypeError, self.calculator.nth_root, *test)

if __name__ == "__main__":
    unittest.main()
