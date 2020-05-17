
class Estanque():
    def __init__(self, nivel):
        self.__Nestanque = nivel
        self.__kk = nivel

    def set_nivel(self, nivel):
        self.__Nestanque = nivel

    def get_nivel(self):
        return self.__Nestanque

    def delta_tanque(self, distancia, kmetraje):
        quemado = int(distancia/kmetraje)
        if self.get_nivel() >= quemado:
            self.set_nivel(self.get_nivel()-quemado)
        elif self.get_nivel() < quemado:
            self.set_nivel(0)

#estubiste trabajando aqui. probablemente no terminado, revisar antes de continuar