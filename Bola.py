import pygame
from pygame.rect import Rect


class Bola:

    """Clase bola"""

    def __int__(self ,bola):

        self.bola = bola

    def dibujar_bola(self, bola, ventana):
        pygame.draw.ellipse(ventana, (255, 255, 255), bola)

    def moverse_bola(self, bola, dx, dy):

        (bola).move_ip(dx, dy)

        if (bola).y < 0 or (bola).y > 25:
            dy*=-1
        if (bola).x < 0 or (bola).x > 40:
            dx*=-1


