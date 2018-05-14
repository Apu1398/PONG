import pygame

class Bola(pygame.sprite.Sprite):

    """Clase bola"""

    def __int__(self, bola, ancho, largo):
        pygame.sprite.Sprite.__init__(self)

        self.rect=bola
        self.rect.centerx=ancho/2
        self.rect.centery=largo/2
        self.speed =[3,3]

    def actualiza(self):
        if self.rect.left<0 or self.rect.right > ancho:
            pass
