"""class torre:
    def __init__(self, discos):
        self.num_discos = discos
        self.origen = list(range(discos, 0, -1))
        self.destino = []
        self.intermedio = []

    def colocar_el_disco(self, origen, lugar_a_mover):
        disco = origen.pop()
        lugar_a_mover.append(disco)
        print(f"Se mueve el disco de {origen} a {lugar_a_mover}")

    def mover_la_torre(self, altura, origen, destino, intermedio):
        if altura >= 1:
            self.mover_la_torre(altura - 1, origen, intermedio, destino)
            self.colocar_el_disco(origen, destino)
            self.mover_la_torre(altura - 1, intermedio, destino, origen)

    def solucion_de_la_torre(self):
        self.mover_la_torre(self.num_discos, self.origen, self.destino, self.intermedio)


discos_elegidos = int(input("Escribe el numero de discos con el que se desea jugar: "))
juego = torre(discos_elegidos)
juego.solucion_de_la_torre()"""

class Torre:
    def __init__(self, discos):
        self.num_discos = discos
        self.origen = list(range(discos, 0, -1))
        self.destino = []
        self.intermedio = []

    def mover_la_torre(self, altura, origen, destino, intermedio):
        if altura >= 1:
            self.mover_la_torre(altura - 1, origen, intermedio, destino)
            disco = origen.pop()
            destino.append(disco)
            print(f"Se mueve el disco de {origen} a {destino}")
            self.mover_la_torre(altura - 1, intermedio, destino, origen)

    def solucion_de_la_torre(self):
        self.mover_la_torre(self.num_discos, self.origen, self.destino, self.intermedio)


discos_elegidos = int(input("Escribe el número de discos con el que se desea jugar: "))
juego = Torre(discos_elegidos)
juego.solucion_de_la_torre()




