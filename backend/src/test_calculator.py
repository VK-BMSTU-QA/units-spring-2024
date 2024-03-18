import unittest
import math
from .calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 2), 2)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(-1, 2), 1)
        self.assertEqual(self.calculator.addition(-1, -2), -3)

        self.assertEqual(self.calculator.addition(complex(1, 2), complex(1, 0)), complex(2, 2))

        self.assertEqual(self.calculator.addition(math.inf, 10), math.inf)

        self.assertEqual(self.calculator.addition("", ""), "")
        self.assertEqual(self.calculator.addition("aaa", ""), "aaa")

        self.assertEqual(self.calculator.addition(["a"], ["a"]), ["a", "a"])
        self.assertEqual(self.calculator.addition([], []), [])

        self.assertAlmostEqual(self.calculator.addition(1.2, 2.3), 3.5)

        with self.assertRaises(TypeError):
            self.calculator.addition("",1)

        with self.assertRaises(TypeError):
            self.calculator.addition(["a"],("a"))

        with self.assertRaises(TypeError):
            self.calculator.addition({},{{},{}})

        with self.assertRaises(TypeError):
            self.calculator.addition({}, complex(1, 1))

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        self.assertEqual(self.calculator.multiplication(-1, -2), 2)

        self.assertAlmostEqual(self.calculator.multiplication(1.2, 2), 2.4)

        self.assertEqual(self.calculator.multiplication(complex(1, 2), complex(1, 1)), complex(-1, 3))

        self.assertEqual(self.calculator.multiplication(math.inf, -1), -math.inf)

        self.assertEqual(self.calculator.multiplication("b", 2), "bb")

        self.assertEqual(self.calculator.multiplication(["b"], 2), ["b","b"])

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.multiplication("b", "a"), "ba")
                
    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        self.assertEqual(self.calculator.subtraction(0, 2), -2)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(-1, 2), -3)
        self.assertEqual(self.calculator.subtraction(-1, -2), 1)

        self.assertAlmostEqual(self.calculator.subtraction(1.2, 2.2), -1)

        self.assertEqual(self.calculator.subtraction(complex(1, 2), complex(1, 1)), complex(0, 1))

        self.assertTrue(math.isnan(self.calculator.subtraction(math.inf, math.inf)))

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.subtraction("", ""), "")

    def test_division(self):
        self.assertAlmostEqual(self.calculator.division(1, 2), 0.5)
        self.assertAlmostEqual(self.calculator.division(0, 2), 0)
        self.assertEqual(self.calculator.division(1, 0), None)
        self.assertAlmostEqual(self.calculator.division(-1, 2), -0.5)
        self.assertAlmostEqual(self.calculator.division(-1, -2), 0.5)

        self.assertAlmostEqual(self.calculator.division(1.2, 2), 0.6)

        self.assertAlmostEqual(self.calculator.division(10, 3), 3.33333, places=4)

        self.assertEqual(self.calculator.division(complex(0, 1), complex(0, 1)), complex(1, 0))

        self.assertEqual(self.calculator.division(math.inf, 10), math.inf)

        with self.assertRaises(TypeError):
            self.calculator.division("", 1)

    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(1), 1)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(-1), 1)

        self.assertEqual(self.calculator.adsolute(complex(3, 4)), 5)

        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.adsolute(""))

    def test_degree(self):
        self.assertEqual(self.calculator.degree(1, 2), 1)
        self.assertEqual(self.calculator.degree(10, 2), 100)
        self.assertEqual(self.calculator.degree(0, 2), 0)
        self.assertEqual(self.calculator.degree(10,0), 1)
        self.assertEqual(self.calculator.degree(10,1), 10)

        self.assertEqual(self.calculator.degree(4,0.5), 2)

        self.assertAlmostEqual(self.calculator.degree(2,-1), 0.5)

        self.assertEqual(self.calculator.degree(10, math.inf), math.inf)

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.degree("",2))

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.exp(1)), 1)
        self.assertAlmostEqual(self.calculator.ln(math.exp(10)),10)
        self.assertAlmostEqual(self.calculator.ln(1), 0)

        self.assertAlmostEqual(self.calculator.ln(1 / math.exp(1)), -1)

        self.assertEqual(self.calculator.ln(math.inf), math.inf)

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.ln(""))
        
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_log(self):
        self.assertEqual(self.calculator.log(math.e, math.e), 1)
        self.assertEqual(self.calculator.log(4, 2), 2)
        self.assertEqual(self.calculator.log(4, 2), 2)

        self.assertEqual(self.calculator.log(0.5, 2), -1)

        self.assertEqual(self.calculator.log(math.inf, 2), math.inf)

        with self.assertRaises(TypeError):
            self.calculator.log("string", 10)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(1), 1)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(100), 10)

        self.assertAlmostEqual(self.calculator.sqrt(-1), complex(0, 1))

        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.sqrt(""))

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(1, 2), 1)
        self.assertAlmostEqual(self.calculator.nth_root(0, 2), 0)
        self.assertAlmostEqual(self.calculator.nth_root(1000, 3), 10)

        self.assertAlmostEqual(self.calculator.nth_root(1000, -3), 0.1)

        self.assertAlmostEqual(self.calculator.nth_root(-1, 2), complex(0, 1))

        self.assertEqual(self.calculator.nth_root(math.inf, 100), math.inf)

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.nth_root(""))
        


if __name__ == "__main__":
    unittest.main()
