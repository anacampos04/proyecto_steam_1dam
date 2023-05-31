from sense_emu import SenseHat
import unittest
from p import presion
import pandas as pd

class presionTest(unittest.TestCase):
    
   def setUp(self):
        self.sense = SenseHat()
        
    def tearDown(self):
        self.sense.clear()
        
    def test_inicializacion(self):
        self.assertlsNotNone(self.sense)
        
    def test_lectura_presion(self):
        presion = self.sense.get_pressure()
        self.assertlsInstance(presion,float)
        
    def test_limites_presion(self):
        presion_maxima = 2000
        presion_minima = 800
        
        presion = self.sense.get_pressure()
        self.assertLessEqual(presion,presion_maxima,"La presion no puede ser mayor que 2000")
        self.assertGreaterEqual(presion,presion_minima, "La presion no puede ser menor que 800)
    
    def test_precision_presion(self):
        pression_esperada = 1013.25
        presion = self.sense.get_pressure()
        self.assertAlmostEqual(presion,presion_esperada,delta=10)
        
        if name == 'main':
            unittest.main()