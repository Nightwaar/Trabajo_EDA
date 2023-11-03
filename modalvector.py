import numpy as np
import random
class arreglo():
    __arreglo=[]
    __tamaño=0
    __maxnum=0
    __sub=[]
    def __init__(self,tamaño,max):
        self.__tamaño=tamaño
        self.__maxnum=max
        self.__arreglo=np.empty(self.__tamaño,dtype=int)
        self.__sub=np.empty(self.__maxnum,dtype=int)
    
    
    def cargar(self):
        i=0
        while i<self.__tamaño:
            self.__arreglo[i]=random.randint(1,self.__maxnum)
            i+=1
        j=0
        while j<self.__maxnum:
            self.__sub[j]=0
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
        self.__sub[numero-1]+=1

    def contador(self):
        i=0
        maximo=self.maximo()
        while i<len(self.__sub):
            if self.__sub[i]==maximo:
                print(f"El numero {i+1} se repite {maximo} veces")
            i+=1
        

    def mostrarsub(self):
        i=0
        while i<self.__maxnum:
            print(self.__sub[i])
            i+=1

    def maximo(self):
        i=0
        nummax=0
        while i<len(self.__sub):
            if self.__sub[i]>nummax:
                nummax=self.__sub[i]
            i+=1
        return(nummax)
if __name__=="__main__":
    arreglo=arreglo(150,100)
    arreglo.cargar()
    arreglo.recorre()