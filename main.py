"""Imports de las clases"""
from pantalla import Pantalla
from algoritmos import *


if __name__ =='__main__':
    
    #seteo de datos iniciales
    gData = {'P1': [6,5], 'P2': [2,7], 'P3': [4,9], 'P4':[3,1], 'P5': [1,2], 'P6':[20,15]}
    print('Procesos:', gData)
    print("")

    #instancia de las clases
    fcfs_obj =  FirstComeFirstServed()
    sjf_obj = ShortestJobFirst()
    srtf_obj = ShortestRemainingTimeFirst()

    #invocacion de los algoritmos
    proceso_fcfs,posiciones_fcfs = fcfs_obj.fcfs(gData)
    proceso_sjf,posiciones_sjf = sjf_obj.sjf(gData)
    proceso_strf,posiciones_srtf = srtf_obj.srtf(gData)
    
    #Impresion de datos
    Pantalla().imprimir_datos(gData,proceso_fcfs,posiciones_fcfs,'First Come First Served')
    Pantalla().imprimir_datos(gData,proceso_sjf,posiciones_sjf,'Shortest Job First')
    Pantalla().imprimir_datos(gData,proceso_strf,posiciones_srtf,'Shortest Remaning Time First')

