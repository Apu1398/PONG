import pygame

WHITE = (0,0,0)

LARGO_VENTANA=800

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x,y, tam_paleta, Humano):

        """Clase Jugador"""
        pygame.sprite.Sprite.__init__(self)

        "Atributos"

        self.tam_paleta=tam_paleta
        self.Humano =Humano
        self.x=x
        self.y=y

    def dibujar_en_pantalla(self, matriz):
        for i in range(self.y, self.y+self.tam_paleta):
            matriz[i][self.x]=1
        return matriz

    def moverse(self,matriz,direccion):
        self.y+=direccion                                           #Direccion de movimiento

        if self.y >= 0 and (self.y + self.tam_paleta) <=25:
            for i in range(0,25):                               #Iteracion que limpia la parte de la pantalla del juagdor
             matriz[i][self.x] = 0
            for i in range(self.y,self.y + self.tam_paleta):    #Pone en 1 la nueva posicion de la paleta
               matriz[i][self.x]=1
        else:
            self.y-=direccion

        #return matriz
