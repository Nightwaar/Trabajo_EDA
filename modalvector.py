import numpy as np
import random
class arreglo():
    __arreglo=[]
    __tamaño=0
    __numeromaximo=0
    __arreglocontador=[]
    def __init__(self,tamaño,maximo):
        self.__tamaño=tamaño
        self.__numeromaximo=maximo
        self.__arreglo=np.empty(self.__tamaño,dtype=int)
        self.__arreglocontador=np.empty(self.__numeromaximo,dtype=int)
    
    
    def cargar(self):
        i=0
        while i<self.__tamaño:
            self.__arreglo[i]=random.randint(1,self.__numeromaximo)
            i+=1
        j=0
        while j<self.__numeromaximo:
            self.__arreglocontador[j]=0
            j+=1
    def mostrar(self):
        i=0
        while i<self.__tamaño:
            print(self.__arreglo[i])
            i+=1

    def recorre(self):
        i=0
        while i<self.__tamaño:
            self.aumenta(self.__arreglo[i])
            i+=1
        self.contador()


    def aumenta(self,numero):
        self.__arreglocontador[numero-1]+=1

    def contador(self):
        i=0
        maximo=self.maximo()
        while i<len(self.__arreglocontador):
            if self.__arreglocontador[i]==maximo:
                print(f"El numero {i+1} se repite {maximo} veces")
            i+=1
        

    def mostrarsub(self):
        i=0
        while i<self.__numeromaximo:
            print(self.__arreglocontador[i])
            i+=1

    def maximo(self):
        i=0
        nummax=0
        while i<len(self.__arreglocontador):
            if self.__arreglocontador[i]>nummax:
                nummax=self.__arreglocontador[i]
            i+=1
        return(nummax)
if __name__=="__main__":
    arreglo=arreglo(20,5)
    arreglo.cargar()
    arreglo.recorre()
