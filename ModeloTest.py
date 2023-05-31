import unittest
from modelo import Mediciones

class ModeloTest(unittest.TestCase):
    
    def setUp(self):
        self.modelo=Mediciones()
        
    def tearDown(self):
        self.modelo=None
        
    def testMediaNotNull(self):
        self.assertIsNotNone(self.modelo.get_temperaturas(),"No debe ser nulo")

    def testMediaIncorrecta(self):
        valores= [50,22,18,34]
        self.assertEqual(self.modelo.get_valor_medio(valores),31,"La media entre los valores anteriores tiene que ser 31")
        

if __name__ == "__main__":
    unittest.main()