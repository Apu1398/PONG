
from Principal import *
import pygame
WHITE = (0,0,0)

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x, tam_paleta, tipo_jugador, ventana):

        """Clase Jugador"""
        pygame.sprite.Sprite.__init__(self)

        "Atributos"

        self.tam_paleta=tam_paleta
        #self.cantidad_paleta=cantidad_paleta
        self.tipo_jugador=tipo_jugador
        self.paleta= pygame.draw.line(ventana, WHITE, [10, 5], [10,tam_paleta], 15)
        self.rect = self.paleta.get_rect()
        self.rect.centerx=x
        self.centery=LARGO_VENTANA/2

    def tipo_Jugador(self, tipo_jugador):
        "Metodo que elige si es jugador humano o AI"

        if tipo_jugador==True:
            self.movimiento_humano()
        else:
            self.movimiento_AI()

    def movimiento_humano(self):
        "Metodo que le da movimiento al humano"
        if self.rect.bottom >=  LARGO_VENTANA:
            self.rect.bottom = LARGO_VENTANA
        elif self.rect.top <=0:
            self.rect.top = 0

    def movimiento_AI(self):
        pass

