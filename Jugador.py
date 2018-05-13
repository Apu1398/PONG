import pygame

WHITE = (0,0,0)

LARGO_VENTANA=800

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x,y,tam_paleta,Humano):

        """Clase Jugador"""
        pygame.sprite.Sprite.__init__(self)

        "Atributos"

        self.tam_paleta=tam_paleta
        self.Humano=Humano
        self.x=x
        self.y=y

    def dibujar_en_pantalla(self,matriz):
        for i in range(self.y,self.y+self.tam_paleta):
            matriz[i][self.x]=1
        return matriz

    def moverse(self,matriz,direccion):
        self.y+=direccion                                           #Direccion de movimiento
        if self.y >= 0:
            for i in range(0,24):                               #Iteracion que limpia la parte de la pantalla del juagdor
             matriz[i][self.x] = 0
            for i in range(self.y,self.y + self.tam_paleta):    #Pone en 1 la nueva posicion de la paleta
               matriz[i][self.x]=1
        else:
            self.y=0

        return matriz


    # def tipo_Jugador(self, tipo_jugador):
    #     "Metodo que elige si es jugador humano o AI"
    #
    #     if tipo_jugador==True:
    #         self.movimiento_humano()
    #     else:
    #         self.movimiento_AI()

    ##IMPORTANTE:
    # Lo comento porque creo que con solo poner self.tipo_de_jugador en cualquier metodo ya se que tipo de jugador es

    # def movimiento_humano(self):
    #
    #     "Metodo que le da movimiento al humano"
    #
    #     if self.dibujar_en_pantalla().bottom >=  LARGO_VENTANA:
    #         self.dibujar_en_pantalla().bottom = LARGO_VENTANA
    #     elif self.dibujar_en_pantalla().top <=0:
    #         self.dibujar_en_pantalla().top = 0
    #
    # def movimiento_AI(self):
    #     pass

