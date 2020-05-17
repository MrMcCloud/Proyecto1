from Ruedas import Ruedas
from Estanque import Estanque
from Velocimetro import Velocimetro


class Auto():
    def __init__(self, motor):
        self.__motor = motor
        self.__estanque = Estanque(32)
        self.__ruedas = [Ruedas(0), Ruedas(0), Ruedas(0), Ruedas(0)]
        self.__velocimetro = Velocimetro()
        self.__encendido = False

    def get_motor(self):
        return self.__motor

    def set_estanque(self, nivel):
        self.__estanque = Estanque(nivel)

    def get_estanque(self):
        return self.__estanque

    def set_ruedas(self, num, max_st):
        for i in range(num):
            r = Ruedas(max_st)
            self.__ruedas.append(r)

    def get_ruedas(self, num):
        return self.__ruedas[num]

    def set_velocimetro(self):
        self.__velocimetro = Velocimetro()

    def get_velocimetro(self):
        return self.__velocimetro

    def set_encendido(self, estado):
        self.__encendido = estado

    def get_encendido(self):
        return self.__encendido

    def delta_encendido(self, llave):
        if llave == 'E':
            self.set_encendido(True)
            self.get_estanque().set_nivel(self.get_estanque().get_nivel()-(self.get_estanque().get_nivel()*0.01))
            print("el auto se a encendido")
        elif llave == 'e':
            self.set_encendido(True)
            self.get_estanque().set_nivel(self.get_estanque().get_nivel()-(self.get_estanque().get_nivel() * 0.01))
            print("el auto se a encendido")
        elif llave == 'Q':
            self.set_encendido(False)
            print("el auto se a apagado")
        elif llave == 'q':
            self.set_encendido(False)
            print("el auto se a apagado")
        else:
            self.set_encendido(False)

    def avance(self, a):
        if a == "w":
            self.get_velocimetro().delta_distancia()
            for i in range(4):
                self.get_ruedas(i).delta_desgaste(self.get_velocimetro().get_velocidad())
            self.get_estanque().delta_tanque(self.get_velocimetro().get_distancia(), self.get_motor().get_kmetraje())
        elif a == "W":
            self.get_velocimetro().delta_distancia()
            for i in range(4):
                self.get_ruedas(i).delta_desgaste(self.get_velocimetro().get_velocidad())
            self.get_estanque().delta_tanque(self.get_velocimetro().get_distancia(), self.get_motor().get_kmetraje())

    def status(self):
        s_distancia = self.get_velocimetro().get_distancia()
        s_velocidad = self.get_velocimetro().get_velocidad()
        s_tiempo = self.get_velocimetro().get_tiempo()
        s_rueda1 = self.get_ruedas(0).get_desgaste()
        s_rueda2 = self.get_ruedas(1).get_desgaste()
        s_rueda3 = self.get_ruedas(2).get_desgaste()
        s_rueda4 = self.get_ruedas(3).get_desgaste()
        s_estanque = self.get_estanque().get_nivel()
        print("estado del auto\n"
              "-distancia recorrida: ", s_distancia, "Km"
              "\n-velocidad media: ", s_velocidad, "Km/h"
              "\n-tiempo transcurrido: ", s_tiempo, "h"
              "\n-nivel de conbustible: ", s_estanque, "%"
              "\n-estado de las reuedas:\n"
              "  +reueda 1: ", s_rueda1, "%"
              "\n  *rueda 2: ", s_rueda2, "%"
              "\n  +rueda 3: ", s_rueda3, "%"
              "\n  +rueda 4: ", s_rueda4, "%")
