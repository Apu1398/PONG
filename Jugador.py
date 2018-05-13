import pygame

WHITE = (0,0,0)

LARGO_VENTANA=800

class Jugador(pygame.sprite.Sprite):
    def __init__(self, x,y, tam_paleta, tipo_jugador, ventana):

        """Clase Jugador"""
        pygame.sprite.Sprite.__init__(self)

        "Atributos"

        self.tam_paleta=tam_paleta
        #self.cantidad_paleta=cantidad_paleta
        self.tipo_jugador=tipo_jugador
        #self.paleta= pygame.draw.line(ventana, WHITE, [0 + x, 25 + 15], [0 + x, 200 + 15], 15)
        self.x=x
        self.y=y
        self.ventana=ventana
        self.abajo=0
        self.arriba=LARGO_VENTANA

    def dibujar_en_pantalla(self):
        j1= pygame.Rect(self.x,self.y, 10, 200)
        pygame.draw.rect(self.ventana, WHITE, j1)

    def tipo_Jugador(self, tipo_jugador):
        "Metodo que elige si es jugador humano o AI"

        if tipo_jugador==True:
            self.movimiento_humano()
        else:
            self.movimiento_AI()

    def movimiento_humano(self):

        "Metodo que le da movimiento al humano"

        if self.dibujar_en_pantalla().bottom >=  LARGO_VENTANA:
            self.dibujar_en_pantalla().bottom = LARGO_VENTANA
        elif self.dibujar_en_pantalla().top <=0:
            self.dibujar_en_pantalla().top = 0

    def movimiento_AI(self):
        pass

