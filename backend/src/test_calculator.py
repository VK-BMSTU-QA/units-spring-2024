import unittest
from src.calculator import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.addition(1, 2), 3)
        self.assertAlmostEqual(self.calculator.addition(1, 2.1), 3.1)
        self.assertAlmostEqual(self.calculator.addition(1.1, 2), 3.1)
        self.assertAlmostEqual(self.calculator.addition(1.1, 2.1), 3.2)

    def test_addition_negative(self):
        self.assertEqual(self.calculator.addition(-1, 2), 1)
        self.assertEqual(self.calculator.addition(1, -2), -1)
        self.assertEqual(self.calculator.addition(-1, -2), -3)

    def test_addition_zero(self):
        self.assertEqual(self.calculator.addition(0, 2), 2)
        self.assertEqual(self.calculator.addition(2, 0), 2)
        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)
        self.assertAlmostEqual(self.calculator.multiplication(3.1, 2.1), 6.51)
        self.assertAlmostEqual(self.calculator.multiplication(3, 2.1), 6.3)
        self.assertAlmostEqual(self.calculator.multiplication(3.1, 2), 6.2)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)
        self.assertEqual(self.calculator.multiplication(3, -2), -6)
        self.assertEqual(self.calculator.multiplication(-3, -2), 6)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertEqual(self.calculator.multiplication(2, 0), 0)
        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 2), 3)
        self.assertAlmostEqual(self.calculator.subtraction(5.2, 2), 3.2)
        self.assertAlmostEqual(self.calculator.subtraction(5, 2.2), 2.8)
        self.assertAlmostEqual(self.calculator.subtraction(5.5, 2.2), 3.3)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(5, -2), 7)
        self.assertEqual(self.calculator.subtraction(-5, 2), -7)
        self.assertEqual(self.calculator.subtraction(-5, -2), -3)

    def test_subtraction_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 2), -2)
        self.assertEqual(self.calculator.subtraction(2, 0), 2)
        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_division(self):
        self.assertEqual(self.calculator.division(6, 2), 3)
        self.assertAlmostEqual(self.calculator.division(5, 2), 2.5)
        self.assertAlmostEqual(self.calculator.division(5.2, 2), 2.6)
        self.assertAlmostEqual(self.calculator.division(5, 2.2), 2.2727272727)
        self.assertAlmostEqual(self.calculator.division(5.5, 2.2), 2.5)

    def test_division_negative(self):
        self.assertEqual(self.calculator.division(6, -2), -3)
        self.assertEqual(self.calculator.division(-6, 2), -3)
        self.assertEqual(self.calculator.division(-6, -2), 3)

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(0, 2), 0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))
        self.assertIsNone(self.calculator.division(52.4, 0))
        self.assertIsNone(self.calculator.division(0, 0), 0)

    def test_abs_positive(self):
        self.assertEqual(self.calculator.adsolute(5), 5)
        self.assertEqual(self.calculator.adsolute(5.4), 5.4)

    def test_abs_negative(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(-5.4), 5.4)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertAlmostEqual(self.calculator.degree(2.2, 3), 10.648)
        self.assertAlmostEqual(self.calculator.degree(2, 2.2), 4.5947934200)
        self.assertAlmostEqual(self.calculator.degree(2.2, 2.2), 5.6666957788)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertAlmostEqual(self.calculator.degree(2, -2), 0.25)

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 3), 0)
        self.assertEqual(self.calculator.degree(2, 0), 1)
        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(10), 2.302585092994046)
        self.assertAlmostEqual(self.calculator.ln(5.5), 1.7047480922384253)

    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-10)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(10, 2), 3.3219280948873626)
        self.assertAlmostEqual(self.calculator.log(5.5, 2), 2.4594316186372973)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-10, 2)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertAlmostEqual(self.calculator.sqrt(8), 2.8284271247)
        self.assertAlmostEqual(self.calculator.sqrt(2.5), 1.5811388301)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(
            self.calculator.sqrt(-2),
            (8.659560562354934e-17+1.4142135623730951j),
        )

    def test_nth_root(self):
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        self.assertAlmostEqual(
            self.calculator.nth_root(4, 3),
            1.5874010519681994,
        )

        self.assertAlmostEqual(
            self.calculator.nth_root(2.5, 5),
            1.2011244339814313,
        )

        self.assertAlmostEqual(
            self.calculator.nth_root(2, 5.1),
            1.1455801751628705
        )

        self.assertAlmostEqual(self.calculator.nth_root(
            2.5, 5.1),
            1.1968161822205403,
        )

    def test_nth_root_negative(self):
        self.assertAlmostEqual(
            self.calculator.nth_root(-2, 3),
            (0.6299605249474367+1.0911236359717214j),
        )


if __name__ == "__main__":
    unittest.main()
