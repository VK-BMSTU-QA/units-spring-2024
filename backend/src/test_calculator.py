import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertEqual(self.calculator.addition(1, -6), -5)
        self.assertEqual(self.calculator.addition(4, 0), 4)
        self.assertEqual(self.calculator.addition(-8, -8), -16)
        self.assertEqual(self.calculator.addition(-8, 8), 0)
        self.assertEqual(self.calculator.addition(13.6, 2.2), 15.8)
        self.assertEqual(self.calculator.addition([1], ["1"]), [1, "1"])
        self.assertEqual(self.calculator.addition("1", "2"), "12")

        with self.assertRaises(TypeError) as context:
            self.calculator.addition()
        self.assertTrue("missing 2 required positional arguments" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            self.calculator.addition(None, None)
        self.assertEqual( str(context.exception), "unsupported operand type(s) for +: 'NoneType' and 'NoneType'")

        with self.assertRaises(TypeError) as context:
            self.calculator.addition("6", 12)
        self.assertTrue("can only concatenate str", str(context.exception))
    
    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(5, 6), 30)
        self.assertEqual(self.calculator.multiplication("ab", 3), "ababab")
        self.assertEqual(self.calculator.multiplication(19, 0), 0)
        self.assertEqual(self.calculator.multiplication(-8, 1), -8)
        self.assertEqual(self.calculator.multiplication(-8, -1), 8)
        self.assertEqual(self.calculator.multiplication(5, 0.5), 2.5)

        with self.assertRaises(TypeError) as context:
            self.calculator.multiplication()
        self.assertTrue("missing 2 required positional arguments" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            self.calculator.multiplication("1", "4")
        self.assertEqual( str(context.exception), "can't multiply sequence by non-int of type 'str'")

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(20, 27), -7)
        self.assertEqual(self.calculator.subtraction(-7, -7), 0)
        self.assertEqual(self.calculator.subtraction(4.7, 1.2), 3.5)


        with self.assertRaises(TypeError) as context:
            self.calculator.subtraction()
        self.assertTrue("missing 2 required positional arguments" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            self.calculator.subtraction("1", "4")
        self.assertEqual( str(context.exception), "unsupported operand type(s) for -: 'str' and 'str'")

    def test_div(self):
        self.assertEqual(self.calculator.division(30, 6), 5)
        self.assertEqual(self.calculator.division(30, 0), None)
        self.assertEqual(self.calculator.division(0, 30), 0)
        self.assertAlmostEqual(self.calculator.division(1, 3), 0.333333333)

        with self.assertRaises(TypeError) as context:
            self.calculator.division()
        self.assertTrue("missing 2 required positional arguments" in str(context.exception))

    def test_abs(self):
        self.assertEqual(self.calculator.absolute(4), 4)
        self.assertEqual(self.calculator.absolute(-7), 7)
        self.assertEqual(self.calculator.absolute(-7.45), 7.45)
        self.assertEqual(self.calculator.absolute(0), 0)

        with self.assertRaises(TypeError) as context:
            self.calculator.absolute()
        self.assertTrue("missing 1 required positional argument" in str(context.exception))

        with self.assertRaises(TypeError) as context:
            self.calculator.absolute(None)
        self.assertEqual( str(context.exception), "bad operand type for abs(): 'NoneType'")

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 10), 1024)
        self.assertEqual(self.calculator.degree(25, 0.5), 5)
        self.assertEqual(self.calculator.degree(2, -1), 0.5)
        self.assertEqual(self.calculator.degree(-4, -1), -0.25)
        self.assertEqual(self.calculator.degree(0.04, 2), 0.0016)
        self.assertEqual(self.calculator.degree(0, 12), 0)
        self.assertEqual(self.calculator.degree(23, 0), 1)

        with self.assertRaises(TypeError) as context:
            self.calculator.degree()
        self.assertTrue("missing 2 required positional arguments" in str(context.exception))

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

        with self.assertRaises(ValueError) as context:
            self.calculator.ln(0)

        with self.assertRaises(ValueError) as context:
            self.calculator.ln(-56)

        with self.assertRaises(TypeError) as context:
            self.calculator.ln()
        self.assertTrue("missing 1 required positional argument" in str(context.exception))

    def test_log(self):
        self.assertEqual(self.calculator.log(64, 4), 3)
        self.assertEqual(self.calculator.log(0.0625, 0.5), 4)
        self.assertEqual(self.calculator.log(0.125, 2), -3)

        with self.assertRaises(TypeError) as context:
            self.calculator.log()
        self.assertTrue("missing 2 required positional arguments" in str(context.exception))

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(625), 25)
        self.assertEqual(self.calculator.sqrt(0), 0)
        self.assertEqual(self.calculator.sqrt(0.0121), 0.11)
        self.assertAlmostEqual(self.calculator.sqrt(5), 2.2360679774)
        self.assertAlmostEqual(self.calculator.sqrt(-16), 4j)

        with self.assertRaises(TypeError) as context:
            self.calculator.sqrt()
        self.assertTrue("missing 1 required positional argument" in str(context.exception))

    def test_nth_sqrt(self):
        self.assertEqual(self.calculator.nth_root(0, 36), 0)
        self.assertEqual(self.calculator.nth_root(625, 4), 5)
        self.assertEqual(self.calculator.nth_root(0, 7), 0)
        self.assertEqual(self.calculator.nth_root(0.0121, 1), 0.0121)

        with self.assertRaises(TypeError) as context:
            self.calculator.nth_root()
        self.assertTrue("missing 2 required positional arguments" in str(context.exception))


if __name__ == "__main__":
    unittest.main()
