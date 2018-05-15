import pygame
from pygame.rect import Rect


class Bola:

    """Clase bola"""


    def __init__(self ,pos_x,pos_y,direccion):
        self.direccion = direccion
        self.pos_x = pos_x
        self.pos_y = pos_y

    def dibujar_bola(self,matriz):
        matriz[self.pos_x][self.pos_y]=1
        return matriz


    def moverse_bola(self, matriz):

        self.pos_y += self.direccion

        if self.pos_y == 40:
            print("Punto")
            matriz[self.pos_x][self.pos_y-1]=0
            self.pos_y=20
            self.direccion = -self.direccion


        elif matriz[self.pos_x][self.pos_y] == 1:
            self.direccion = -self.direccion
            self.pos_y += self.direccion
            matriz[self.pos_x][self.pos_y] = 1

        else:
            matriz[self.pos_x][(self.pos_y)-self.direccion] = 0
            matriz[self.pos_x][self.pos_y] = 1

        return matriz



        # (bola).move_ip(dx, dy)
        #
        # if (bola).y < 0 or (bola).y > 25:
        #     dy*=-1
        # if (bola).x < 0 or (bola).x > 40:
        #     dx*=-1


