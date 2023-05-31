
from sense_emu import SenseHat
#import pandas as pd
import matplotlib.pyplot as plt

class Vista:
    
    def __init__(self):
        self.sense=SenseHat()
        
    def menu(self):
        print("0. Menú:")
        print("1. Medir temperatura")
        print("2. Medir presión")
        print("3. Medir humedad")
        print("4. Grafico de la temperatura")
        print("5. Grafico de la presion")
        print("6. Grafico de la humedad")
        print("7. Valor medio de la temperatura")
        print("8. Valor medio de la presión")
        print("9. Valor medio de la humedad")
        print("10. Valor maximo temperatura")
        print("11. Valor maximo presion")
        print("12. Valor maximo humedad")
        print("13. Valor minimo temperatura")
        print("14. Valor minimo presion")
        print("15. Valor minimo humedad")
        print("16. Leer fichero")
        print("17. Escribir fichero")
        print("s. Salir")
        return input("Ingrese la opción deseada: ")
    
    def mostrar_temperatura(self,t):
        self.sense.show_message("{}C".format(t))
        print(t)
        
    def mostrar_presion(self,p):
        self.sense.show_message("{}Mbar".format(p))
        print(p)
          
    def mostrar_humedad(self,h):
        self.sense.show_message("{}%".format(h))
        print(h)
        
    def mostrar_valor_max(self,m,textito):
        if textito=="temperatura" :
            self.sense.show_message("{}C".format(m))
        elif textito=="presion" :
            self.sense.show_message("{}bar".format(m))
        elif textito=="humedad" :
            self.sense.show_message("{}g/m3".format(m))
        print(m)
        
    def mostrar_valor_min(self,m,textito):
        if textito=="temperatura":
            self.sense.show_message("{}C".format(m))
        elif textito=="presion":
            self.sense.show_message("{}bar".format(m))
        elif textito=="humedad":
            self.sense.show_message("{}g/m3".format(m))
        print(m)
          
    def mostrar_valor_medio(self, m, texto):
        if texto=="temperatura" :
            self.sense.show_message("{}C".format(m))
        elif texto=="presion" :
            self.sense.show_message("{}bar".format(m))
        elif texto=="humedad" :
            self.sense.show_message("{}g/m3".format(m))
        print(m)   
    
    
    def leer_fichero(f):
        print(f.readline())
      
 
    
    def mostrar_grafico_temperatura (self, temperaturas):
        df_temperatura = pd.DataFrame({'Temperatura': temperaturas})

        # crear un gráfico de línea
        df_temperatura.plot(kind='line')

        # personalizar el gráfico con títulos y etiquetas de los ejes
        plt.title('Temperatura')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Temperatura (°C)')

        # mostrar el gráfico
        plt.show()

    def mostrar_grafico_presion (self, presiones):
        df_presion = pd.DataFrame({'Presión': presiones})

        # crear un gráfico de línea
        df_presion.plot(kind='line')

        # personalizar el gráfico con títulos y etiquetas de los ejes
        plt.title('Presión')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Presión (mbar)')

        # mostrar el gráfico
        plt.show()
        
    def mostrar_grafico_humedad (self, humedades):
        df_humedad = pd.DataFrame({'Humedad': humedades})

        # crear un gráfico de línea
        df_humedad.plot(kind='line')

        # personalizar el gráfico con títulos y etiquetas de los ejes
        plt.title('Humedad')
        plt.xlabel('Tiempo (minutos)')
        plt.ylabel('Humedad (%)')

        # mostrar el gráfico
        plt.show()
        
   
