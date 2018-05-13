import pygame

class Bola(pygame.sprite.Sprite):

    """Clase bola"""

    def __int__(self, x, y, bola):
        pygame.sprite.Sprite.__init__(self)

        self.x=x
        self.y=x
        self.bola=bola

    def movimiento_bola(self):
        if self.bola.y < self.bola.y >
