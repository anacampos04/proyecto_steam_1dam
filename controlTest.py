import unittest
from control import Control


class controlTest(unittest.TestCase):

    def setUp(self):
        self.control = Control()

    def tearDown(self):
        self.control = None

    def testControlNotNull(self):
        self.assertIsNotNone(self.control, "Control no debe ser null")
        print("Se ha ejecutado el método testControlNotNull")

    def testValorMaximoNegativo(self):
        valores  = {-3,-1}
        self.assertEqual(self.modelo.get_valor_max(valores), -1, "El valor máximo entre -3 y -1 debe ser -1")

    def testValorMaximoPositivo(self):
        valores  = {1, 3}
        self.assertEqual(self.modelo.get_valor_max(valores), 3, "El valor máximo entre 1y 3 debe ser 3")

    def testValorMinimoPositivo(self):
        valores  = {1, 3}
        self.assertEqual(self.modelo.get_valor_max(valores), 1, "El valor mínimo entre 1 y 3 debe ser 1")
    
    def testValorMinimoNegativo(self):
        valores  = {-1, -3}
        self.assertEqual(self.modelo.get_valor_max(valores), -3, "El valor mínimo entre -1 y -3 debe ser -3")


if __name__ == '__main__':
    unittest.main()
