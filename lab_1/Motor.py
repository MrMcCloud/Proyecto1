import random


class Motor():
    def __init__(self):
        self.__cilindrada = None
        self.__Kmetraje = None

    def set_kmetraje(self, constante):
        self.__Kmetraje = constante

    def get_kmetraje(self):
        return self.__Kmetraje

    def set_cilindrada(self, choice):
        self.__cilindrada = choice

    def get_cilindrada(self):
        return self.__cilindrada

    def choice_cilindrada(self):
        c = random.randint(1, 3)
        if c == 1:
            self.set_cilindrada(1.2)
        else:
            self.set_cilindrada(1.6)

    def choice_Kmetraje(self):
        if self.get_cilindrada() == 1.2:
            self.set_kmetraje(20)
        else:
            self.set_kmetraje(14)

#esto deberia estar bien, revisar antes de continuar