import math
import unittest
from . import calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator.Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(3, -3), 0)
        self.assertEqual(self.calculator.addition(-1, -2), -3)
        self.assertEqual(self.calculator.addition(3, 2.5), 5.5)
        self.assertEqual(self.calculator.addition(math.inf, -2), math.inf)

        with self.assertRaises(TypeError):
            self.calculator.addition("string", -2)

        with self.assertRaises(TypeError):
            self.calculator.addition(None, -2)

        with self.assertRaises(TypeError):
            self.calculator.addition([1, "99", 878], -2)


    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(3, 1), 2)
        self.assertEqual(self.calculator.subtraction(3, -3), 6)
        self.assertEqual(self.calculator.subtraction(-3, 3), -6)
        self.assertEqual(self.calculator.subtraction(math.inf, 3), math.inf)
        self.assertEqual(self.calculator.subtraction(-3.2, 1.5), -4.7)

        with self.assertRaises(TypeError):
            self.calculator.subtraction("string", -2)

        with self.assertRaises(TypeError):
            self.calculator.subtraction(None, -2)

        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, "99", 878], -2)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 4), 12)
        self.assertEqual(self.calculator.multiplication(-3, 4), -12)
        self.assertEqual(self.calculator.multiplication(-3, -4), 12)
        self.assertEqual(self.calculator.multiplication(3, 0), 0)
        self.assertEqual(self.calculator.multiplication(3, 2.5), 7.5)
        self.assertEqual(self.calculator.multiplication(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.multiplication("str", 2), "strstr")
        self.assertEqual(self.calculator.multiplication([1, 2], 2), [1, 2, 1, 2])

        with self.assertRaises(TypeError):
            self.calculator.multiplication(None, -2)

        with self.assertRaises(TypeError):
            self.calculator.multiplication("string", "string")

        with self.assertRaises(TypeError):
            self.calculator.multiplication([1, "99", 878], [1, "99", 878])


    def test_division(self):
        self.assertEqual(self.calculator.division(10, 5), 2)
        self.assertEqual(self.calculator.division(5, 2), 2.5)
        self.assertEqual(self.calculator.division(10, 0), None)
        self.assertEqual(self.calculator.division(math.inf, 100000000000), math.inf)
        self.assertAlmostEqual(self.calculator.division(10, 1.5),  6.66666, places=3)

        with self.assertRaises(TypeError):
            self.calculator.division("string", -2)

        with self.assertRaises(TypeError):
            self.calculator.division(None, -2)

        with self.assertRaises(TypeError):
            self.calculator.division([1, "99", 878], -2)

    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(-10), 10)
        self.assertEqual(self.calculator.adsolute(-2.5), 2.5)
        self.assertEqual(self.calculator.adsolute(10), 10)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

        with self.assertRaises(TypeError):
            self.calculator.adsolute("string")

        with self.assertRaises(TypeError):
            self.calculator.adsolute([1, "99", 878])

        with self.assertRaises(TypeError):
            self.calculator.adsolute(None)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 2), 4)
        self.assertEqual(self.calculator.degree(2.5, 2), 6.25)
        self.assertEqual(self.calculator.degree(4, 0.5), 2)
        self.assertEqual(self.calculator.degree(10, -2), 0.01)
        self.assertEqual(self.calculator.degree(10, 1), 10)

        with self.assertRaises(TypeError):
            self.calculator.degree("string", 2)

        with self.assertRaises(TypeError):
            self.calculator.degree([1, "99", 878], 2)

        with self.assertRaises(TypeError):
            self.calculator.degree(None, 2)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(math.e), 1)
        self.assertEqual(self.calculator.ln(math.e ** 10), 10)
        self.assertEqual(self.calculator.ln(math.e ** -10), -10)
        self.assertEqual(self.calculator.ln(1), 0)

        with self.assertRaises(ValueError):
            self.calculator.ln(0)

        with self.assertRaises(TypeError):
            self.calculator.ln("string")

        with self.assertRaises(TypeError):
            self.calculator.ln([1, "99", 878])

        with self.assertRaises(TypeError):
            self.calculator.ln(None)

    def test_log(self):
        self.assertEqual(self.calculator.log(math.e, math.e), 1)
        self.assertEqual(self.calculator.log(2, 4), 0.5)
        self.assertEqual(self.calculator.log(4, 2), 2)
        self.assertEqual(self.calculator.log(10, 10), 1)

        with self.assertRaises(TypeError):
            self.calculator.log("string", 2)

        with self.assertRaises(TypeError):
            self.calculator.log([1, "99", 878], 2)

        with self.assertRaises(TypeError):
            self.calculator.log(None, 2)

        with self.assertRaises(ValueError):
            self.calculator.log(10, 0)

        with self.assertRaises(ValueError):
            self.calculator.log(0, 2)

        with self.assertRaises(ValueError):
            self.calculator.log(-10, 2)



    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertEqual(self.calculator.sqrt(1), 1)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(-10), (-10) ** 0.5)
        self.assertAlmostEqual(self.calculator.sqrt(11), 3.316, places=2)

        with self.assertRaises(TypeError):
            self.calculator.sqrt("string")

        with self.assertRaises(TypeError):
            self.calculator.sqrt([1, "99", 878])

        with self.assertRaises(TypeError):
            self.calculator.sqrt(None)



    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(4, 2), 2)
        self.assertEqual(self.calculator.nth_root(4, 1), 4)
        self.assertEqual(self.calculator.nth_root(100, 2), 10)
        self.assertEqual(self.calculator.nth_root(10, 0.5), 100)
        self.assertAlmostEqual(self.calculator.nth_root(10, -2), 0.316, places=2)

        with self.assertRaises(TypeError):
            self.calculator.nth_root("string", 2)

        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, "99", 878], 2)

        with self.assertRaises(TypeError):
            self.calculator.nth_root(None, 2)


if __name__ == "__main__":
    unittest.main()
