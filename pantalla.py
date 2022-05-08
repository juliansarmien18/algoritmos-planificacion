
"""definicion de la clase que imprime los datos de cada proceso planificado"""
class Pantalla:
    
    """Definicion de atributos"""
    def __init__(self):
        self.prom_tiempo_espera = 0
        self.prom_tiempo_respuesta = 0
        self.linea_procesosstr= "0 -> "

    """Imprime el nombre del proceso junto a los calculos obtenidos en los respectivos metodos de cada clase"""
    def printData(self, gData, procesos, linea_procesos, nombre):
        #impresion del nombre y titulos
        print(nombre.upper())
        print('| CLAVE | LLEGADA | EXPLOSION | ESPERAR |')
        
        #recorrido los procesos e imprime los datos segun corresponda
        for key,value in sorted(procesos.items()):
            print('{:>4}{:>8}{:>9}{:>8}{:>10}'.format(key,gData[key][0],gData[key][1],value[0],value[1]))
            self.prom_tiempo_espera += value[0]
            self.prom_tiempo_respuesta += value[1]
        
        print("")
        #impresion del calculo de tiempos
        print('Tiempo de Espera promedio = {}    Tiempo de respuesta promedio = {}\n'.format(self.prom_tiempo_espera/len(procesos),self.prom_tiempo_respuesta/len(procesos)))
        
        #imprsion de la linea de procesos
        for x in linea_procesos:
            self.linea_procesosstr += ('{} -> {} -> '.format(x[0],x[1]))
        print('{}\n'.format(self.linea_procesosstr[:-3]))