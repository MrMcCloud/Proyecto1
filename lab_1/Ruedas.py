class Ruedas():
    def __init__(self, desgaste):
        self.__desgaste = desgaste

    def set_desgaste(self, nivel):
        self.__desgaste = nivel

    def get_desgaste(self):
        return self.__desgaste

    def delta_desgaste(self, velocidad):
        tasa = 0
        if velocidad <= 20:
            tasa = 1
        if velocidad <= 40:
            if velocidad > 20:
                tasa = 2
        if velocidad <= 60:
            if velocidad > 40:
                tasa = 4
        if velocidad <= 80:
            if velocidad > 60:
                tasa = 6
        if velocidad <= 100:
            if velocidad > 80:
                tasa = 8
        if velocidad <= 120:
            if velocidad > 80:
                tasa = 10
        self.set_desgaste(self.get_desgaste() + tasa)
