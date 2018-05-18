class Jugador():

    def __init__(self, x,y,tam_paleta,Humano,cantidad_paletas):
        self.x=x
        self.y=y
        self.tam_paleta = tam_paleta
        self.Humano = Humano
        self.cantidad_paletas = cantidad_paletas

    def dibujar_en_pantalla(self, matriz):
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

        if self.Humano:
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
                if self.y >= 1 and (self.y + self.tam_paleta) <= 24:
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
                    self.y-=1

        return matriz

    def get_posicion(self):           #Funcion que retorna la posicion del jugador divida
        tupla_pos = (self.y,self.y +(self.tam_paleta//3)), \
                    ((self.y +(self.tam_paleta//3),self.y+(self.tam_paleta//3)*2)),\
                    ((self.y + (self.tam_paleta // 3) * 2),self.y + (self.tam_paleta // 3) * 3)
        return tupla_pos
