
"""Clase del algoritmo Shortest Job First"""
class ShortestJobFirst:
    
    #definicion de atributos
    def __init__(self):
        self.begHold = 0
        self.endHold = 0
        self.dict_sjf = {}
        self.linea_posiciones = []
    
    #metodo que ejecuta el algoritmo
    def sjf(self, data : dict):
        dict_temporal,dict_ordenado={},{}
        
        #recorre el diccionario de listas y valida sus datos para planificar los procesos
        for key,value in data.items():
            at,bt = value[0],value[1]
            if (self.begHold == 0):
                self.endHold += bt
                self.dict_sjf[key] = [self.begHold-at,bt-at]
                self.linea_posiciones.append([key,self.endHold])
                self.begHold = bt
            else:
                dict_temporal[key] = value[0],value[1]
        
        #recorre el diccionario temporal como auxiliar para llenar el diccionario ordenado
        for key,value in sorted(dict_temporal.items(), key = lambda x : x[1][1]):
            dict_ordenado[key] = value[0],value[1]
        for key,value in dict_ordenado.items():
            at,bt = value[0],value[1]
            if(self.begHold-at > 0):
                self.endHold += bt
                self.dict_sjf[key] = [self.begHold-at,self.endHold-at]
                self.linea_posiciones.append([key,self.endHold])
                self.begHold += bt
            else:
                self.endHold += bt
                self.dict_sjf[key] = [0,bt]
                self.linea_posiciones.append([key,self.endHold+1])
                self.begHold += bt       
                
        #retorna los procesos junto a la lista de posiciones
        return self.dict_sjf,self.linea_posiciones
