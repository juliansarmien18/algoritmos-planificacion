
"""Clase que ejecuta el algoritmo Shortest Remaining Time First"""
class ShortestRemainingTimeFirst:
    
    #definicion de atributos
    def __init__(self):
        self.begHold = 0
        self.endHold = 0
        self.dict_srtf = {}
        self.linea_posiciones = []
    
    #metodo que ejecuta el algoritmo
    def srtf(self, data : dict):
        dict_temporal,dict_ordenado = {},{}
        
        #recorre los datos del diccionario de listas y valida su informacion
        for key,value in data.items():
            at,bt = value[0],value[1]
            if (self.begHold == 0):
                second = list(data.values())[1]
                self.dict_srtf[key] = [self.begHold-at, bt-second[0]-at]
                self.endHold += bt-second[0]
                self.begHold = bt-second[0]
                dict_temporal[key] = at, bt-self.begHold
                self.linea_posiciones.append([key,self.endHold])
            else:
                dict_temporal[key] = at,bt
                
        #Usa el diccionario temporal como auxiliar para llenar al diccionario ordenado
        for key,value in reversed(sorted(dict_temporal.items(), key = lambda x : x[1][1],reverse=True)):
            dict_ordenado[key] = value[0],value[1]
        for key,value in dict_ordenado.items():
            at,bt = value[0], value[1]
            if key in self.dict_srtf.keys():
                hold = self.dict_srtf[key]
                self.endHold += bt
                self.dict_srtf[key] = [self.begHold-hold[1],self.endHold-at]
                self.linea_posiciones.append([key,self.endHold])
                self.begHold += bt
            elif(self.begHold-at > 0):
                self.endHold += bt
                self.dict_srtf[key] = [self.begHold-at,self.endHold-at]
                self.linea_posiciones.append([key,self.endHold])
                self.begHold += bt
            else:
                self.endHold += bt
                self.dict_srtf[key] = [0,bt]
                self.linea_posiciones.append([key,self.endHold+1])
                self.begHold += bt 
                
        #retorna los procesos junto a la linea de posiciones
        return self.dict_srtf, self.linea_posiciones