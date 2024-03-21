import unittest
from src.calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        # Целочисленные положительные аргументы
        self.assertEqual(self.calculator.addition(1, 2), 3)
        # Целое число и строка
        self.assertRaises(TypeError, self.calculator.addition, 1, "a")
        # Целое число и словарь
        self.assertRaises(TypeError, self.calculator.addition, 1, {"foo":"bar"})
        # Целое число и None
        self.assertRaises(TypeError, self.calculator.addition, 1, None)
        # Целое число и массив
        self.assertRaises(TypeError, self.calculator.addition, 1, ["foo","bar"])
        # Строки
        self.assertEqual(self.calculator.addition("1", "2"), "12")
        # Положительное и отрицательные числа
        self.assertEqual(self.calculator.addition(-1, 1), 0)
        # Ноль как одно из слагаемых
        self.assertEqual(self.calculator.addition(1, 0), 1)
        # Дробные числа
        self.assertEqual(self.calculator.addition(1.1, 1.2), 2.3)

    def test_mult(self):
        # Целые числа
        self.assertEqual(self.calculator.multiplication(1, 2), 2)
        # Число и строка
        self.assertEqual(self.calculator.multiplication(2, "a"), "aa")
        # Число и словарь
        self.assertRaises(TypeError, self.calculator.multiplication, 1, {"foo":"bar"})
        # Число и Nonne
        self.assertRaises(TypeError, self.calculator.multiplication, 1, None)
        # Число и список
        self.assertEqual(self.calculator.multiplication(2, ["foo","bar"]), ["foo","bar", "foo","bar"])
        # Положительное и отрицательное число
        self.assertEqual(self.calculator.multiplication(-1, 2), -2)
        # Два отрицательных числа
        self.assertEqual(self.calculator.multiplication(-1, -1), 1)
        # Умножение на ноль
        self.assertEqual(self.calculator.multiplication(1, 0), 0)
        # Дробные числа
        self.assertEqual(self.calculator.multiplication(1.1, 1.2), 1.32)

    def test_sub(self):
        # Целочисленные положительные аргументы, положительный результат
        self.assertEqual(self.calculator.subtraction(2, 1), 1)
        # Целое число и строка
        self.assertRaises(TypeError, self.calculator.subtraction, 1, "a")
        # Целое число и словарь
        self.assertRaises(TypeError, self.calculator.subtraction, 1, {"foo":"bar"})
        # Целое число и None
        self.assertRaises(TypeError, self.calculator.subtraction, 1, None)
        # Целое число и массив
        self.assertRaises(TypeError, self.calculator.subtraction, 1, ["foo","bar"])
        # Целочисленные положительные аргументы, отрицательный результат
        self.assertEqual(self.calculator.subtraction(1, 2), -1)
        # Целочисленные положительный и отрицательный аргументы, положительный результат
        self.assertEqual(self.calculator.subtraction(1, -1), 2)
        # Целочисленные положительный и отрицательный аргументы, отрицательный результат
        self.assertEqual(self.calculator.subtraction(-1, 1), -2)
        # Вычитание нуля
        self.assertEqual(self.calculator.subtraction(1, 0), 1)
        # Погрешность из-за представления дробных чисел
        self.assertAlmostEqual(self.calculator.subtraction(1.1, 1.2), -0.1)

    def test_div(self):
        # Деление на 0
        self.assertIsNone(self.calculator.division(1, 0), 0)
        # Деление 0
        self.assertEqual(self.calculator.division(0, 1), 0)
        # Целое число и строка
        self.assertRaises(TypeError, self.calculator.division, 1, "a")
        # Целое число и словарь
        self.assertRaises(TypeError, self.calculator.division, 1, {"foo":"bar"})
        # Целое число и None
        self.assertRaises(TypeError, self.calculator.division, 1, None)
        # Целое число и массив
        self.assertRaises(TypeError, self.calculator.division, 1, ["foo","bar"])
        # Целочисленные аргументы и результат
        self.assertEqual(self.calculator.division(2, 2), 1)
        # Целочисленные аргументы, дробный результат
        self.assertEqual(self.calculator.division(1, 2), 0.5)
        # Целочисленные аргументы, иррациональный результат
        self.assertAlmostEqual(self.calculator.division(1, 3), 0.333, 3)
        # Целое делимое, дробный делитель
        self.assertEqual(self.calculator.division(1, 0.5), 2)
        # Дробное делимое, дробный делитель
        self.assertEqual(self.calculator.division(0.25, 0.5), 0.5)
        # Дробное делимое, целый делитель
        self.assertEqual(self.calculator.division(0.5, 2), 0.25)
        # Отрицательный аргумент
        self.assertEqual(self.calculator.division(1, -1), -1)

    def test_abs(self):
        # Модуль отрицательного числа положителен
        self.assertEqual(self.calculator.adsolute(-1), 1)
        # Модуль положительного числа положителен
        self.assertEqual(self.calculator.adsolute(1), 1)

    def test_deg(self):
        # Целое число и строка
        self.assertRaises(TypeError, self.calculator.degree, 1, "a")
        # Целое число и словарь
        self.assertRaises(TypeError, self.calculator.degree, 1, {"foo":"bar"})
        # Целое число и None
        self.assertRaises(TypeError, self.calculator.degree, 1, None)
        # Целое число и массив
        self.assertRaises(TypeError, self.calculator.degree, 1, ["foo","bar"])
        # Единица в степени, не равное единице
        self.assertEqual(self.calculator.degree(1, 2), 1)
        # Не равное единице число в первой степени
        self.assertEqual(self.calculator.degree(2, 1), 2)
        # Число в 0 степени
        self.assertEqual(self.calculator.degree(2, 0), 1)
        # Число в отрицательной степени
        self.assertEqual(self.calculator.degree(2, -1), 0.5)
        # Отрицательное число в чётной степени
        self.assertEqual(self.calculator.degree(-2, 2), 4)
        # Отрицательное число в нечётной степени
        self.assertEqual(self.calculator.degree(-2, 3), -8)
        # Целое число в дробной степени
        self.assertEqual(self.calculator.degree(4, 0.5), 2)
        # Дробное число в дробной степени
        self.assertEqual(self.calculator.degree(0.25, 0.5), 0.5)
        # 0^0
        self.assertEqual(self.calculator.degree(0, 0), 1)


    def test_ln(self):
        # Натуральный логарифм единицы
        self.assertEqual(self.calculator.ln(1), 0)
        # Натуральный логарифм строки
        self.assertRaises(TypeError, self.calculator.ln, "a")
        # Натуральный логарифм словаря
        self.assertRaises(TypeError, self.calculator.ln, {"foo":"bar"})
        # Натуральный логарифм None
        self.assertRaises(TypeError, self.calculator.ln, None)
        # Натуральный логарифм массива
        self.assertRaises(TypeError, self.calculator.ln, ["foo","bar"])
        # Натуральный логарифм e
        self.assertEqual(self.calculator.ln(math.e), 1)
        # Натуральный логарифм отрицательного числа
        self.assertRaises(ValueError, self.calculator.ln, -1)
        # Натуральный логарифм 0
        self.assertRaises(ValueError, self.calculator.ln, 0)
        # Натуральный логарифм e в положительной степени
        self.assertEqual(self.calculator.ln(math.e ** 2), 2)

    def test_log(self):
        # Логарифм 1
        self.assertEqual(self.calculator.log(1, 2), 0)
        # Логарифм по основанию 1
        self.assertRaises(ZeroDivisionError, self.calculator.log, 1, 1)
        # Логарифм по основанию 0
        self.assertRaises(ValueError, self.calculator.log, 0, 2)
        # Логарифм 0
        self.assertRaises(ValueError, self.calculator.log, 2, 0)
        # Целое число и строка
        self.assertRaises(TypeError, self.calculator.log, 1, "a")
        # Целое число и словарь
        self.assertRaises(TypeError, self.calculator.log, 1, {"foo":"bar"})
        # Целое число и None
        self.assertRaises(TypeError, self.calculator.log, 1, None)
        # Целое число и массив
        self.assertRaises(TypeError, self.calculator.log, 1, ["foo","bar"])
        # Логарифм с отрицательным основанием
        self.assertRaises(ValueError, self.calculator.log, -1, 2)
        # Логарифм отрицательного значения
        self.assertRaises(ValueError, self.calculator.log, 2, -1)
        # Логарифм целого положительного числа по целому положительному основанию
        self.assertEqual(self.calculator.log(4, 2), 2)
        # Логарифм с дробным основанием и аргументом
        self.assertEqual(self.calculator.log(6.25, 2.5), 2)
        # Логарифм основание > аргумент
        self.assertEqual(self.calculator.log(2, 4), 0.5)
        # Логарифм дробного числа
        self.assertEqual(self.calculator.log(0.5, 2), -1)

    def test_sqrt(self):
        # Квадратный корень целого положительного числа
        self.assertEqual(self.calculator.sqrt(4), 2)
        # Целое число и строка
        self.assertRaises(TypeError, self.calculator.sqrt, 1, "a")
        # Целое число и словарь
        self.assertRaises(TypeError, self.calculator.sqrt, 1, {"foo":"bar"})
        # Целое число и None
        self.assertRaises(TypeError, self.calculator.sqrt, 1, None)
        # Целое число и массив
        self.assertRaises(TypeError, self.calculator.sqrt, 1, ["foo","bar"])
        # Квадратный корень дробного числа > 1
        self.assertEqual(self.calculator.sqrt(6.25), 2.5)
        # Квадратный корень дробного числа < 1
        self.assertEqual(self.calculator.sqrt(0.25), 0.5)
        # Квадратный корень дробного числа < 0
        self.assertIsInstance(self.calculator.sqrt(-1), complex)
        # Комплексная часть корня из отрицательного числа
        self.assertEqual(self.calculator.sqrt(-1).imag, 1)
    
    def test_nroot(self):
        # Корень n степени целого положительного числа
        self.assertEqual(self.calculator.nth_root(8, 3), 2)
        # Целое число и строка
        self.assertRaises(TypeError, self.calculator.nth_root, 1, "a")
        # Целое число и словарь
        self.assertRaises(TypeError, self.calculator.nth_root, 1, {"foo":"bar"})
        # Целое число и None
        self.assertRaises(TypeError, self.calculator.nth_root, 1, None)
        # Целое число и массив
        self.assertRaises(TypeError, self.calculator.nth_root, 1, ["foo","bar"])
        # Корень степени 1
        self.assertEqual(self.calculator.nth_root(4, 1), 4)
        # Корень 0 степени
        self.assertRaises(ZeroDivisionError, self.calculator.nth_root, 4, 0)
        # Корень отрицательной степени целого числа
        self.assertEqual(self.calculator.nth_root(2, -1), 0.5)
        # Корень отрицательной степени дробного числа
        self.assertEqual(self.calculator.nth_root(6.25, -1), 0.16)


if __name__ == "__main__":
    unittest.main()
