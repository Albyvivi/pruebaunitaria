from contextlib import AbstractContextManager
from typing import Any
import calculadora
import unittest

class TestCalculadora(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(calculadora.suma(2, 3), 5)
        self.assertEqual(calculadora.suma(-2, 3), 1)
        self.assertEqual(calculadora.suma(-2, -3), -5)

    def test_resta(self):
        self.assertEqual(calculadora.resta(2, 3), -1)
        self.assertEqual(calculadora.resta(-2, 3), -5)
        self.assertEqual(calculadora.resta(-2, -3), 1) 

    def test_multiplicacion(self):
        self.assertEqual(calculadora.multiplicacion(2, 3), 6)
        self.assertEqual(calculadora.multiplicacion(-2, 3), -6)
        self.assertEqual(calculadora.multiplicacion(-2, -3), 6)

    def test_division(self):
        self.assertEqual(calculadora.division(6, 3), 2)
        self.assertEqual(calculadora.division(-6, 3), -2)
        self.assertEqual(calculadora.division(-6, -3), 2)
        self.assertEqual(calculadora.division(6, -3), -2)
        self.assertRaises(ValueError, calculadora.division, 6, 0)

if __name__ == '__main__':
    unittest.main()

# Run the test:
# $ python test_calculadora.py
    