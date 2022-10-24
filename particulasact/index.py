from array import array
import string
from particulasact.particula import Particula


class Nodo():
    dato = None
    siguiente = None
    anterior = None

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class Lista_ligada():
    nodo_inicial = None
    nodo_final = None
    no_elements = 0

    def __init__(self):
        self.nodo_inicial = None
        self.nodo_final = None

    def agregar_inicio(self, nodo):
        if(self.no_elements == 0):
            self.nodo_inicial = nodo
            self.nodo_final = nodo
            self.no_elements = self.no_elements + 1
        else:
            temporal = self.nodo_inicial
            temporal.anterior = nodo
            nodo.siguiente = temporal
            self.nodo_inicial = nodo
            self.no_elements = self.no_elements + 1

    def agregar_final(self, nodo):
        if(self.no_elements == 0):
            self.nodo_inicial = nodo
            self.nodo_final = nodo
            self.no_elements = self.no_elements + 1
        else:
            temporal = self.nodo_final
            temporal.siguiente = nodo
            nodo.anterior = temporal
            self.nodo_final = nodo
            self.no_elements = self.no_elements+1

    def mostrar(self):
        temp = self.nodo_inicial
        while(temp):
            print(temp.dato)
            temp = temp.siguiente

    def __str__(self):
        temp = self.nodo_inicial
        array = []
        while(temp):
            array.append(str(temp.dato))
            temp = temp.siguiente

        return "".join(array)
