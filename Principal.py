from Jugador import *
from Juego import *
import pygame,sys
from pygame.locals import *
from Bola import *

pygame.init()                                #Inicializa python
ANCHO_VENNTANA = 600
LARGO_VENTANA = 375
ventana = pygame.display.set_mode((ANCHO_VENNTANA,LARGO_VENTANA)) #Tamaño de la ventana
pygame.display.set_caption("PONG")                                #Titulo de la ventana
ventana.fill(pygame.Color(0,0,0))                                 #Color del fondo de la ventana(negro)
pygame.key.set_repeat(1, 50)                                     #Instruccion que arregla la fluidez de la teclas

juego = juego()                                                   #Llama a la clase juego
matriz_principal = juego.crear_matriz(25,40)                      #Crea la matriz de control
BALL = Bola(13,20,-1,1)


ALTO = 15                                          #Constantes de la matriz de la interfaz
ANCHO = 15                                         #Constantes de la matriz de la interfaz
NEGRO = (0,0,0)                                    #Constantes de la matriz de la interfaz
AZUL = (16,94,205)                                 #Constantes de la matriz de la interfaz
BLANCO = (255,255,255)                             #Constantes de la matriz de la interfaz

Principal_1 = True                               #Inicia con el menu principal
Principal_2 = False                              #Indica cuando se va a utilizar la pantalla de escoger paletas

FUENTE= pygame.font.Font(None,35)                #Crea variable con la fuente que se va utilizar
Imagen_titulo = pygame.image.load("Titulo.png")  #Crea la imagen para el titulo
sonido = pygame.mixer.Sound("menu_over.wav")     #Carga sonido para cuando el mouse se posicione sobre un boton
AZUL = (16,94,205)                               #Color azul
grosor1=2                                        #Tamaño del grosor utilizado para cuando el mosue se posiciona sobre un boton
grosor2=2                                        #Tamaño del grosor utilizado para cuando el mosue se posiciona sobre un boton
grosor3=2                                        #Tamaño del grosor utilizado para cuando el mosue se posiciona sobre un boton
reloj = pygame.time.Clock()                       #Varia la velocidad del juego

