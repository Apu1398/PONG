from Jugador import *
from Juego import *
import pygame,sys
from pygame.locals import *

pygame.init()                                #Inicializa python
ANCHO_VENNTANA=800
LARGO_VENTANA=600
ventana = pygame.display.set_mode((ANCHO_VENNTANA,LARGO_VENTANA)) #Tamaño de la ventana
pygame.display.set_caption("PONG")           #Titulo de la ventana
ventana.fill(pygame.Color(0,0,0))            #Color del fondo de la ventana(negro)

juego=juego()
matriz_principal = juego.crear_matriz(25,40)      #Crea la matriz de control
#5matriz_principal
jugador_humano1= Jugador(40, 20, 200,True, ventana )

ALTO=15                                          #Constantes de la matriz de la interfaz
ANCHO=15                                         #Constantes de la matriz de la interfaz
NEGRO = (0,0,0)                                  #Constantes de la matriz de la interfaz
BLANCO = (255,255,255)                           #Constantes de la matriz de la interfaz

while True:                                  #Bucle principal

    for i in range(25):                      #Bucle que actualiza la matriz dependiendo de la matriz principal

        for j in range(40):
            color = NEGRO                             #El color prederteminado sera el negro
            if matriz_principal[i][j] == 1:           #Si hay un uno el cuadro será blanco
                color=BLANCO
            pygame.draw.rect(ventana,color,[ALTO*j,ANCHO*i,ALTO,ANCHO],0)




    for event in pygame.event.get():          #Eventos
        if event.type== QUIT:                 #Si se pulsa la "x"
            pygame.quit()
            sys.exit()
        elif event.type ==MOUSEBUTTONDOWN:      #Prueba con el mosueclick
            matriz_principal[1][0] = 1

    pygame.display.update()                  #Actualiza la pantalla

