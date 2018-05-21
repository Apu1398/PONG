class Jugador:
    """Clase que genera el objeto jugador con sus funcionalidades como lo son: dibujarse en pantalla,
        moverse y obtener posicion actual de jugador"""
    def __init__(self, x,y,tam_paleta,humano,cantidad_paletas):
        self.x=x                                 #da la posicion en x
        self.y=y                                 #da la posicion en y
        self.tam_paleta = tam_paleta             #da el taamno de la paleta
        self.humano = humano                     #comprueba si es humano o no
        self.cantidad_paletas = cantidad_paletas #da la cantidad de paletas a utilizar para jugar

    def dibujar_en_pantalla(self, matriz):
        #E: matriz
        #S: dibuja en la matriz la paleta
        #R: No presenta
        """Metodo encargado de dibujar en la matriz los jugadores"""
        if self.cantidad_paletas == 1:                         #Si la cantidad de paletas es 1
            for i in range(self.y, self.y+self.tam_paleta):
                matriz[i][self.x] = 1
        else:
            for i in range (self.y, self.y + self.tam_paleta): #Si la cantidad de paletas es 2
                matriz[i][self.x] = 1
            for i in range (self.y + self.tam_paleta + 2, (self.y + self.tam_paleta + 2) + self.tam_paleta):  #Establece los margenes para la segunda paleta
                matriz[i][self.x] = 1
        return matriz

    def moverse(self,matriz,direccion,pos_x_bola,direccion_bola):
        #E: matriz, direccion,pos_x_bola, direccion_bola
        #S: generacion de movimiento de los jugadores
        #R: No presenta
        """Metodo que que le movilidad al jugador, verifica los limites
           en donde se puede mover los jugadores"""

        if self.humano:
            self.y+=direccion                                           #Direccion de movimiento

            if self.cantidad_paletas == 1:
                if self.y >= 1 and (self.y + self.tam_paleta) <=24:
                    for i in range(1,24):                               #Iteracion que limpia la parte de la pantalla del juagdor
                        matriz[i][self.x] = 0
                    for i in range(self.y,self.y + self.tam_paleta):    #Pone en 1 la nueva posicion de la paleta
                        matriz[i][self.x]=1
                else:
                    self.y-=direccion
            else:
                if self.y >= 1 and (self.y + self.tam_paleta + 2 + self.tam_paleta ) <=24:
                    for i in range(1,24):                                                      #Limpia la parte del juagdor
                        matriz[i][self.x] = 0
                    for i in range(self.y,self.y + self.tam_paleta):
                        matriz[i][self.x]=1
                    for i in range(self.y + self.tam_paleta + 2, self.y + self.tam_paleta + 2 + self.tam_paleta):
                        matriz[i][self.x] = 1
                else:
                    self.y-=direccion
        else:
            if direccion_bola != -1:
                diferencia = self.y - pos_x_bola
                if self.cantidad_paletas == 1:
                    if self.y >= 1 and (self.y + self.tam_paleta) < 24:
                        for i in range(1, 24):  # Iteracion que limpia la parte de la pantalla del juagdor1
                            matriz[i][self.x] = 0
                        if diferencia < 0 :
                            self.y += 1
                            for i in range(self.y,self.y + self.tam_paleta):
                               matriz[i][self.x] = 1
                        elif diferencia > 0:
                            self.y -= 1
                            for i in range(self.y, self.y + self.tam_paleta):
                                matriz[i][self.x] = 1
                        elif diferencia == 0:
                            for i in range(self.y, self.y + self.tam_paleta):
                                matriz[i][self.x] = 1
                    else:
                        self.y -= 1
                else:

                    if self.y >= 1 and (self.y + self.tam_paleta + 2 + self.tam_paleta) < 24:
                        for i in range(1, 24):  # Iteracion que limpia la parte de la pantalla del juagdor1
                            matriz[i][self.x] = 0
                        if diferencia < 0 :
                            self.y += 1
                            for i in range(self.y,self.y + self.tam_paleta):
                               matriz[i][self.x] = 1
                            for i in range (self.y + self.tam_paleta + 2 ,self.y + self.tam_paleta + 2 + self.tam_paleta):
                                matriz[i][self.x] = 1
                        elif diferencia > 0:
                            self.y -= 1
                            for i in range(self.y,self.y + self.tam_paleta):
                               matriz[i][self.x] = 1
                            for i in range (self.y + self.tam_paleta + 2 ,self.y + self.tam_paleta + 2 + self.tam_paleta):
                                matriz[i][self.x] = 1
                        elif diferencia == 0:
                            for i in range(self.y,self.y + self.tam_paleta):
                               matriz[i][self.x] = 1
                            for i in range (self.y + self.tam_paleta + 2 ,self.y + self.tam_paleta + 2 + self.tam_paleta):
                                matriz[i][self.x] = 1
                    else:
                        self.y -= 2


        return matriz

    def get_posicion(self):
        #E: No presenta
        #S: obtencion de las posiones de jugador
        #R: No presenta
        """Metodo que retorna la posicion del jugador dividida"""
        tupla_pos = (self.y,self.y +(self.tam_paleta//3)), \
                    ((self.y +(self.tam_paleta//3),self.y+(self.tam_paleta//3)*2)),\
                    ((self.y + (self.tam_paleta // 3) * 2),self.y + (self.tam_paleta // 3) * 3)

        tupla_pos2 = (self.y+11,self.y+11 +(self.tam_paleta//3)), \
                    ((self.y+11 +(self.tam_paleta//3),self.y+11+(self.tam_paleta//3)*2)),\
                    ((self.y+11 + (self.tam_paleta // 3) * 2),self.y +11 + (self.tam_paleta // 3) * 3)


        return tupla_pos,tupla_pos2
