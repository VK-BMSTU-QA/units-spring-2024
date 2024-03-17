import unittest
from src.calculator import Calculator
import math



class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        testCases  = [
            {"test_name": "test_positive_1", "a": 1,         "b": 2,        "result": 3},
            {"test_name": "test_positive_2", "a": 2,         "b": 5,        "result": 7},
            {"test_name": "test_positive_3", "a": 4,         "b": 3,        "result": 7},
            {"test_name": "test_negative_1", "a": -2,        "b": 7,        "result": 5},
            {"test_name": "test_negative_2", "a": -1,        "b": -54,      "result": -55},
            {"test_name": "test_zero_1",     "a": 2,         "b": 0,        "result": 2},
            {"test_name": "test_zero_2",     "a": 0,         "b": 0,        "result": 0},
            {"test_name": "test_inf_1",      "a": 0,         "b": math.inf, "result": math.inf},
            {"test_name": "test_inf_2",      "a": math.inf,  "b": math.inf, "result": math.inf},
            {"test_name": "test_complex_1",  "a": 1+2j,      "b": 3+4j,     "result": 4+6j}
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                result = self.calculator.addition(tc["a"], tc["b"])
                self.assertEqual(
                    result, 
                    tc["result"],
                    f'{tc["test_name"]} failed: {tc["a"]} + {tc["b"]} != {tc["result"]}, got {result}'
                )
    
    def test_add_types(self):
        testCases  = [
            {"test_name": "test_array",     "a": [1, 3, 5],     "b": [7, 8, 9],     "result": [1, 3, 5, 7, 8, 9]},
            {"test_name": "test_string",    "a": "Hello, ",     "b": "world!",      "result": "Hello, world!"},
            {"test_name": "test_dict",      "a": {"dict": 18},  "b": {"dict": 43},  "exeception": TypeError},
            {"test_name": "test_bool_1",    "a": True,          "b": False,         "result": True},
            {"test_name": "test_bool_2",    "a": False,         "b": False,         "result": False},
            {"test_name": "test_tuple",     "a": (1, 2),        "b": (3, 4),        "result": (1, 2, 3, 4)},
            {"test_name": "test_set",       "a": {1, 2},        "b": {3, 4},        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.addition(tc["a"], tc["b"])
                else:
                    result = self.calculator.addition(tc["a"], tc["b"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["a"]} + {tc["b"]} != {tc["result"]}, got {result}'
                    )

    def test_multiplication(self):
        testCases  = [
            {"test_name": "test_positive_1",    "a": 1,         "b": 2,         "result": 2},
            {"test_name": "test_positive_2",    "a": 2,         "b": 5,         "result": 10},
            {"test_name": "test_positive_3",    "a": 4,         "b": 3,         "result": 12},
            {"test_name": "test_negative_1",    "a": -2,        "b": 7,         "result": -14},
            {"test_name": "test_negative_2",    "a": -1,        "b": -54,       "result": 54},
            {"test_name": "test_zero_1",        "a": 2,         "b": 0,         "result": 0},
            {"test_name": "test_zero_2",        "a": 0,         "b": 0,         "result": 0},
            {"test_name": "test_zero_3",        "a": -1,        "b": 0,         "result": 0},
            {"test_name": "test_inf_1",         "a": math.inf,  "b": 3,         "result": math.inf},
            {"test_name": "test_inf_2",         "a": math.inf,  "b": math.inf,  "result": math.inf},
            {"test_name": "test_complex_1",     "a": 1+2j,      "b": 3+4j,      "result": -5+10j},
            {"test_name": "test_float",         "a": 0.1,       "b": 0.2,       "result": 0.02},
            {"test_name": "test_large",         "a": 1e308,     "b": 1e308,     "result": math.inf},
            {"test_name": "test_small",         "a": 1e-308,    "b": 1e-308,    "result": 0.0},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                result = self.calculator.multiplication(tc["a"], tc["b"])
                if isinstance(tc["result"], float):
                    self.assertAlmostEqual(
                        result, 
                        tc["result"], 
                        places=7, 
                        msg=f'{tc["test_name"]} failed: {tc["a"]} * {tc["b"]} != {tc["result"]}, got {result}'
                    )
                else:
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["a"]} * {tc["b"]} != {tc["result"]}, got {result}'
                    )
    
    def test_multiplication_types(self):
        testCases  = [
            {"test_name": "test_array",     "a": [1, 3, 5],     "b": [7, 8, 9],     "exeception": TypeError},
            {"test_name": "test_string_1",  "a": "Hello, ",     "b": "world!",      "exeception": TypeError},
            {"test_name": "test_string_2",  "a": "str",         "b": 5,             "result": "strstrstrstrstr"},
            {"test_name": "test_dict",      "a": {"dict": 18},  "b": {"dict": 43},  "exeception": TypeError},
            {"test_name": "test_bool_1",    "a": True,          "b": False,         "result": False},
            {"test_name": "test_bool_2",    "a": False,         "b": False,         "result": False},
            {"test_name": "test_tuple_1",   "a": (1, 2),        "b": (3, 4),        "exeception": TypeError},
            {"test_name": "test_tuple_2",   "a": (1, 2),        "b": 2,             "result": (1, 2, 1, 2)},
            {"test_name": "test_set",       "a": {1, 2},        "b": {3, 4},        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.multiplication(tc["a"], tc["b"])
                else:
                    result = self.calculator.multiplication(tc["a"], tc["b"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["a"]} * {tc["b"]} != {tc["result"]}, got {result}'
                    )
        
    def test_subtraction(self):
        testCases  = [
            {"test_name": "test_positive_1", "a": 1,               "b": 2,             "result": -1},
            {"test_name": "test_positive_2", "a": 2,               "b": 5,             "result": -3},
            {"test_name": "test_positive_3", "a": 4,               "b": 3,             "result": 1},
            {"test_name": "test_negative_1", "a": -2,              "b": 7,             "result": -9},
            {"test_name": "test_negative_2", "a": -1,              "b": -54,           "result": 53},
            {"test_name": "test_zero_1",     "a": 2,               "b": 0,             "result": 2},
            {"test_name": "test_zero_2",     "a": 0,               "b": 0,             "result": 0},
            {"test_name": "test_complex_1",  "a": complex(1, 2),   "b": complex(2, 3), "result": complex(-1, -1)},
            {"test_name": "test_complex_2",  "a": complex(10, -5), "b": complex(3, 7), "result": complex(7, -12)},
            {"test_name": "test_inf_1",      "a": math.inf,        "b": 100,           "result": math.inf},
            {"test_name": "test_inf_2",      "a": 0,               "b": math.inf,      "result": -math.inf},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                result = self.calculator.subtraction(tc["a"], tc["b"])
                self.assertEqual(
                    result, 
                    tc["result"], 
                    f'{tc["test_name"]} failed: {tc["a"]} - {tc["b"]} != {tc["result"]}, got {result}'
                )
    
    def test_subtraction_types(self):
        testCases  = [
            {"test_name": "test_array",     "a": [1, 3, 5],     "b": [7, 8, 9],     "exeception": TypeError},
            {"test_name": "test_string_1",  "a": "Hello, ",     "b": "world!",      "exeception": TypeError},
            {"test_name": "test_string_2",  "a": "Nicola",      "b": 2,             "exeception": TypeError},
            {"test_name": "test_dict",      "a": {"dict": 18},  "b": {"dict": 43},  "exeception": TypeError},
            {"test_name": "test_bool_1",    "a": True,          "b": False,         "result": True},
            {"test_name": "test_bool_2",    "a": True,          "b": True,          "result": False},
            {"test_name": "test_tuple",     "a": (1, 2),        "b": (3, 4),        "exeception": TypeError},
            {"test_name": "test_set",       "a": {1, 2},        "b": {1, 4},        "result": {2}},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.subtraction(tc["a"], tc["b"])
                else:
                    result = self.calculator.subtraction(tc["a"], tc["b"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["a"]} - {tc["b"]} != {tc["result"]}, got {result}'
                    )
    
    def test_division(self):
        testCases  = [
            {"test_name": "test_positive_1", "a": 1,        "b": 2,            "result": 0.5},
            {"test_name": "test_positive_2", "a": 2,        "b": 5,            "result": 0.4},
            {"test_name": "test_positive_3", "a": 25,       "b": 5,            "result": 5},
            {"test_name": "test_negative_1", "a": -21,      "b": 7,            "result": -3},
            {"test_name": "test_negative_2", "a": -20,      "b": -1,           "result": 20},
            {"test_name": "test_zero_1",     "a": 2,        "b": 0,            "result": None},
            {"test_name": "test_zero_1",     "a": 0,        "b": 100,          "result": 0},
            {"test_name": "test_float_1",    "a": 0.5,      "b": 0.2,          "result": 2.5},
            {"test_name": "test_float_2",    "a": -3.5,     "b": 0.5,          "result": -7},
            {"test_name": "test_float_3",    "a": 1.2,      "b": 0.4,          "result": 3.},
            {"test_name": "test_inf_1",      "a": math.inf, "b": 2,            "result": math.inf},
            {"test_name": "test_inf_2",      "a": 1,        "b": math.inf,     "result": 0.},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                result = self.calculator.division(tc["a"], tc["b"])
                if isinstance(tc["result"], float):
                    self.assertAlmostEqual(
                        result, 
                        tc["result"], 
                        places=7, 
                        msg=f'{tc["test_name"]} failed: {tc["a"]} / {tc["b"]} != {tc["result"]}, got {result}'
                    )
                else:
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["a"]} / {tc["b"]} != {tc["result"]}, got {result}'
                    )
    
    def test_division_types(self):
        testCases  = [
            {"test_name": "test_array",     "a": [1, 3, 5],     "b": [7, 8, 9],     "exeception": TypeError},
            {"test_name": "test_string_1",  "a": "Hello, ",     "b": "world!",      "exeception": TypeError},
            {"test_name": "test_string_2",  "a": "Nicola",      "b": 2,             "exeception": TypeError},
            {"test_name": "test_dict",      "a": {"dict": 18},  "b": {"dict": 43},  "exeception": TypeError},
            {"test_name": "test_bool_1",    "a": True,          "b": False,         "result": None},
            {"test_name": "test_bool_2",    "a": True,          "b": True,          "result": True},
            {"test_name": "test_tuple",     "a": (1, 2),        "b": (3, 4),        "exeception": TypeError},
            {"test_name": "test_set",       "a": {1, 2},        "b": {1, 4},        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.division(tc["a"], tc["b"])
                else:
                    result = self.calculator.division(tc["a"], tc["b"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["a"]} / {tc["b"]} != {tc["result"]}, got {result}'
                    )
    
    def test_adsolute(self):
        testCases  = [
            {"test_name": "test_positive_1", "a": 1,     "result": 1},
            {"test_name": "test_positive_2", "a": 2,     "result": 2},
            {"test_name": "test_positive_3", "a": 4,     "result": 4},
            {"test_name": "test_negative_1", "a": -2,    "result": 2},
            {"test_name": "test_negative_2", "a": -167,  "result": 167},
            {"test_name": "test_zero",       "a": 0,     "result": 0},
            {"test_name": "test_float_1",    "a": -3.14, "result": 3.14},
            {"test_name": "test_float_2",    "a": 3.45,  "result": 3.45},
            {"test_name": "test_complex_1",  "a": 3+4j,  "result": 5},
            {"test_name": "test_complex_2",  "a": -2-2j, "result": 2.8284271247461903}
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                result = self.calculator.adsolute(tc["a"])
                self.assertEqual(
                    result, 
                    tc["result"], 
                    f'{tc["test_name"]} failed: |{tc["a"]}| != {tc["result"]}, got {result}'
                )
    
    def test_adsolute_types(self):
        testCases  = [
            {"test_name": "test_array",     "a": [1, 3, 5],     "exeception": TypeError},
            {"test_name": "test_string_1",  "a": "Hello, ",     "exeception": TypeError},
            {"test_name": "test_string_2",  "a": "Nicola",      "exeception": TypeError},
            {"test_name": "test_dict",      "a": {"dict": 18},  "exeception": TypeError},
            {"test_name": "test_bool_1",    "a": False,         "result": False},
            {"test_name": "test_bool_2",    "a": True,          "result": True},
            {"test_name": "test_tuple",     "a": (1, 2),        "exeception": TypeError},
            {"test_name": "test_set",       "a": {1, 2},        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.adsolute(tc["a"])
                else:
                    result = self.calculator.adsolute(tc["a"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: |{tc["a"]}| != {tc["result"]}, got {result}'
                    )
    
    def test_degree(self):
        testCases  = [
            {"test_name": "test_positive_1", "a": 1,   "n": 2,  "result": 1},
            {"test_name": "test_positive_2", "a": 2,   "n": 5,  "result": 32},
            {"test_name": "test_positive_3", "a": 4,   "n": 5,  "result": 1024},
            {"test_name": "test_zero_1",     "a": 21,  "n": 0,  "result": 1},
            {"test_name": "test_zero_2",     "a": 0,   "n": 0,  "result": 1},
            {"test_name": "test_zero_2",     "a": 0,   "n": 4,  "result": 0},
            {"test_name": "test_one",        "a": 20,  "n": 1,  "result": 20},
            {"test_name": "test_negative_1", "a": 2,   "n": -1, "result": 0.5},
            {"test_name": "test_float",      "a": 1.5, "n": 2,  "result": 2.25},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                result = self.calculator.degree(tc["a"], tc["n"])
                self.assertEqual(
                    result, 
                    tc["result"], 
                    f'{tc["test_name"]} failed: {tc["a"]} ^{tc["n"]} != {tc["result"]}, got {result}'
                )
    
    def test_degree_types(self):
        testCases  = [
            {"test_name": "test_array_1",     "a": [1, 3, 5],       "n": [1, 2],  "exeception": TypeError},
            {"test_name": "test_array_2",     "a": [1, 3, 5],       "n": 2,       "exeception": TypeError},
            {"test_name": "test_string_1",    "a": "Hello, ",       "n":"world!", "exeception": TypeError},
            {"test_name": "test_string_2",    "a": "Nicola",        "n":1,        "exeception": TypeError},
            {"test_name": "test_dict",        "a": {"dict": 18},    "n":5,        "exeception": TypeError},
            {"test_name": "test_bool_1",      "a": False,           "n":True,     "result": False},
            {"test_name": "test_bool_2",      "a": True,            "n":False,    "result": True},
            {"test_name": "test_tuple",       "a": (1, 2),          "n":2,        "exeception": TypeError},
            {"test_name": "test_set",         "a": {1, 2},          "n":6,        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.degree(tc["a"], tc["n"])
                else:
                    result = self.calculator.degree(tc["a"], tc["n"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["a"]} ^{tc["n"]} != {tc["result"]}, got {result}'
                    )

    def test_ln(self):
        testCases = [
            {"test_name": "test_positive_1", "x": 1,                "result": 0.0},
            {"test_name": "test_positive_2", "x": 10,               "result": math.log(10)},
            {"test_name": "test_exp",        "x": math.e,           "result": 1.0},
            {"test_name": "test_float_1",    "x": 0.5,              "result": math.log(0.5)},
            {"test_name": "test_float_2",    "x": 2.5,              "result": math.log(2.5)},
            {"test_name": "test_infinite_1", "x": float('inf'),     "result": float('inf')},
            {"test_name": "test_infinite_2", "x": float('-inf'),    "exeception": ValueError},
            {"test_name": "test_zero",       "x": 0,                "exeception": ValueError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.ln(tc["x"])
                else:
                    result = self.calculator.ln(tc["x"])
                    self.assertAlmostEqual(
                        result, 
                        tc["result"], 
                        places=7, 
                        msg=f'{tc["test_name"]} failed: ln({tc["x"]}) != {tc["result"]}, got {result}'
                    )
    
    def test_ln_types(self):
        testCases  = [
            {"test_name": "test_array",     "x": [1, 3, 5],     "exeception": TypeError},
            {"test_name": "test_string_1",  "x": "Hello, ",     "exeception": TypeError},
            {"test_name": "test_string_2",  "x": "Nicola",      "exeception": TypeError},
            {"test_name": "test_dict",      "x": {"dict": 18},  "exeception": TypeError},
            {"test_name": "test_bool_1",    "x": False,         "exeception": ValueError},
            {"test_name": "test_bool_2",    "x": True,          "result": False},
            {"test_name": "test_tuple",     "x": (1, 2),        "exeception": TypeError},
            {"test_name": "test_set",       "x": {1, 2},        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.ln(tc["x"])
                else:
                    result = self.calculator.ln(tc["x"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: ln({tc["x"]}) != {tc["result"]}, got {result}'
                    )
    
    def test_log(self):
        testCases = [
            {"test_name": "test_positive_1",    "x": 100,           "n": 10, "result": 2},
            {"test_name": "test_positive_2",    "x": 8,             "n": 2,  "result": 3},
            {"test_name": "test_float_1",       "x": 0.5,           "n": 2,  "result": -1.},
            {"test_name": "test_float_2",       "x": 3.14159,       "n": 2,  "result": 1.651494910},
            {"test_name": "test_zero_1",        "x": 1,             "n": 0,  "exeception": ValueError},
            {"test_name": "test_zero_2",        "x": 0,             "n": 2,  "exeception": ValueError},
            {"test_name": "test_negative",      "x": -1,            "n": 10, "exeception": ValueError},
            {"test_name": "test_infinity",      "x": float('inf'),  "n": 10, "result": float('inf')},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                    if "exeception" in tc:
                        with self.assertRaises(tc["exeception"]):
                            self.calculator.log(tc["x"], tc["n"])
                    else:
                        result = self.calculator.log(tc["x"], tc["n"])
                        self.assertAlmostEqual(
                            result, 
                            tc["result"], 
                            places=7, 
                            msg=f'{tc["test_name"]} failed: log{tc["n"]}({tc["x"]}) != {tc["result"]}, got {result}'
                        )
    

    def test_log_types(self):
        testCases  = [
            {"test_name": "test_array_1",     "x": [1, 3, 5],       "n": [1, 2],  "exeception": TypeError},
            {"test_name": "test_array_2",     "x": [1, 3, 5],       "n": 2,       "exeception": TypeError},
            {"test_name": "test_string_1",    "x": "Hello, ",       "n":"world!", "exeception": TypeError},
            {"test_name": "test_string_2",    "x": "Nicola",        "n":1,        "exeception": TypeError},
            {"test_name": "test_dict",        "x": {"dict": 18},    "n":5,        "exeception": TypeError},
            {"test_name": "test_bool_1",      "x": True,            "n":True,     "exeception": ZeroDivisionError},
            {"test_name": "test_bool_2",      "x": True,            "n":False,    "exeception": ValueError},
            {"test_name": "test_tuple",       "x": (1, 2),          "n":2,        "exeception": TypeError},
            {"test_name": "test_set",         "x": {1, 2},          "n":6,        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.log(tc["x"], tc["n"])
                else:
                    result = self.calculator.log(tc["x"], tc["n"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: log{tc["n"]}({tc["x"]}) != {tc["result"]}, got {result}'
                    )

    def test_sqrt(self):
        testCases = [
            {"test_name": "test_positive_1",    "x": 4,         "result": 2},
            {"test_name": "test_positive_2",    "x": 9,         "result": 3},
            {"test_name": "test_positive_3",    "x": 25,        "result": 5},
            {"test_name": "test_negative_1",    "x": -1,        "result": 0+1j},
            {"test_name": "test_negative_2",    "x": -25,       "result": 0+5j},
            {"test_name": "test_float_1",       "x": 2.25,      "result": 1.5},
            {"test_name": "test_float_2",       "x": 8.64,      "result": 2.93938769133},
            {"test_name": "test_inf",           "x": math.inf,  "result": math.inf},
            {"test_name": "test_zero",          "x": 0,         "result": 0},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.sqrt(tc["x"])
                else:
                    result = self.calculator.sqrt(tc["x"])
                    self.assertAlmostEqual(
                        result, 
                        tc["result"], 
                        places=7, 
                        msg=f'{tc["test_name"]} failed: √{tc["x"]} != {tc["result"]}, got {result}'
                    )
    

    def test_sqrt_types(self):
        testCases  = [
            {"test_name": "test_array",     "x": [1, 3, 5],     "exeception": TypeError},
            {"test_name": "test_string_1",  "x": "Hello, ",     "exeception": TypeError},
            {"test_name": "test_string_2",  "x": "Nicola",      "exeception": TypeError},
            {"test_name": "test_dict",      "x": {"dict": 18},  "exeception": TypeError},
            {"test_name": "test_bool_1",    "x": False,         "result": False},
            {"test_name": "test_bool_2",    "x": True,          "result": True},
            {"test_name": "test_tuple",     "x": (1, 2),        "exeception": TypeError},
            {"test_name": "test_set",       "x": {1, 2},        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.sqrt(tc["x"])
                else:
                    result = self.calculator.sqrt(tc["x"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: √({tc["x"]}) != {tc["result"]}, got {result}'
                    )

    def test_nth_root(self):
        testCases = [
            {"test_name": "test_positive_1",        "x": 8,         "n": 3, "result": 2},
            {"test_name": "test_positive_2",        "x": 27,        "n": 3, "result": 3},
            {"test_name": "test_float_1",           "x": 16.0,      "n": 4, "result": 2.0},
            {"test_name": "test_float_2",           "x": 81.0,      "n": 4, "result": 3.0},
            {"test_name": "test_inf_1",             "x": math.inf,  "n": 3, "result": math.inf},
            {"test_name": "test_inf_2",             "x": math.inf,  "n": 2, "result": math.inf},
            {"test_name": "test_zero_1",            "x": 0,         "n": 3, "result": 0},
            {"test_name": "test_zero_2",            "x": 0,         "n": 2, "result": 0},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                    if "exeception" in tc:
                        with self.assertRaises(tc["exeception"]):
                            self.calculator.nth_root(tc["x"], tc["n"])
                    else:
                        result = self.calculator.nth_root(tc["x"], tc["n"])
                        self.assertAlmostEqual(
                            result, 
                            tc["result"], 
                            places=7, 
                            msg=f'{tc["test_name"]} failed: {tc["n"]}√{tc["x"]} != {tc["result"]}, got {result}'
                        )
    
    def test_nth_root_types(self):
        testCases  = [
            {"test_name": "test_array_1",     "x": [1, 3, 5],       "n": [1, 2],  "exeception": TypeError},
            {"test_name": "test_array_2",     "x": [1, 3, 5],       "n": 2,       "exeception": TypeError},
            {"test_name": "test_string_1",    "x": "Hello, ",       "n":"world!", "exeception": TypeError},
            {"test_name": "test_string_2",    "x": "Nicola",        "n":1,        "exeception": TypeError},
            {"test_name": "test_dict",        "x": {"dict": 18},    "n":5,        "exeception": TypeError},
            {"test_name": "test_bool_1",      "x": True,            "n":True,     "exeception": ZeroDivisionError},
            {"test_name": "test_bool_2",      "x": True,            "n":False,    "exeception": ValueError},
            {"test_name": "test_tuple",       "x": (1, 2),          "n":2,        "exeception": TypeError},
            {"test_name": "test_set",         "x": {1, 2},          "n":6,        "exeception": TypeError},
        ]
        for tc in testCases:
            with self.subTest(tc["test_name"]):
                if "exeception" in tc:
                    with self.assertRaises(tc["exeception"]):
                        self.calculator.log(tc["x"], tc["n"])
                else:
                    result = self.calculator.log(tc["x"], tc["n"])
                    self.assertEqual(
                        result, 
                        tc["result"], 
                        f'{tc["test_name"]} failed: {tc["n"]}√{tc["x"]} != {tc["result"]}, got {result}'
                    )

if __name__ == "__main__":
    unittest.main()