while True:                                                    #Bucle principal

    if Principal_1:                                              #Si el usuario esta en la pantalla principal
        ventana.fill(NEGRO)

        pygame.draw.rect(ventana,AZUL, [3,3,595,369], 15)      #Dibuja el marco
        ventana.blit(Imagen_titulo,(195,10))                   #Posiciona el titulo a la ventana

        #Botones------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana,AZUL,[160,150,265,30],grosor1)                #Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto1= FUENTE.render("Humano vs Humano",0,BLANCO)                     #Texto del boton
        pygame.draw.rect(ventana, AZUL, [135, 200, 310, 30], grosor2)          # Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto2 = FUENTE.render("Humano vs Computador", 0, BLANCO)              # Texto del boton
        pygame.draw.rect(ventana, AZUL, [250, 250, 85, 30], grosor3)
        Texto3 = FUENTE.render("Salir",0,BLANCO)

        ventana.blit(Texto1,(175,153))                         #Coloca el texto en la ventana
        ventana.blit(Texto2,(150,203))                         #Coloca el texto en la ventana
        ventana.blit(Texto3, (265, 253))                       #Coloca el texto en la ventana

        #Se identifica si el mouse esta dentro de los margenes de los botones-----------------------------------------------
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if 160 <= x_mouse <= 425 and 150 <= y_mouse <= 180:    # Cambia el grosor boton 1
            grosor1 = 0
        elif 135 <= x_mouse <= 444 and 200 <= y_mouse <= 230:  # Cambia el grosor boton 2
            grosor2 = 0
        elif 250 <= x_mouse <= 335 and 250 <= y_mouse <= 280:  # Cambia el grosor del boton Salir
            grosor3 = 0
        else:
            grosor1 = 2                                        # Vuelve a la normalidad el grosor
            grosor2 = 2                                        # Vuelve a la normalidad el grosor
            grosor3 = 2                                        # Vuelve a la normalidad el grosor

        #Eventos de la pantalla principal-----------------------------------------------------------------------------------

        for event in pygame.event.get():                       #Eventos menu principal
            if event.type== QUIT:                              #Si se pulsa la "x"
               pygame.quit()
               sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if 160 <=  x_mouse <= 425 and 150<=y_mouse<=180 :      #Si se pulsa el boton humano vs humano
                    sonido.play()                                      #Reproduce un sonido
                    grosor1 = 2                                        #Vuelve el grosor a la noramalidad
                    Principal_1=False                                  #Se pasa a la segunda pantalla
                    Principal_2 = True                                 #Se pasa a la segunda pantalla
                    cantidad_jugadores=2                               #Define la cantidad de jugadores

                elif 135 <= x_mouse <= 444 and 200 <= y_mouse <= 230:  #Si se pulsa el boton humano vs computadora
                    sonido.play()                                      #reproduce un sonido
                    grosor2 = 2                                        #Vuelve el grosor a la normalidad
                    Principal_1 = False                                #Pasa a la segunda pantalla
                    Principal_2 = True                                 #Pasa a la segunda pantalla
                    cantidad_jugadores = 1                             #Define la cantidad de jugadores

                elif 250 <= x_mouse <= 335 and 250 <= y_mouse <= 280:  #Se pulsa el boton Salir
                    sonido.play()                                      #Reproduce sonido
                    grosor3 = 2                                        #Vuelve el grosor a la normalidad
                    pygame.quit()                                      #Se sale del juego
                    sys.exit()                                         #Termina la aplicacion

    elif Principal_2:
        ventana.fill(NEGRO)                                    #Pone la pantalla en negro

        pygame.draw.rect(ventana, AZUL, [3, 3, 595, 369], 15)  # Dibuja el marco
        ventana.blit(Imagen_titulo, (195, 10))                 # Posiciona el titulo a la ventana

        # Botones------------------------------------------------------------------------------------------------------
        pygame.draw.rect(ventana, AZUL, [200, 150, 180, 30],grosor1)       # Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto1 = FUENTE.render("Una paleta", 0, BLANCO)                    # Texto del boton
        pygame.draw.rect(ventana, AZUL, [200, 200, 180, 30], grosor2)      # Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto2 = FUENTE.render("Dos paletas", 0, BLANCO)                   # Texto del boton
        pygame.draw.rect(ventana, AZUL, [235, 250, 100, 30],grosor3)       # Dibuja boton, lo cuadra segun el rectangulo ya creado
        Texto3 = FUENTE.render("Volver", 0, BLANCO)                        # Texto del boton

        ventana.blit(Texto1, (225, 153))  # Coloca el texto en la ventana
        ventana.blit(Texto2, (225, 203))  # Coloca el texto en la ventana
        ventana.blit(Texto3, (250, 253))  # Coloca el texto en la ventana


        x_mouse,y_mouse = pygame.mouse.get_pos()

        # Se identifica si el mouse esta dentro de los margenes de los botones-----------------------------------------------
        x_mouse, y_mouse = pygame.mouse.get_pos()
        if 200 <= x_mouse <= 380 and  150<= y_mouse <= 180:               #Cambia el grosor boton 1
            grosor1 = 0
        elif 200 <= x_mouse <= 390 and 200 <= y_mouse <= 230:             #Cambia el grosor boton 2
            grosor2 = 0
        elif 235 <= x_mouse <= 335 and 250 <= y_mouse <= 280:             #Cambia el grosor del boton Salir
            grosor3 = 0
        else:
            grosor1 = 2                                                   #Vuelve a la noramlidad el grosor
            grosor2 = 2                                                   #Vuelve a la normalidad el grosor
            grosor3 = 2                                                   #Vuelve a la normalidad el grosor

        for event in pygame.event.get():                       #Eventos menu principal_2
            if event.type== QUIT:                              #Si se pulsa la "x"
               pygame.quit()
               sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if 200 <=  x_mouse <= 380 and 150<=y_mouse<=180:            #Clic sobre el boton una paleta
                    sonido.play()                                           #Reproduce un sonido
                    Principal_2=False                                       #Deshabilita el menu principal dos
                    ventana.fill(NEGRO)                                     #Pinta la pantalla de negro (Para dibujar sobre ella)
                    grosor1 = 2                                             #Regresa el grosor a la normalidad

                    if cantidad_jugadores==1:                               #Verifica cual fue la seleccion del usuario
                        jugador1 = Jugador(0,7,3,True,1)                    #Crea jugador 1
                        jugador2 = Jugador(39,7,3,False,1)                  #Crea jugador 2
                        matriz_principal = jugador1.dibujar_en_pantalla(matriz_principal)  #Dibuja el juagdor 1
                        matriz_principal = jugador2.dibujar_en_pantalla(matriz_principal)  #Dibuja el jugador 2
                    elif cantidad_jugadores == 2:                                          # Verifica cual fue la seleccion del usuario
                        jugador1 = Jugador(0, 7, 3, True, 1)                               # Crea jugador 1
                        jugador2 = Jugador(39, 7, 3, True, 1)                              # Crea jugador 2
                        matriz_principal = jugador1.dibujar_en_pantalla(matriz_principal)  # Dibuja el juagdor 1
                        matriz_principal = jugador2.dibujar_en_pantalla(matriz_principal)  # Dibuja el jugador 2

                elif 200<= x_mouse <= 380 and 200 <= y_mouse <= 230:        #Clic sobre el boton dos paletas
                    sonido.play()
                    Principal_2 = False
                    ventana.fill(NEGRO)
                    grosor2 = 2

                    if cantidad_jugadores == 1:
                        jugador1 = Jugador(0,2,3,True,2)                                   #Crea al jugador 1 con dos paletas
                        jugador2 = Jugador(39,2,3,False,2)                                 #Crea al jugador 2 con dos paletas
                        matriz_principal = jugador1.dibujar_en_pantalla(matriz_principal)  # Dibuja el juagdor 1
                        matriz_principal = jugador2.dibujar_en_pantalla(matriz_principal)  # Dibuja el jugador 2

                    elif cantidad_jugadores == 2:                                          # Verifica cual fue la seleccion del usuario
                        jugador1 = Jugador(0, 2, 9, True, 2)                               # Crea jugador 1
                        jugador2 = Jugador(39, 2, 9, True, 2)                              # Crea jugador 2
                        matriz_principal = jugador1.dibujar_en_pantalla(matriz_principal)  # Dibuja el juagdor 1
                        matriz_principal = jugador2.dibujar_en_pantalla(matriz_principal)  # Dibuja el jugador 2

                elif 235 <= x_mouse <= 335 and 250 <= y_mouse <= 280:       #Clic sobre el boton volver
                    sonido.play()
                    grosor3 = 2
                    Principal_2 = False
                    Principal_1 = True


    else:                                              #Si no se esta sobre el menu principal, carga el campo de juego

         tupla_jugador1 = jugador1.get_posicion()                            #Obtiene las sublistas de cada jugador, dependiendo de la posicion
         tupla_jugador2 = jugador2.get_posicion()                            #Obtiene las sublistas de cada jugador, dependiendo de la posicion
         BALL.dibujar_bola(matriz_principal)
         BALL.moverse_bola(matriz_principal,tupla_jugador1,tupla_jugador2)   #Mueve la bola, necesita los argumentos para determinar su comportamiento

         for i in range(25):                            #Bucle que actualiza la matriz dependiendo de la matriz principal
             for j in range(40):
                 color = NEGRO                          #El color prederteminado sera el negro
                 if matriz_principal[i][j] == 1:        #Si hay un uno el cuadro será blanco
                    color= AZUL
                 pygame.draw.rect(ventana,color,[ALTO*j,ANCHO*i,ALTO,ANCHO],0) #Dibuja cada cuadro

         for event in pygame.event.get():          #Eventos
             if event.type== QUIT:                 #Si se pulsa la "x"
               pygame.quit()
               sys.exit()
             elif pygame.key.get_pressed()[K_w]:      #Si se pulsa la w
                jugador1.moverse(matriz_principal,-1,0,0)
             elif pygame.key.get_pressed()[K_s]:      #Si se pulsa la s
                jugador1.moverse(matriz_principal,1,0,0)
             elif pygame.key.get_pressed()[K_UP]:          #Si se pulsa la flecha arriba
                 if cantidad_jugadores == 2:               #Si los jugadores son dos humanos
                     jugador2.moverse(matriz_principal,-1,0,0) #Permite que el segundo jugador se mueva
             elif pygame.key.get_pressed()[K_DOWN]:        #Si se pulsa la flecha abajo
                 if cantidad_jugadores == 2:               #Si los jugadores son dos humanos
                     jugador2.moverse(matriz_principal,1,0,0)  #Permite que el segundo jugador se mueva para abajo

         if BALL.pos_y > 20 and BALL.pos_y <38:
             jugador2.moverse(matriz_principal,0,BALL.pos_x,BALL.direccion_columnas)

         tiempo = reloj.tick(1)                           #Varia la velocidad del juego



    pygame.display.update()                  #Actualiza la pantalla

