import unittest
from calculadora import sumar, restar

class PruebasCalculadora(unittest.TestCase):

    def test_suma(self):
        # Comprueba que 2 + 3 es 5
        self.assertEqual(sumar(2, 3), 5)

    def test_resta(self):
        # Comprueba que 10 - 4 es 6
        self.assertEqual(restar(10, 4), 6)
