import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(8, -7), 1)
    # Add the following test methods to the TestCalculator class:
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(3, 1), 2)
        self.assertEqual(self.calc.subtract(10, 4), 6)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)
        self.assertEqual(self.calc.multiply(3, 5), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(4, 4), 1)
        self.assertEqual(self.calc.divide(0, 3), 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(101, 10), 1)
        self.assertEqual(self.calc.modulo(127, 3), 1)

if __name__ == '__main__':
    unittest.main()