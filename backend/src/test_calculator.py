import math
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

        self.assertAlmostEqual(self.calculator.addition(-1.2, 2.1), 0.9)
        self.assertAlmostEqual(self.calculator.addition(1.1, -2.2), -1.1)
        self.assertAlmostEqual(self.calculator.addition(-1.1, -2.1), -3.2)

    def test_addition_zero(self):
        self.assertEqual(self.calculator.addition(0, 2), 2)
        self.assertEqual(self.calculator.addition(2, 0), 2)

        self.assertAlmostEqual(self.calculator.addition(0, 2.2), 2.2)
        self.assertAlmostEqual(self.calculator.addition(2.2, 0), 2.2)

        self.assertEqual(self.calculator.addition(0, -2), -2)
        self.assertEqual(self.calculator.addition(-2, 0), -2)

        self.assertEqual(self.calculator.addition(0, -2.2), -2.2)
        self.assertEqual(self.calculator.addition(-2.2, 0), -2.2)

        self.assertEqual(self.calculator.addition(0, math.inf), math.inf)
        self.assertEqual(self.calculator.addition(math.inf, 0), math.inf)

        self.assertEqual(self.calculator.addition(0, 0), 0)

    def test_addition_string(self):
        self.assertEqual(
            self.calculator.addition('first', 'second'),
            'firstsecond',
        )
        self.assertEqual(
            self.calculator.addition('', 'second'),
            'second',
        )
        self.assertEqual(
            self.calculator.addition('first', ''),
            'first',
        )
        self.assertEqual(
            self.calculator.addition('', ''),
            '',
        )

    def test_addition_list(self):
        self.assertEqual(
            self.calculator.addition([1, 2], [3, 4]),
            [1, 2, 3, 4],
        )
        self.assertEqual(
            self.calculator.addition([], [3, 4]),
            [3, 4],
        )
        self.assertEqual(
            self.calculator.addition([1, 2], []),
            [1, 2],
        )
        self.assertEqual(
            self.calculator.addition([], []),
            [],
        )

    def test_addition_different_types_operands(self):
        with self.assertRaises(TypeError):
            self.calculator.addition(1, 'string')

        with self.assertRaises(TypeError):
            self.calculator.addition('string', 1)

        with self.assertRaises(TypeError):
            self.calculator.addition(1, [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.addition([1, 2], 1)

        with self.assertRaises(TypeError):
            self.calculator.addition([1, 2], 'string')

    def test_addition_infinity(self):
        self.assertEqual(self.calculator.addition(1, math.inf), math.inf)
        self.assertEqual(self.calculator.addition(math.inf, 1), math.inf)
        self.assertEqual(self.calculator.addition(
            math.inf, math.inf),
            math.inf,
        )

        self.assertEqual(self.calculator.addition(1, -math.inf), -math.inf)
        self.assertEqual(self.calculator.addition(-math.inf, 1), -math.inf)
        self.assertEqual(self.calculator.addition(
            -math.inf, -math.inf),
            -math.inf,
        )

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiplication(3, 2), 6)
        self.assertAlmostEqual(self.calculator.multiplication(3.1, 2.1), 6.51)
        self.assertAlmostEqual(self.calculator.multiplication(3, 2.1), 6.3)
        self.assertAlmostEqual(self.calculator.multiplication(3.1, 2), 6.2)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiplication(-3, 2), -6)
        self.assertEqual(self.calculator.multiplication(3, -2), -6)
        self.assertEqual(self.calculator.multiplication(-3, -2), 6)

        self.assertAlmostEqual(
            self.calculator.multiplication(-1.2, 2.1),
            -2.52,
        )
        self.assertAlmostEqual(
            self.calculator.multiplication(1.1, -2.2),
            -2.42,
        )
        self.assertAlmostEqual(
            self.calculator.multiplication(-1.1, -2.1),
            2.31,
        )

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiplication(0, 2), 0)
        self.assertEqual(self.calculator.multiplication(2, 0), 0)

        self.assertAlmostEqual(self.calculator.multiplication(0, 2.2), 0)
        self.assertAlmostEqual(self.calculator.multiplication(2.2, 0), 0)

        self.assertEqual(self.calculator.multiplication(0, -2), 0)
        self.assertEqual(self.calculator.multiplication(-2, 0), 0)

        self.assertEqual(self.calculator.multiplication(0, -2.2), 0)
        self.assertEqual(self.calculator.multiplication(-2.2, 0), 0)

        self.assertTrue(math.isnan(
            self.calculator.multiplication(0, math.inf)),
        )
        self.assertTrue(math.isnan(
            self.calculator.multiplication(math.inf, 0)),
        )

        self.assertEqual(self.calculator.multiplication(0, 0), 0)

    def test_multiplication_string(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication('first', 'second')

        with self.assertRaises(TypeError):
            self.calculator.multiplication('first', '')

        with self.assertRaises(TypeError):
            self.calculator.multiplication('', 'second')

        with self.assertRaises(TypeError):
            self.calculator.multiplication('', '')

    def test_multiplication_list(self):
        with self.assertRaises(TypeError):
            self.calculator.multiplication([1, 2], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.multiplication([1, 2], [])

        with self.assertRaises(TypeError):
            self.calculator.multiplication([], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.multiplication([], [])

    def test_multiplication_different_types_operands(self):
        self.assertEqual(
            self.calculator.multiplication('string', 2),
            'stringstring',
        )

        self.assertEqual(
            self.calculator.multiplication(2, 'string'),
            'stringstring',
        )

        self.assertEqual(
            self.calculator.multiplication('string', 0),
            '',
        )

        self.assertEqual(
            self.calculator.multiplication(0, 'string'),
            '',
        )

        self.assertEqual(
            self.calculator.multiplication([1, 2], 2),
            [1, 2, 1, 2],
        )

        self.assertEqual(
            self.calculator.multiplication(2, [1, 2]),
            [1, 2, 1, 2],
        )

        self.assertEqual(
            self.calculator.multiplication([1, 2], 0),
            [],
        )

        self.assertEqual(
            self.calculator.multiplication(0, [1, 2]),
            [],
        )

        with self.assertRaises(TypeError):
            self.calculator.multiplication('string', [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.multiplication([1, 2], 'string')

    def test_multiplication_infinity(self):
        self.assertEqual(self.calculator.multiplication(2, math.inf), math.inf)
        self.assertEqual(self.calculator.multiplication(math.inf, 2), math.inf)
        self.assertEqual(
            self.calculator.multiplication(math.inf, math.inf),
            math.inf
        )

        self.assertEqual(self.calculator.multiplication(
            2, -math.inf),
            -math.inf,
        )
        self.assertEqual(
            self.calculator.multiplication(-math.inf, 2),
            -math.inf,
        )
        self.assertEqual(
            self.calculator.multiplication(-math.inf, -math.inf),
            math.inf
        )

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtraction(5, 2), 3)
        self.assertAlmostEqual(self.calculator.subtraction(5.2, 2), 3.2)
        self.assertAlmostEqual(self.calculator.subtraction(5, 2.2), 2.8)
        self.assertAlmostEqual(self.calculator.subtraction(5.5, 2.2), 3.3)

    def test_subtraction_negative(self):
        self.assertEqual(self.calculator.subtraction(5, -2), 7)
        self.assertEqual(self.calculator.subtraction(-5, 2), -7)
        self.assertEqual(self.calculator.subtraction(-5, -2), -3)

        self.assertAlmostEqual(self.calculator.subtraction(-1.2, 2.1), -3.3)
        self.assertAlmostEqual(self.calculator.subtraction(1.1, -2.2), 3.3)
        self.assertAlmostEqual(self.calculator.subtraction(-1.1, -2.1), 1)

    def test_subtraction_zero(self):
        self.assertEqual(self.calculator.subtraction(0, 2), -2)
        self.assertEqual(self.calculator.subtraction(2, 0), 2)

        self.assertAlmostEqual(self.calculator.subtraction(0, 2.2), -2.2)
        self.assertAlmostEqual(self.calculator.subtraction(2.2, 0), 2.2)

        self.assertEqual(self.calculator.subtraction(0, -2), 2)
        self.assertEqual(self.calculator.subtraction(-2, 0), -2)

        self.assertAlmostEqual(self.calculator.subtraction(0, -2.2), 2.2)
        self.assertAlmostEqual(self.calculator.subtraction(-2.2, 0), -2.2)

        self.assertEqual(self.calculator.subtraction(0, math.inf), -math.inf)
        self.assertEqual(self.calculator.subtraction(math.inf, 0), math.inf)

        self.assertEqual(self.calculator.subtraction(0, 0), 0)

    def test_subtraction_string(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('first', 'second')

        with self.assertRaises(TypeError):
            self.calculator.subtraction('first', '')

        with self.assertRaises(TypeError):
            self.calculator.subtraction('', 'second')

        with self.assertRaises(TypeError):
            self.calculator.subtraction('', '')

    def test_subtraction_list(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, 2], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, 2], [])

        with self.assertRaises(TypeError):
            self.calculator.subtraction([], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.subtraction([], [])

    def test_subtraction_different_types_operands(self):
        with self.assertRaises(TypeError):
            self.calculator.subtraction('string', 2)

        with self.assertRaises(TypeError):
            self.calculator.subtraction(2, 'string')

        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, 2], 2)

        with self.assertRaises(TypeError):
            self.calculator.subtraction(2, [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.subtraction('string', [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.subtraction([1, 2], 'string')

    def test_subtraction_infinity(self):
        self.assertEqual(self.calculator.subtraction(2, math.inf), -math.inf)
        self.assertEqual(self.calculator.subtraction(math.inf, 2), math.inf)
        self.assertTrue(math.isnan(
            self.calculator.subtraction(math.inf, math.inf)),
        )

        self.assertEqual(self.calculator.subtraction(2, -math.inf), math.inf)
        self.assertEqual(self.calculator.subtraction(-math.inf, 2), -math.inf)
        self.assertTrue(math.isnan(
            self.calculator.subtraction(-math.inf, -math.inf)),
        )

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

        self.assertAlmostEqual(
            self.calculator.division(-1.2, 2.1),
            -0.5714285714,
        )
        self.assertAlmostEqual(
            self.calculator.division(1.1, -2.2),
            -0.5,
        )
        self.assertAlmostEqual(
            self.calculator.division(-1.1, -2.1),
            0.5238095238,
        )

    def test_division_zero(self):
        self.assertEqual(self.calculator.division(0, 2), 0)
        self.assertEqual(self.calculator.division(0, 2.2), 0)
        self.assertEqual(self.calculator.division(0, -2), 0)
        self.assertEqual(self.calculator.division(0, -2.2), 0)
        self.assertEqual(self.calculator.division(0, math.inf), 0)

    def test_division_by_zero(self):
        self.assertIsNone(self.calculator.division(5, 0))
        self.assertIsNone(self.calculator.division(52.4, 0))
        self.assertIsNone(self.calculator.division(0, 0), 0)
        self.assertEqual(self.calculator.subtraction(math.inf, 0), math.inf)

    def test_division_string(self):
        with self.assertRaises(TypeError):
            self.calculator.division('first', 'second')

        with self.assertRaises(TypeError):
            self.calculator.division('first', '')

        with self.assertRaises(TypeError):
            self.calculator.division('', 'second')

        with self.assertRaises(TypeError):
            self.calculator.division('', '')

    def test_division_list(self):
        with self.assertRaises(TypeError):
            self.calculator.division([1, 2], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.division([1, 2], [])

        with self.assertRaises(TypeError):
            self.calculator.division([], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.division([], [])

    def test_division_different_types_operands(self):
        with self.assertRaises(TypeError):
            self.calculator.division('string', 2)

        with self.assertRaises(TypeError):
            self.calculator.division(2, 'string')

        with self.assertRaises(TypeError):
            self.calculator.division([1, 2], 2)

        with self.assertRaises(TypeError):
            self.calculator.division(2, [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.division('string', [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.division([1, 2], 'string')

    def test_division_infinity(self):
        self.assertEqual(self.calculator.division(2, math.inf), 0)
        self.assertEqual(self.calculator.division(math.inf, 2), math.inf)
        self.assertTrue(math.isnan(
            self.calculator.division(math.inf, math.inf)),
        )

        self.assertEqual(self.calculator.division(2, -math.inf), 0)
        self.assertEqual(self.calculator.division(-math.inf, 2), -math.inf)
        self.assertTrue(math.isnan(
            self.calculator.division(-math.inf, -math.inf)),
        )

    def test_abs_positive(self):
        self.assertEqual(self.calculator.adsolute(5), 5)
        self.assertEqual(self.calculator.adsolute(5.4), 5.4)

    def test_abs_negative(self):
        self.assertEqual(self.calculator.adsolute(-5), 5)
        self.assertEqual(self.calculator.adsolute(-5.4), 5.4)

    def test_abs_zero(self):
        self.assertEqual(self.calculator.adsolute(0), 0)

    def test_abs_string(self):
        with self.assertRaises(TypeError):
            self.calculator.adsolute('string')

        with self.assertRaises(TypeError):
            self.calculator.adsolute('')

    def test_abs_list(self):
        with self.assertRaises(TypeError):
            self.calculator.adsolute([1, 2])

        with self.assertRaises(TypeError):
            self.calculator.adsolute([])

    def test_abs_infinity(self):
        self.assertEqual(self.calculator.adsolute(math.inf), math.inf)
        self.assertEqual(self.calculator.adsolute(-math.inf), math.inf)

    def test_degree(self):
        self.assertEqual(self.calculator.degree(2, 3), 8)
        self.assertAlmostEqual(self.calculator.degree(2.2, 3), 10.648)
        self.assertAlmostEqual(self.calculator.degree(2, 2.2), 4.5947934200)
        self.assertAlmostEqual(self.calculator.degree(2.2, 2.2), 5.6666957788)

    def test_degree_negative(self):
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        self.assertAlmostEqual(self.calculator.degree(2, -2), 0.25)

        self.assertAlmostEqual(
            self.calculator.degree(-1.2, 2.1),
            (1.394719722540787+0.4531719085779955j),
        )
        self.assertAlmostEqual(self.calculator.degree(1.1, -2.2), 0.8108417320)
        self.assertAlmostEqual(
            self.calculator.degree(-1.1, -2.1),
            (0.7785413551720506-0.2529634206272577j),
        )

    def test_degree_zero(self):
        self.assertEqual(self.calculator.degree(0, 3), 0)
        self.assertEqual(self.calculator.degree(2, 0), 1)

        self.assertAlmostEqual(self.calculator.degree(0, 2.2), 0)
        self.assertAlmostEqual(self.calculator.degree(2.2, 0), 1)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.degree(0, -2)
        self.assertEqual(self.calculator.degree(-2, 0), 1)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.degree(0, -2.2)
        self.assertAlmostEqual(self.calculator.degree(-2.2, 0), 1)

        self.assertEqual(self.calculator.degree(0, math.inf), 0)
        self.assertEqual(self.calculator.degree(math.inf, 0), 1)

        self.assertEqual(self.calculator.degree(0, 0), 1)

    def test_degree_string(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('first', 'second')

        with self.assertRaises(TypeError):
            self.calculator.degree('first', '')

        with self.assertRaises(TypeError):
            self.calculator.degree('', 'second')

        with self.assertRaises(TypeError):
            self.calculator.degree('', '')

    def test_degree_list(self):
        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], [])

        with self.assertRaises(TypeError):
            self.calculator.degree([], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.degree([], [])

    def test_degree_different_types_operands(self):
        with self.assertRaises(TypeError):
            self.calculator.degree('string', 2)

        with self.assertRaises(TypeError):
            self.calculator.degree(2, 'string')

        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], 2)

        with self.assertRaises(TypeError):
            self.calculator.degree(2, [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.degree('string', [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.degree([1, 2], 'string')

    def test_degree_infinity(self):
        self.assertEqual(self.calculator.degree(2, math.inf), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, 3), math.inf)
        self.assertEqual(self.calculator.degree(math.inf, math.inf), math.inf)

        self.assertEqual(self.calculator.degree(2, -math.inf), 0)
        self.assertEqual(self.calculator.degree(-math.inf, 2), math.inf)
        self.assertEqual(self.calculator.degree(-math.inf, 3), -math.inf)
        self.assertEqual(self.calculator.degree(-math.inf, -math.inf), 0)

    def test_ln(self):
        self.assertAlmostEqual(self.calculator.ln(10), 2.302585092994046)
        self.assertAlmostEqual(self.calculator.ln(5.5), 1.7047480922384253)
        self.assertEqual(self.calculator.ln(math.e), 1)

    def test_ln_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(-10)

        with self.assertRaises(ValueError):
            self.calculator.ln(-10.2)

    def test_ln_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.ln(0)

    def test_ln_string(self):
        with self.assertRaises(TypeError):
            self.calculator.ln('string')

        with self.assertRaises(TypeError):
            self.calculator.ln('')

    def test_ln_list(self):
        with self.assertRaises(TypeError):
            self.calculator.ln([1, 2])

        with self.assertRaises(TypeError):
            self.calculator.ln([])

    def test_ln_infinity(self):
        self.assertEqual(self.calculator.ln(math.inf), math.inf)

        with self.assertRaises(ValueError):
            self.calculator.ln(-math.inf)

    def test_log(self):
        self.assertAlmostEqual(self.calculator.log(10, 2), 3.3219280948873626)
        self.assertAlmostEqual(self.calculator.log(5.5, 2), 2.4594316186372973)
        self.assertAlmostEqual(self.calculator.log(5, 2.2), 2.041249144646876)
        self.assertAlmostEqual(
            self.calculator.log(5.5, 2.2),
            2.1621309888601017,
        )

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            self.calculator.log(-10, 2)

        with self.assertRaises(ValueError):
            self.calculator.log(10, -2)

        with self.assertRaises(ValueError):
            self.calculator.log(-10, -2)

        with self.assertRaises(ValueError):
            self.calculator.log(-1.2, 2.1)

        with self.assertRaises(ValueError):
            self.calculator.log(1.1, -2.2)

        with self.assertRaises(ValueError):
            self.calculator.log(-1.1, -2.1)

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            self.calculator.log(0, 2)

        with self.assertRaises(ValueError):
            self.calculator.log(2, 0)

        with self.assertRaises(ValueError):
            self.calculator.log(0, 2.2)

        with self.assertRaises(ValueError):
            self.calculator.log(2.2, 0)

        with self.assertRaises(ValueError):
            self.calculator.log(0, -2)

        with self.assertRaises(ValueError):
            self.calculator.log(-2, 0)

        with self.assertRaises(ValueError):
            self.calculator.log(0, -2.2)

        with self.assertRaises(ValueError):
            self.calculator.log(-2.2, 0)

        with self.assertRaises(ValueError):
            self.calculator.log(0, math.inf)

        with self.assertRaises(ValueError):
            self.calculator.log(math.inf, 0)

        with self.assertRaises(ValueError):
            self.calculator.log(0, 0)

    def test_log_string(self):
        with self.assertRaises(TypeError):
            self.calculator.log('first', 'second')

        with self.assertRaises(TypeError):
            self.calculator.log('first', '')

        with self.assertRaises(TypeError):
            self.calculator.log('', 'second')

        with self.assertRaises(TypeError):
            self.calculator.log('', '')

    def test_log_list(self):
        with self.assertRaises(TypeError):
            self.calculator.log([1, 2], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.log([1, 2], [])

        with self.assertRaises(TypeError):
            self.calculator.log([], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.log([], [])

    def test_log_different_types_operands(self):
        with self.assertRaises(TypeError):
            self.calculator.log('string', 2)

        with self.assertRaises(TypeError):
            self.calculator.log(2, 'string')

        with self.assertRaises(TypeError):
            self.calculator.log([1, 2], 2)

        with self.assertRaises(TypeError):
            self.calculator.log(2, [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.log('string', [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.log([1, 2], 'string')

    def test_log_infinity(self):
        self.assertEqual(self.calculator.log(2, math.inf), 0)
        self.assertEqual(self.calculator.log(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.log(math.inf, 3), math.inf)
        self.assertTrue(
            math.isnan(self.calculator.log(math.inf, math.inf)),
        )

        with self.assertRaises(ValueError):
            self.calculator.log(2, -math.inf)

        with self.assertRaises(ValueError):
            self.calculator.log(-math.inf, 2)

        with self.assertRaises(ValueError):
            self.calculator.log(-math.inf, 3)

        with self.assertRaises(ValueError):
            self.calculator.log(-math.inf, -math.inf)

    def test_sqrt(self):
        self.assertEqual(self.calculator.sqrt(4), 2)
        self.assertAlmostEqual(self.calculator.sqrt(8), 2.8284271247)
        self.assertAlmostEqual(self.calculator.sqrt(2.5), 1.5811388301)

    def test_sqrt_negative(self):
        self.assertAlmostEqual(
            self.calculator.sqrt(-2),
            (8.659560562354934e-17+1.4142135623730951j),
        )

        self.assertAlmostEqual(
            self.calculator.sqrt(-2.2),
            (9.082223739063148e-17+1.4832396974191326j),
        )

    def test_sqrt_zero(self):
        self.assertEqual(self.calculator.sqrt(0), 0)

    def test_sqrt_string(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt('string')

        with self.assertRaises(TypeError):
            self.calculator.sqrt('')

    def test_sqrt_list(self):
        with self.assertRaises(TypeError):
            self.calculator.sqrt([1, 2])

        with self.assertRaises(TypeError):
            self.calculator.sqrt([])

    def test_sqrt_infinity(self):
        self.assertEqual(self.calculator.sqrt(math.inf), math.inf)
        self.assertEqual(self.calculator.sqrt(-math.inf), math.inf)

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

        self.assertAlmostEqual(
            self.calculator.nth_root(2.5, 5.1),
            1.1968161822205403,
        )

    def test_nth_root_negative(self):
        self.assertAlmostEqual(
            self.calculator.nth_root(5, -2),
            0.4472135954999579,
        )
        self.assertAlmostEqual(
            self.calculator.nth_root(-5, 2),
            (1.3691967456605067e-16+2.23606797749979j),
        )
        self.assertAlmostEqual(
            self.calculator.nth_root(-5, -2),
            (2.738393491321013e-17-0.4472135954999579j),
        )

        self.assertAlmostEqual(
            self.calculator.nth_root(-1.2, 2.1),
            (0.08150812098075119+1.08765028708426j),
        )
        self.assertAlmostEqual(self.calculator.nth_root(
            1.1, -2.2),
            0.9576022175517517,
        )
        self.assertAlmostEqual(
            self.calculator.nth_root(-1.1, -2.1),
            (0.0714142243692801-0.9529565974842009j),
        )

    def test_nth_root_zero(self):
        self.assertEqual(self.calculator.nth_root(0, 2), 0)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(2, 0)

        self.assertAlmostEqual(self.calculator.nth_root(0, 2.2), 0)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(2.2, 0)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(0, -2)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(-2, 0)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(0, -2.2)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(-2.2, 0)

        self.assertEqual(self.calculator.nth_root(0, math.inf), 1)
        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(math.inf, 0)

        with self.assertRaises(ZeroDivisionError):
            self.calculator.nth_root(0, 0)

    def test_nth_root_string(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('first', 'second')

        with self.assertRaises(TypeError):
            self.calculator.nth_root('first', '')

        with self.assertRaises(TypeError):
            self.calculator.nth_root('', 'second')

        with self.assertRaises(TypeError):
            self.calculator.nth_root('', '')

    def test_nth_root_list(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, 2], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, 2], [])

        with self.assertRaises(TypeError):
            self.calculator.nth_root([], [3, 4])

        with self.assertRaises(TypeError):
            self.calculator.nth_root([], [])

    def test_nth_root_different_types_operands(self):
        with self.assertRaises(TypeError):
            self.calculator.nth_root('string', 2)

        with self.assertRaises(TypeError):
            self.calculator.nth_root(2, 'string')

        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, 2], 2)

        with self.assertRaises(TypeError):
            self.calculator.nth_root(2, [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.nth_root('string', [1, 2])

        with self.assertRaises(TypeError):
            self.calculator.nth_root([1, 2], 'string')

    def test_nth_root_infinity(self):
        self.assertEqual(self.calculator.nth_root(2, math.inf), 1)
        self.assertEqual(self.calculator.nth_root(math.inf, 2), math.inf)
        self.assertEqual(self.calculator.nth_root(math.inf, 3), math.inf)
        self.assertEqual(self.calculator.nth_root(math.inf, math.inf), 1)

        with self.assertRaises(ValueError):
            self.calculator.log(2, -math.inf)

        with self.assertRaises(ValueError):
            self.calculator.log(-math.inf, 2)

        with self.assertRaises(ValueError):
            self.calculator.log(-math.inf, 3)

        with self.assertRaises(ValueError):
            self.calculator.log(-math.inf, -math.inf)


if __name__ == "__main__":
    unittest.main()
