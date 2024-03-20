import unittest
import math

from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(3, 5), 8)
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        self.assertEqual(self.calculator.addition(0, 0), 0)

        self.assertAlmostEqual(self.calculator.addition(2.5, 3.5), 6.0)
        self.assertEqual(self.calculator.addition(complex(3, 5), complex(2, 1)), complex(5, 6))
        self.assertEqual(self.calculator.addition(complex(1, 2), 3), complex(4, 2))

        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)

        self.assertEqual(self.calculator.addition("hello", "world"), "helloworld")
        self.assertEqual(self.calculator.addition("123", "456"), "123456")

        self.assertEqual(self.calculator.addition(["apple"], ["orange"]), ["apple", "orange"])
        self.assertEqual(self.calculator.addition([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

        self.assertRaises(TypeError, self.calculator.addition, "apple", 5)
        self.assertRaises(TypeError, self.calculator.addition, [1, 2, 3], 4)
        self.assertRaises(TypeError, self.calculator.addition, {}, "test")
        self.assertRaises(TypeError, self.calculator.addition, complex(1, 2), [1, 2])

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 5), 15)
        self.assertEqual(self.calculator.multiplication(-2, 4), -8)
        self.assertEqual(self.calculator.multiplication(0, 10), 0)

        self.assertAlmostEqual(self.calculator.multiplication(2.5, 3.5), 8.75)
        self.assertEqual(self.calculator.multiplication(complex(3, 5), complex(2, 1)), complex(1, 13))
        self.assertEqual(self.calculator.multiplication(complex(1, 2), 3), complex(3, 6))

        self.assertEqual(self.calculator.multiplication(math.inf, 10), math.inf)

        self.assertEqual(self.calculator.multiplication("hello", 3), "hellohellohello")
        self.assertEqual(self.calculator.multiplication("abc", 0), "")

        self.assertEqual(self.calculator.multiplication(["apple"], 3), ["apple", "apple", "apple"])
        self.assertEqual(self.calculator.multiplication([1, 2], 2), [1, 2, 1, 2])

        self.assertRaises(TypeError, self.calculator.multiplication, "apple", "orange")
        self.assertRaises(TypeError, self.calculator.multiplication, [1, 2, 3], [4, 5, 6])
        self.assertRaises(TypeError, self.calculator.multiplication, {}, "test")
        self.assertRaises(TypeError, self.calculator.multiplication, complex(1, 1), [1, 2])

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 3), 2)
        self.assertEqual(self.calculator.subtraction(3, 5), -2)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

        self.assertAlmostEqual(self.calculator.subtraction(5.5, 3.5), 2.0)
        self.assertAlmostEqual(self.calculator.subtraction(2.5, 3.5), -1.0)

        self.assertEqual(self.calculator.subtraction(complex(3, 5), complex(2, 1)), complex(1, 4))
        self.assertEqual(self.calculator.subtraction(complex(1, 2), 3), complex(-2, 2)) 

        self.assertEqual(self.calculator.subtraction(math.inf, 1), math.inf)
        
        self.assertRaises(TypeError, self.calculator.subtraction, "hello", "world")
        self.assertRaises(TypeError, self.calculator.subtraction, "123", "456")
        self.assertRaises(TypeError, self.calculator.subtraction, ["apple", "orange"], ["orange"])
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2, 3, 4, 5], [4, 5, 6])
        self.assertRaises(TypeError, self.calculator.subtraction, "apple", 5)
        self.assertRaises(TypeError, self.calculator.subtraction, [1, 2, 3], "test")
        self.assertRaises(TypeError, self.calculator.subtraction, complex(1, 2), [1, 2])
        self.assertRaises(TypeError, self.calculator.subtraction, {}, 4)

    def test_division(self):
        self.assertEqual(self.calculator.division(10, 5), 2)
        self.assertEqual(self.calculator.division(7, 2), 3.5)
        self.assertIsNone(self.calculator.division(10, 0))

        self.assertAlmostEqual(self.calculator.division(2.4, 2), 1.2)
        self.assertAlmostEqual(self.calculator.division(10, 3), 3.33333, places=4)

        self.assertEqual(self.calculator.division(complex(3, 5), complex(2, 1)), complex(2.2, 1.4))
        self.assertAlmostEqual(self.calculator.division(complex(1, 2), 3), complex(0.33333, 0.66666), places=4)

        self.assertEqual(self.calculator.division(math.inf, 2), math.inf)
        self.assertIsNone(self.calculator.division(math.inf, 0))

        self.assertRaises(TypeError, self.calculator.division, "hello", "world")
        self.assertRaises(TypeError, self.calculator.division, "123", "456")
        self.assertRaises(TypeError, self.calculator.division, ["apple", "orange"], ["orange"])
        self.assertRaises(TypeError, self.calculator.division, [1, 2, 3, 4, 5], [4, 5, 6])
        self.assertRaises(TypeError, self.calculator.division, "apple", 5)
        self.assertRaises(TypeError, self.calculator.division, [1, 2, 3], "test")
        self.assertRaises(TypeError, self.calculator.division, complex(1, 2), [1, 2])
        self.assertRaises(TypeError, self.calculator.division, {}, 4)

    def test_absolute(self):
        self.assertEqual(self.calculator.absolute(5), 5)
        self.assertEqual(self.calculator.absolute(-5), 5)
        self.assertEqual(self.calculator.absolute(0), 0)

        self.assertAlmostEqual(self.calculator.absolute(-2.5), 2.5)
        self.assertAlmostEqual(self.calculator.absolute(3.14159), 3.14159)

        self.assertEqual(self.calculator.absolute(complex(3, 4)), 5)
        self.assertAlmostEqual(self.calculator.absolute(complex(-1, -1)), 1.4142, places=4)

        self.assertEqual(self.calculator.absolute(math.inf), math.inf)
        self.assertRaises(TypeError, self.calculator.absolute, "hello")
        self.assertRaises(TypeError, self.calculator.absolute, ["apple", "orange"])
        self.assertRaises(TypeError, self.calculator.absolute, {"apple": 1, "orange": 2})

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertEqual(self.calculator.degree(5, 0), 1)
        self.assertAlmostEqual(self.calculator.degree(3, -1), 1/3)

        self.assertAlmostEqual(self.calculator.degree(2.5, 1.2), 3.0028, places=4)
        self.assertAlmostEqual(self.calculator.degree(2.5, -1.2), 0.3330212829607493, places=4)

        self.assertEqual(self.calculator.degree(complex(2, 3), 2), complex(-5, 12))
        self.assertAlmostEqual(self.calculator.degree(complex(1, 1), 3.3), complex(-2.6759, 1.6398), places=4)

        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertRaises(TypeError, self.calculator.degree, "hello", 2)
        self.assertRaises(TypeError, self.calculator.degree, ["apple", "orange"], 3)
        self.assertRaises(TypeError, self.calculator.degree, {"apple": 1, "orange": 2}, 4)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(1), 0.0)  
        self.assertAlmostEqual(self.calculator.ln(math.e), 1.0) 
        self.assertAlmostEqual(self.calculator.ln(10), 2.3026, places=4)
        self.assertAlmostEqual(self.calculator.ln(235.235), 5.4606, places=4)

        self.assertEqual(self.calculator.ln(math.inf), math.inf)

        self.assertRaises(ValueError, self.calculator.ln, 0)
        self.assertRaises(ValueError, self.calculator.ln, -1)

        self.assertRaises(TypeError, self.calculator.ln, "hello")
        self.assertRaises(TypeError, self.calculator.ln, ["apple", "orange"])
        self.assertRaises(TypeError, self.calculator.ln, {"apple": 1, "orange": 2})

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(8, 2), 3.0) 
        self.assertAlmostEqual(self.calculator.log(1000, 10), 3.0)  
        self.assertAlmostEqual(self.calculator.log(math.e, math.e), 1.0)
        self.assertAlmostEqual(self.calculator.log(16, 100), 0.602059991)
        self.assertAlmostEqual(self.calculator.log(12.332, 1231.312), 0.3530, places=4)  



        self.assertEqual(self.calculator.log(math.inf, 10), math.inf)

        self.assertRaises(ValueError, self.calculator.log, 0, 10)
        self.assertRaises(ValueError, self.calculator.log, 10, 0)
        self.assertRaises(ValueError, self.calculator.log, 1, -1)
        self.assertRaises(ZeroDivisionError, self.calculator.log, 1, 1)

        self.assertRaises(TypeError, self.calculator.log, "hello", 10)
        self.assertRaises(TypeError, self.calculator.log, 100, "world")
        self.assertRaises(TypeError, self.calculator.log, ["apple", "orange"], 10)
        self.assertRaises(TypeError, self.calculator.log, {"apple": 1, "orange": 2}, 10)
            

    def test_sqrt(self):
        self.assertAlmostEqual(self.calculator.sqrt(4), 2.0)
        self.assertAlmostEqual(self.calculator.sqrt(81.81), 9.0449, places=4)
        self.assertAlmostEqual(self.calculator.sqrt(2), math.sqrt(2))
        self.assertAlmostEqual(self.calculator.sqrt(0), 0)
        self.assertAlmostEqual(self.calculator.sqrt(123), 11.0905, places=4)

        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)

        self.assertAlmostEqual(self.calculator.sqrt(-25), complex(3.061616997868383e-16, 5))

        self.assertRaises(TypeError, self.calculator.sqrt, "hello")
        self.assertRaises(TypeError, self.calculator.sqrt, ["apple", "orange"])
        self.assertRaises(TypeError, self.calculator.sqrt, {"apple": 1, "orange": 2})

    def test_nth_root(self):
        self.assertAlmostEqual(self.calculator.nth_root(8, 3), 2.0) 
        self.assertAlmostEqual(self.calculator.nth_root(16, 4), 2)
        self.assertAlmostEqual(self.calculator.nth_root(153, 3), 5.3485, places=4)
        self.assertAlmostEqual(self.calculator.nth_root(2144.3444, 124), 1.0638, places=4)

        self.assertEqual(self.calculator.nth_root(math.inf, 100), math.inf)

        self.assertAlmostEqual(self.calculator.nth_root(-25, 2), complex(3.061616997868383e-16, 5))

        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 25, 0)

        self.assertRaises(TypeError, self.calculator.nth_root, "hello", 2)
        self.assertRaises(TypeError, self.calculator.nth_root, 100, "world")
        self.assertRaises(TypeError, self.calculator.nth_root, ["apple", "orange"], 2)
        self.assertRaises(TypeError, self.calculator.nth_root, {"apple": 1, "orange": 2}, 2)

if __name__ == "__main__":
    unittest.main()
