import random


class Velocimetro():
    def __init__(self):
        self.__Velocidad = 0
        self.__Distancia = 0
        self.__Tiempo = 0

    def set_velocidad(self, v):
        self.__Velocidad = v

    def get_velocidad(self):
        return self.__Velocidad

    def set_distancia(self, d):
        self.__Distancia = d

    def get_distancia(self):
        return self.__Distancia

    def set_tiempo(self, t):
        self.__Tiempo = t

    def get_tiempo(self):
        return self.__Tiempo

    def delta_tiempo(self):
        self.set_tiempo(self.get_tiempo()+random.randint(1, 11))

    def delta_velocidad(self):
        delta = self.get_velocidad()+random.randint(1, 3)
        if delta > 120:
            self.set_velocidad(120)
        else:
            self.set_velocidad(delta)

    def delta_distancia(self):
        self.delta_velocidad()
        self.delta_tiempo()
        self.set_distancia(self.get_velocidad()*self.get_tiempo())

#deberia esta terminado. rebisar antes de continuar