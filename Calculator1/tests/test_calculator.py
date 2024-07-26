import unittest
from calculator.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        calc = Calculator(1, 2)
        self.assertEqual(calc.add(), 3)

    def test_subtract(self):
        calc = Calculator(5, 3)
        self.assertEqual(calc.subtract(), 2)

    def test_multiply(self):
        calc = Calculator(10, 5)
        self.assertEqual(calc.multiply(), 50)

    def test_divide(self):
        calc = Calculator(20, 5)
        self.assertEqual(calc.divide(), 4)

    def test_divide_by_zero(self):
        calc = Calculator(20, 0)
        self.assertIsNone(calc.divide())

    def test_nroot(self):
        calc = Calculator(27, 3)
        self.assertAlmostEqual(calc.nroot(), 3)

    def test_nroot_zero_divisor(self):
        calc = Calculator(27, 0)
        self.assertIsNone(calc.nroot())

    def test_invalid_input_string(self):
        with self.assertRaises(TypeError):
            Calculator("a", 2)

    def test_invalid_input_none(self):
        with self.assertRaises(TypeError):
            Calculator(None, 2)

    def test_reset(self):
        calc = Calculator(10, 5)
        calc.add()
        calc.reset()
        self.assertEqual(calc.memory, 0)

    def test_chaining_operations(self):
        calc = Calculator(10, 5)
        self.assertEqual(calc.add().subtract().multiply().divide().memory, 2.0)


if __name__ == '__main__':
    unittest.main()