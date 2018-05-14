from Jugador import *
from Juego import *
import pygame,sys
from pygame.locals import *

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

ALTO=15                                          #Constantes de la matriz de la interfaz
ANCHO=15                                         #Constantes de la matriz de la interfaz
NEGRO = (0,0,0)                                  #Constantes de la matriz de la interfaz
BLANCO = (255,255,255)                           #Constantes de la matriz de la interfaz

Principal = True                                 #Inicia con el menu principal
FUENTE= pygame.font.Font(None,35)                #Crea variable con la fuente que se va utilizar
Imagen_titulo = pygame.image.load("Titulo.png")  #Crea la imagen para el titulo
AZUL= (16,94,205)                                #Color azul
grosor1=2
grosor2=2
grosor3=2

while True:                                                    #Bucle principal

    if Principal:                                              #Si el usuario esta en la pantalla principal
        ventana.fill(NEGRO)                                    #Rellena la pantalla para que dibuje sobre ella

        pygame.draw.rect(ventana,AZUL, [3,3,595,369], 15)      #Dibuja el marco
        ventana.blit(Imagen_titulo,(195,10))                   #Posiciona el titulo a la ventana

        #Botones------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana,AZUL,[160,150,265,30],grosor1)            #Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto1= FUENTE.render("Humano vs Humano",0,BLANCO)                 #Texto del boton
        pygame.draw.rect(ventana, AZUL, [135, 200, 310, 30], grosor2)      # Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto2 = FUENTE.render("Humano vs Computador", 0, BLANCO)          # Texto del boton
        pygame.draw.rect(ventana, AZUL, [250, 250, 85, 30], grosor3)       # Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto3 = FUENTE.render("Salir",0,BLANCO)                           # Texto del boton

        ventana.blit(Texto1,(175,153))                         #Coloca el texto en la ventana
        ventana.blit(Texto2,(150,203))                         #Coloca el texto en la ventana
        ventana.blit(Texto3, (265, 253))                       #Coloca el texto en la ventana

        #Se identifica si el mouse esta dentro de los margenes de los botones-----------------------------------------------

        x_mouse,y_mouse = pygame.mouse.get_pos()

        if 160 <=  x_mouse <= 425 and 150<=y_mouse<=180 :             #Cambia el grosor del boton1
            grosor1 = 0
        elif 135 <=  x_mouse <= 444 and 200<=y_mouse<=230 :           #Cambia el grosor del boton2
            grosor2 = 0
        elif 250 <=  x_mouse <= 335 and 250<=y_mouse<=280 :           #Cambia el grosor del boton3
            grosor3 = 0
        else:                                                         #Vuelve a la normalidad
            grosor1=2
            grosor2 = 2
            grosor3 = 2


        for event in pygame.event.get():                       #Eventos menu principal
            if event.type== QUIT:                              #Si se pulsa la "x"
               pygame.quit()
               sys.exit()


    else:                                              #Si no se esta sobre el menu principal, carga el campo de juegp
        for i in range(25):                            #Bucle que actualiza la matriz dependiendo de la matriz principal
            for j in range(40):
                color = NEGRO                          #El color prederteminado sera el negro
                if matriz_principal[i][j] == 1:        #Si hay un uno el cuadro será blanco
                   color=BLANCO
                pygame.draw.rect(ventana,color,[ALTO*j,ANCHO*i,ALTO,ANCHO],0)

        for event in pygame.event.get():          #Eventos
            if event.type== QUIT:                 #Si se pulsa la "x"
               pygame.quit()
               sys.exit()
            elif pygame.key.get_pressed()[K_UP]:
               matriz_principal=jugador2.moverse(matriz_principal,-1)
            elif pygame.key.get_pressed()[K_DOWN]:
               matriz_principal = jugador2.moverse(matriz_principal,1)



    pygame.display.update()                  #Actualiza la pantalla

