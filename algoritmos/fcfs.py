
"""Algoritmo FCFS"""
class FirstComeFirstServed:
    
    """definicion de atributos"""
    def __init__(self):
        self.btHold = 0
        self.taHold = 0
        self.linea_posiciones = []
        self.dict_fcfs = {}
    
    """Metodo que refleja el algoritmo"""
    def fcfs(self, data : dict):
        #recorre los datos que se le pasan por parametro
        for key,value in data.items():
            at,bt = value[0],value[1]
            
            #valida los datos que va recorriendo para realizar la planificacion de procesos
            if (at == 0):
                self.taHold += bt
                self.dict_fcfs[key] = [self.btHold-at,bt-at]
                self.linea_posiciones.append([key,self.taHold])
                self.btHold = bt
            elif(self.btHold-at > 0):
                self.taHold += bt
                self.dict_fcfs[key] = [self.btHold-at,self.taHold-at]
                self.linea_posiciones.append([key,self.taHold])
                self.btHold += bt
            else:
                self.taHold += bt
                self.dict_fcfs[key] = [0,bt]
                self.linea_posiciones.append([key,self.taHold+1])
                self.btHold += bt
        #retorna la lista de posiciones generada junto a los procesos
        return self.dict_fcfs,self.linea_posiciones