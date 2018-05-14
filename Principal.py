from Jugador import *
from Juego import *
import pygame,sys
from pygame.locals import *
from Bola import *

pygame.init()                                #Inicializa python
ANCHO_VENNTANA=600
LARGO_VENTANA=375
ventana = pygame.display.set_mode((ANCHO_VENNTANA,LARGO_VENTANA)) #Tamaño de la ventana
pygame.display.set_caption("PONG")           #Titulo de la ventana
ventana.fill(pygame.Color(0,0,0))            #Color del fondo de la ventana(negro)

juego=juego()
matriz_principal = juego.crear_matriz(25,40)      #Crea la matriz de control

jugador1 = Jugador(0,7,9,True)
jugador2 = Jugador(39,7,9,False)
matriz_principal = jugador1.dibujar_en_pantalla(matriz_principal)
matriz_principal = jugador2.dibujar_en_pantalla(matriz_principal)
bola=Rect(100,200,30,30)
ball= Bola()

ALTO=15                                          #Constantes de la matriz de la interfaz
ANCHO=15                                         #Constantes de la matriz de la interfaz
NEGRO = (0,0,0)                                  #Constantes de la matriz de la interfaz
AZUL= (16,94,205)
BLANCO = (255,255,255)                           #Constantes de la matriz de la interfaz

Principal = False                                  #Inicia con el menu principal
FUENTE= pygame.font.Font(None,35)                 #Crea variable con la fuente que se va utilizar
Imagen_titulo = pygame.image.load("Titulo.png")   #Crea la imagen para el titulo

pygame.key.set_repeat(1, 100) #Instruccion que arregla la fluidez de la teclas

while True:                                                    #Bucle principal

    if Principal:                                              #Si el usuario esta en la pantalla principal

        pygame.draw.rect(ventana,AZUL, [3,3,595,369], 15)      #Dibuja el marco
        ventana.blit(Imagen_titulo,(195,10))                   #Posiciona el titulo a la ventana

        #Botones------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana,AZUL,[160,150,265,30],2)            #Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto1= FUENTE.render("Humano vs Humano",0,BLANCO)           #Texto del boton
        pygame.draw.rect(ventana, AZUL, [135, 200, 310, 30], 2)      # Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto2 = FUENTE.render("Humano vs Computador", 0, BLANCO)    # Texto del boton
        pygame.draw.rect(ventana, AZUL, [250, 250, 85, 30], 2)
        Texto3 = FUENTE.render("Salir",0,BLANCO)

        ventana.blit(Texto1,(175,153))                         #Coloca el texto en la ventana
        ventana.blit(Texto2,(150,203))                         #Coloca el texto en la ventana
        ventana.blit(Texto3, (265, 253))                       #Coloca el texto en la ventana

        for event in pygame.event.get():                       #Eventos menu principal
            if event.type== QUIT:                              #Si se pulsa la "x"
               pygame.quit()
               sys.exit()

    else:
        for i in range(25):                      #Bucle que actualiza la matriz dependiendo de la matriz principal
            for j in range(40):
                color = NEGRO                          #El color prederteminado sera el negro
                if matriz_principal[i][j] == 1:           #Si hay un uno el cuadro será blanco
                   color=BLANCO
                pygame.draw.rect(ventana,color,[ALTO*j,ANCHO*i,ALTO,ANCHO],1)

        for event in pygame.event.get():          #Eventos
            if event.type== QUIT:                 #Si se pulsa la "x"
               pygame.quit()
               sys.exit()
            elif pygame.key.get_pressed()[K_UP]:
               matriz_principal=jugador2.moverse(matriz_principal,-1)
            elif pygame.key.get_pressed()[K_DOWN]:
               matriz_principal = jugador2.moverse(matriz_principal,1)

        ball.dibujar_bola(bola,ventana)
        ball.moverse_bola(bola, dx=2, dy=2)

    pygame.display.update()                  #Actualiza la pantalla

