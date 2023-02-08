import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def test_2_mas_2(self):
        calc = Calculadora()
        self.assertEqual(4,calc.sumar(2,2))

class TestCalculadora(unittest.TestCase):
    def test_2_mas_2(self):
        calc = Calculadora()
        self.assertEqual(11,calc.sumar(10,2))

if __name__ == '__main__':
    unittest.main()


#52.40.132.229