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

    def moverse(self,matriz,direccion):

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
            print("Me traté de mover")

        return matriz

    def get_posicion(self):           #Funcion que retorna la posicion del jugador divida
        tupla_pos = (self.y,self.y +(self.tam_paleta//3)), \
                    ((self.y +(self.tam_paleta//3),self.y+(self.tam_paleta//3)*2)),\
                    ((self.y + (self.tam_paleta // 3) * 2),self.y + (self.tam_paleta // 3) * 3)
        return tupla_pos




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

