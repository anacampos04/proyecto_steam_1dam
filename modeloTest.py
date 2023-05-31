import unittest
from modelo import Mediciones

class ModeloTest(unittest.TestCase):

    def setUp(self):
        self.modelo = Modelo()

    def testHumedadNoMenorQueCero(self):
        humedad = self.modelo.getHumedad()
        
        self.assertGreaterEqual(humedad, 0, "La humedad no debe ser menor que cero")
        print("Humedad menor que 0")

    def testHumedadNoMayorQueCien(self):
        humedad = self.modelo.getHumedad()

        # Verificamos que la humedad no sea mayor que cien
        self.assertLessEqual(humedad, 100, "La humedad no debe ser mayor que cien")
        print("Humedad mayor que 100")
        
    def setUp(self):
        self.modelo=Mediciones()
        
    def tearDown(self):
        self.modelo=None
        
    def testMediaNotNull(self):
        self.assertIsNotNone(self.modelo.get_temperaturas(),"No debe ser nulo")

    def testMediaIncorrecta(self):
        valores= [50,22,18,34]
        self.assertEqual(self.modelo.get_valor_medio(valores),31,"La media entre los valores anteriores tiene que ser 31")
        
        
    if __name__ == '__main__':
        unittest.main()