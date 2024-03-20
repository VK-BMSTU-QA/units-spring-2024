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

    def test_abs(self):
        self.assertEqual(self.calculator.absolute(4), 4)
        self.assertEqual(self.calculator.absolute(-7), 7)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 10), 1024)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_log(self):
        self.assertEqual(self.calculator.log(64, 4), 3)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(625), 25)

    def test_nth_sqrt(self):
        self.assertEqual(self.calculator.nth_root(0, 36), 0)


if __name__ == "__main__":
    unittest.main()
