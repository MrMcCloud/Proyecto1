from Auto import Auto
from Motor import Motor


if __name__ == '__main__':

    ejecucion = True
    encendido = False
    while ejecucion is True:
        print("creacion del auto")
        m = Motor()
        m.choice_cilindrada()
        m.choice_Kmetraje()
        a = Auto(m)
        print("El auto a sido creado")
        if encendido is False:
            key = input("ingrese E para encender el auto\n>>")
            a.delta_encendido(key)
            if a.get_encendido() is False:
                break
        final = False
        while final is False:
            a.status()
            mv = input("ingresa W para avanzar\n>>")
            a.avance(mv)
            for i in range(4):
                if a.get_ruedas(i).get_desgaste() >= 90:
                    a.delta_encendido("q")
                    a.get_ruedas(i).set_desgaste(0)
                    a.delta_encendido("e")
            if a.get_estanque().get_nivel() == 0:
                a.status()
                a.delta_encendido("q")
                final = True
                ejecucion = False