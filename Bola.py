import pygame
from pygame.rect import Rect


class Bola:

    """Clase bola"""


    def __init__(self ,pos_x,pos_y,direccion):
        self.direccion = direccion
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.velocidad=[3,3]

    def dibujar_bola(self,matriz):
        matriz[self.pos_x][self.pos_y]=1
        return matriz


    def moverse_bola(self, matriz,tupla):

        self.pos_y += self.direccion                  #Siempre le suma o le resta a la posicion y que tenga actualamente

        if self.pos_y == 40:                          #Si la posicion es 40 la puntuacion cambia
            print("Punto")
            self.speed[0]= -self.velocidad[0]
            matriz[self.pos_x][self.pos_y-1]=0        #Pone en 0 la posicion en la que estaba la bola...
            self.pos_y=20                             #Para luego ponerla en el medio
            self.direccion = -self.direccion          #La bola iría en direccion contraria

        elif self.pos_y == -1:                        #Si la posicion es -1 uno la puntuacion cambia
            print("Punto")
            matriz[self.pos_x][self.pos_y+1]=0        #Pone en 0 la posicion en la que estaba la bola...
            self.pos_y=20                             #Para luego ponerla en el medio
            self.direccion = -self.direccion          #La bola iría en direccion contraria

        elif matriz[self.pos_x][self.pos_y] == 1:     #Si la siguiente posicion es 1 la bola "Rebota"

            if self.pos_x in range(tupla[0][0],tupla[0][1]) and self.pos_y == 0:
                print("Pego en la primera parte")
            elif self.pos_x in range(tupla[1][0],tupla[1][1]) and self.pos_y == 0:
                print ("Pego en la segunda parte")
            elif self.pos_x in range(tupla[2][0],tupla[2][1]) and self.pos_y == 0:
                print("Pego en la tercer parte")

            self.direccion = -self.direccion          #Por eso se le cambia la dirección
            self.pos_y += self.direccion              #Se aumenta o disminuye la posicion en y
            matriz[self.pos_x][self.pos_y] = 1        #La bola se mueve para el lado contrario

        else:                                                    #Si no, la bola se sigue moviendo
            matriz[self.pos_x][(self.pos_y)-self.direccion] = 0  #Primero "apaga el cuadrante anterior"
            matriz[self.pos_x][self.pos_y] = 1                   #"Enciende el siguiente cuadrante

        return matriz                                            #Retorna la matriz   m