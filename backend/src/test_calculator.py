import unittest
from calculator import Calculator
import math


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        testCases  = [
            {"a": 1, "b": 2, "result": 3},
            {"a": 2, "b": 5, "result": 7},
            {"a": 4, "b": 3, "result": 7},
            {"a": -2, "b": 7, "result": 5},
            {"a": -1, "b": -54, "result": -55},
            {"a": 2, "b": 0, "result": 2},
        ]
        for tc in testCases:
            self.assertEqual(self.calculator.addition(tc["a"], tc["b"]), tc["result"])

    def test_multiplication(self):
        testCases  = [
            {"a": 1, "b": 2, "result": 2},
            {"a": 2, "b": 5, "result": 10},
            {"a": 4, "b": 3, "result": 12},
            {"a": -2, "b": 7, "result": -14},
            {"a": -1, "b": -54, "result": 54},
            {"a": 2, "b": 0, "result": 0},
        ]
        for tc in testCases:
            self.assertEqual(self.calculator.multiplication(tc["a"], tc["b"]), tc["result"])
        
    def test_subtraction(self):
        testCases  = [
            {"a": 1, "b": 2, "result": -1},
            {"a": 2, "b": 5, "result": -3},
            {"a": 4, "b": 3, "result": 1},
            {"a": -2, "b": 7, "result": -9},
            {"a": -1, "b": -54, "result": 53},
            {"a": 2, "b": 0, "result": 2},
        ]
        for tc in testCases:
            self.assertEqual(self.calculator.subtraction(tc["a"], tc["b"]), tc["result"])
    
    def test_division(self):
        testCases  = [
            {"a": 1, "b": 2, "result": 0.5},
            {"a": 2, "b": 5, "result": 0.4},
            {"a": 25, "b": 5, "result": 5},
            {"a": 21, "b": 7, "result": 3},
            {"a": 20, "b": 1, "result": 20},
            {"a": 2, "b": 0, "result": None},
        ]
        for tc in testCases:
            self.assertEqual(self.calculator.division(tc["a"], tc["b"]), tc["result"])
    
    def test_adsolute(self):
        testCases  = [
            {"a": 1, "result": 1},
            {"a": 2, "result": 2},
            {"a": 4, "result": 4},
            {"a": -2, "result": 2},
            {"a": -167, "result": 167},
            {"a": 0,"result": 0},
        ]
        for tc in testCases:
            self.assertEqual(self.calculator.adsolute(tc["a"]), tc["result"])
    
    def test_degree(self):
        testCases  = [
            {"a": 1, "n": 2, "result": 1},
            {"a": 2, "n": 5, "result": 32},
            {"a": 4, "n": 5, "result": 1024},
            {"a": 21, "n": 0, "result": 1},
            {"a": 20, "n": 1, "result": 20},
            {"a": 2, "n": -1, "result": 0.5},
        ]
        for tc in testCases:
            self.assertEqual(self.calculator.degree(tc["a"], tc["n"]), tc["result"])

    def test_ln(self):
        testCases = [
            {"x": 1, "result": 0.0},
            {"x": math.e, "result": 1.0},
            {"x": 10, "result": math.log(10)},
        ]
        for tc in testCases:
            self.assertAlmostEqual(self.calculator.ln(tc["x"]), tc["result"])
    
    def test_log(self):
        testCases = [
            {"x": 100, "n": 10, "result": 2},
            {"x": 8, "n": 2, "result": 3},
            # Add more test cases as needed
        ]
        for tc in testCases:
            self.assertAlmostEqual(self.calculator.log(tc["x"], tc["n"]), tc["result"])

    def test_sqrt(self):
        testCases = [
            {"x": 4, "result": 2},
            {"x": 9, "result": 3},
            {"x": 25, "result": 5},
        ]
        for tc in testCases:
            self.assertAlmostEqual(self.calculator.sqrt(tc["x"]), tc["result"])

    def test_nth_root(self):
        testCases = [
            {"x": 8, "n": 3, "result": 2},
            {"x": 27, "n": 3, "result": 3},
        ]
        for tc in testCases:
            self.assertAlmostEqual(self.calculator.nth_root(tc["x"], tc["n"]), tc["result"])
    

if __name__ == "__main__":
    unittest.main()
