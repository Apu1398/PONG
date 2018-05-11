import pygame,sys
from pygame.locals import *
from Juego import *

pygame.init()                                #Inicializa python

ventana = pygame.display.set_mode((400,400)) #Tamaño de la ventana
pygame.display.set_caption("PONG")           #Titulo de la ventana
ventana.fill(pygame.Color(0,0,0))            #Color del fondo de la ventana(negro)

matriz_principal = juego.crear_matriz()

while True:                                  #Bucle principal

    for event in pygame.event.get():         #Eventos
        if event.type== QUIT:                     #Si se pulsa la "x"
            pygame.quit()
            sys.exit()

    pygame.display.update()                  #Actualiza la pantalla

