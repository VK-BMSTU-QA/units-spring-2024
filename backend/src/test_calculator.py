import unittest
from calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)

    def test_add_negative(self):
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_add_float(self):
        self.assertAlmostEqual(self.calculator.addition(0.1, 0.2), 0.3)

    def test_add_float_negative(self):
        self.assertAlmostEqual(self.calculator.addition(-0.1, -0.2), -0.3)

    def test_add_None(self):
        self.assertRaises(TypeError, self.calculator.addition, None, None)

    def test_sub(self):
        self.assertEqual(self.calculator.subtraction(2, 1), 1)

    def test_sub_negative(self):
        self.assertEqual(self.calculator.subtraction(2, -1), 3)

    def test_sub_float(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.2, 0.1), 0.1)

    def test_sub_float_negative(self):
        self.assertAlmostEqual(self.calculator.subtraction(0.2, -0.2), 0.4)

    def test_sub_None(self):
        self.assertRaises(TypeError, self.calculator.subtraction, None, 1)

    def test_mul(self):
        self.assertEqual(self.calculator.multiplication(2, 3), 6)

    def test_mul_negative(self):
        self.assertEqual(self.calculator.multiplication(2, -3), -6)

    def test_mul_double_negative(self):
        self.assertEqual(self.calculator.multiplication(-2, -3), 6)

    def test_mul_float(self):
        self.assertEqual(self.calculator.multiplication(2, 3.5), 7.0)

    def test_mul_zero(self):
        self.assertEqual(self.calculator.multiplication(2, 0), 0)

    def test_mul_None(self):
        self.assertRaises(TypeError, self.calculator.multiplication, 1, None)

    def test_div(self):
        self.assertEqual(self.calculator.division(6, 3), 2)

    def test_div_negative(self):
        self.assertAlmostEqual(self.calculator.division(6, -2), -3.0)

    def test_div_float(self):
        self.assertAlmostEqual(self.calculator.division(7, 2), 3.5)

    def test_div_float_negative(self):
        self.assertAlmostEqual(self.calculator.division(7, -2), -3.5)

    def test_div_by_zero(self):
        self.assertEqual(self.calculator.division(6, 0), None)

    def test_div_None(self):
        self.assertRaises(TypeError, self.calculator.division, 4, None)

    def test_abs(self):
        self.assertEqual(self.calculator.adsolute(-8), 8)

    def test_abs_positive(self):
        self.assertEqual(self.calculator.absolute(8), 8)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.absolute(0), 0)

    def test_abs_float(self):
        self.assertAlmostEqual(self.calculator.absolute(8.48), 8.48)

    def test_abs_float_negative(self):
        self.assertAlmostEqual(self.calculator.absolute(-8.48), 8.48)

    def test_abs_None(self):
        self.assertRaises(TypeError, self.calculator.absolute, None)

    def test_deg(self):
        self.assertEqual(self.calculator.degree(5, 3), 125)

    def test_deg_negative_degree(self):
        self.assertAlmostEqual(self.calculator.degree(2, -3), 0.125)

    def test_deg_negative_base(self):
        self.assertAlmostEqual(self.calculator.degree(-2, 3), -8.0)

    def test_deg_float_base(self):
        self.assertAlmostEqual(self.calculator.degree(0.5, 2), 0.25)

    def test_deg_float_degree(self):
        self.assertAlmostEqual(self.calculator.degree(4, 0.5), 2.0)

    def test_deg_zero_degree(self):
        self.assertEqual(self.calculator.degree(4, 0), 1)

    def test_deg_None_base(self):
        self.assertRaises(TypeError, self.calculator.degree, None, 2)

    def test_deg_None_degree(self):
        self.assertRaises(TypeError, self.calculator.degree, 2, None)

    def test_ln(self):
        self.assertEqual(self.calculator.ln(1), 0)

    def test_ln_negative(self):
        self.assertRaises(ValueError, self.calculator.ln, -1)

    def test_ln_None(self):
        self.assertRaises(TypeError, self.calculator.ln, None)

    def test_log(self):
        self.assertEqual(self.calculator.log(64, 2), 6)

    def test_log(self):
        self.assertEqual(self.calculator.log(64, 2), 6)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(36), 6)

    def test_root(self):
        self.assertEqual(self.calculator.nth_root(27, 3), 3)




if __name__ == "__main__":
    unittest.main()
