
import pygame

#Clase que define el metodo jugador
class Jugador:
    def __init__(self, tam_paleta, cantidad_paleta, tipo_jugador):
        pygame.sprite.Sprite.__init__(self)

        "Atributos"

        self.tam_paleta=tam_paleta
        self.cantidad_paleta=cantidad_paleta
        self.posy=0
        self.tipo_jugador=tipo_jugador



    def movimiento_humano(self):
        pass

