import pygame,sys
from pygame.locals import *
from Juego import *

pygame.init()                                #Inicializa python

ventana = pygame.display.set_mode((400,400)) #Tamaño de la ventana
pygame.display.set_caption("PONG")           #Titulo de la ventana
ventana.fill(pygame.Color(0,0,0))            #Color del fondo de la ventana(negro)

matriz_principal = juego.crear_matriz()      #Crea la matriz de control
ALTO=15
ANCHO=15
NEGRO = (0,0,0)
BLANCO = (255,255,255)

while True:                                  #Bucle principal

    for i in range(25):                      #Bucle que actualiza la matriz dependiendo de la matriz principal
        color=NEGRO
        for j in range(40):
            if matriz_principal[i][j] == 1: #Si hay un uno el cuadro será blanco
                color=BLANCO
            pygame.draw.rect(ventana,color,[ALTO*j,ANCHO*i,ALTO,ANCHO],0)




    for event in pygame.event.get():         #Eventos
        if event.type== QUIT:                     #Si se pulsa la "x"
            pygame.quit()
            sys.exit()

    pygame.display.update()                  #Actualiza la pantalla

