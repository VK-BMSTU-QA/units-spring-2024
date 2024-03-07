import unittest
from . import calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = calculator.Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(0, 2), 2)
        self.assertEqual(self.calculator.addition(0, 0), 0)
        self.assertEqual(self.calculator.addition(-1, 2), 1)
        self.assertEqual(self.calculator.addition(-1, -2), -3)

        self.assertEqual(self.calculator.addition(complex(1, 2), complex(1, 0)), complex(2, 2))

        self.assertEqual(self.calculator.addition("", ""), "")
        self.assertEqual(self.calculator.addition("aaa", ""), "aaa")

        self.assertEqual(self.calculator.addition(["a"], ["a"]), ["a", "a"])
        self.assertEqual(self.calculator.addition([], []), [])

        self.assertAlmostEqual(self.calculator.addition(1.2, 2.3), 3.5)

        with self.assertRaises(TypeError):
            self.calculator.addition("",1)

    def test_multiplication(self):
            self.assertEqual(self.calculator.multiplication(1, 2), 2)
            self.assertEqual(self.calculator.multiplication(0, 2), 0)
            self.assertEqual(self.calculator.multiplication(0, 0), 0)

            self.assertEqual(self.calculator.multiplication(-1, 2), -2)
            self.assertEqual(self.calculator.multiplication(-1, -2), 2)

            self.assertAlmostEqual(self.calculator.multiplication(1.2, 2), 2.4)

            self.assertEqual(self.calculator.multiplication(complex(1, 2), complex(1, 1)), complex(-1, 3))

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

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.subtraction("", ""), "")

    def test_division(self):
        self.assertAlmostEqual(self.calculator.division(1, 2), 0.5)
        self.assertAlmostEqual(self.calculator.division(0, 2), 0)
        self.assertEqual(self.calculator.division(1, 0), None)
        self.assertAlmostEqual(self.calculator.division(-1, 2), -0.5)
        self.assertAlmostEqual(self.calculator.division(-1, -2), 0.5)

        self.assertEqual(self.calculator.division(complex(0, 1), complex(0, 1)), complex(1, 0))

        self.assertAlmostEqual(self.calculator.division(1.2, 2), 0.6)

        with self.assertRaises(TypeError):
            self.calculator.division("", 1)

    def test_absolute(self):
        self.assertEqual(self.calculator.adsolute(1), 1)
        self.assertEqual(self.calculator.adsolute(0), 0)
        self.assertEqual(self.calculator.adsolute(-1), 1)

        self.assertEqual(self.calculator.adsolute(complex(3, 4)), 5)

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

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.degree("",2))

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(math.exp(1)), 1)
        self.assertAlmostEqual(self.calculator.ln(math.exp(10)),10)
        self.assertAlmostEqual(self.calculator.ln(1), 0)

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.ln(""))
        
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(1), 1)
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(100), 10)

        self.assertAlmostEqual(self.calculator.sqrt(-1), complex(0, 1))

        with self.assertRaises(TypeError):
            self.assertEqual(self.calculator.sqrt(""))
        


if __name__ == "__main__":
    unittest.main()
