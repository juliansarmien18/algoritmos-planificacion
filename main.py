
from pantalla import Pantalla
from algoritmos import *

gData = {'P1': [0,10], 'P2': [1,2], 'P3': [4,4], 'P4':[5,1], 'P5': [10,3], 'P6':[21,12]}
gQuant = 4
gContSwitch = 0.4

fcfs_obj =  FirstComeFirstServed()
sjf_obj = ShortestJobFirst()
srtf_obj = ShortestRemainingTimeFirst()


proceso_fcfs,posiciones_fcfs = fcfs_obj.fcfs(gData)
proceso_sjf,posiciones_sjf = sjf_obj.sjf(gData)
proceso_strf,posiciones_srtf = srtf_obj.srtf(gData)
Pantalla().printData(gData,proceso_fcfs,posiciones_fcfs,'First Come First Served')
Pantalla().printData(gData,proceso_sjf,posiciones_sjf,'Shortest Job First')
Pantalla().printData(gData,proceso_strf,posiciones_srtf,'Shortest Remaning Time First')

