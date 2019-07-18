class Marcador(object):
    def __init__(self):
        self.puntos = {'A': 0, 'B': 0}
        
        self.set_ganados = {'A': 0, 'B': 0}

        self.estado = 0
        
        self.set_act = 1
        
        self.juego_terminado = 0

    def agrega_puntos(self, jugador, puntos):
        self.puntos[jugador] += puntos
        print('Marcador', self.retorna_marcador())
        self.checa_marcador()

    def checa_marcador(self):

        if self.puntos['A'] in [20, 29] and self.puntos['A'] == self.puntos['B']:
            self.estado = self.puntos['A']

        for k in self.puntos:
            if self.puntos[k] == 21 and not self.estado:
                print("Jugador %s gana set %s " % (k, self.set_act))
                self.set_ganados[k] += 1
                self.set_act += 1
                self.puntos = {'A': 0, 'B': 0}
            if self.set_ganados[k] == 2:
                print("Jugador %s gana juego" % k)
                self.juego_terminado = 1

    def retorna_marcador(self):
        return self.puntos
        
    def es_finalizado(self):
        return self.juego_terminado

if __name__ == "__main__":

    mc = Marcador()
    print('-- Marcador badminton --')
    print('Jugadores A y B')
    opc = '0'
    while not mc.es_finalizado():
        print('1) Anadir punto (Ejemplo A1)')
        opc = input('Introduce opcion...')
        jugador, puntos = opc[0], opc[1:]
        mc.agrega_puntos(jugador, int(puntos))

