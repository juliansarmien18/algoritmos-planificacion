"""Imports de las clases"""
from pantalla import Pantalla
from algoritmos import *


if __name__ =='__main__':
    
    #seteo de datos iniciales
    gData = {'P1': [0,10], 'P2': [1,2], 'P3': [4,4], 'P4':[5,1], 'P5': [10,3], 'P6':[21,12]}
    gQuant = 4
    gContSwitch = 0.4

    #instancia de las clases
    fcfs_obj =  FirstComeFirstServed()
    sjf_obj = ShortestJobFirst()
    srtf_obj = ShortestRemainingTimeFirst()

    #invocacion de los algoritmos
    proceso_fcfs,posiciones_fcfs = fcfs_obj.fcfs(gData)
    proceso_sjf,posiciones_sjf = sjf_obj.sjf(gData)
    proceso_strf,posiciones_srtf = srtf_obj.srtf(gData)
    
    #Impresion de datos
    Pantalla().printData(gData,proceso_fcfs,posiciones_fcfs,'First Come First Served')
    Pantalla().printData(gData,proceso_sjf,posiciones_sjf,'Shortest Job First')
    Pantalla().printData(gData,proceso_strf,posiciones_srtf,'Shortest Remaning Time First')

