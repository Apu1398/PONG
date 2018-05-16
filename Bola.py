class Bola:

    """Clase bola"""


    def __init__(self ,pos_x,pos_y,direccion_columnas,direccion_filas):
        self.direccion_columnas = direccion_columnas
        self.direccion_filas = direccion_filas
        self.pos_x = pos_x
        self.pos_y = pos_y

    def dibujar_bola(self,matriz):
        matriz[self.pos_x][self.pos_y]=1
        return matriz


    def moverse_bola(self, matriz,tupla1, tupla2):

        self.pos_y += self.direccion_columnas                  #Siempre le suma o le resta a la posicion y que tenga actualamente
        self.pos_x += self.direccion_filas

        if self.pos_y == 40:                          #Si la posicion es 40 la puntuacion cambia
            print("Punto")
            matriz[self.pos_x][self.pos_y-1]=0        #Pone en 0 la posicion en la que estaba la bola...
            self.pos_y=20                             #Para luego ponerla en el medio
            self.direccion_columnas = -self.direccion_columnas          #La bola iría en direccion contraria

        elif self.pos_y == -1:                        #Si la posicion es -1 uno la puntuacion cambia
            print("Punto")
            matriz[self.pos_x][self.pos_y+1]=0        #Pone en 0 la posicion en la que estaba la bola...
            self.pos_y=20                             #Para luego ponerla en el medio
            self.direccion_columnas = -self.direccion_columnas          #La bola iría en direccion contraria

        elif matriz[self.pos_x][self.pos_y] == 1:     #Si la siguiente posicion es 1 la bola "Rebota"

            if self.pos_x in range(tupla1[0][0],tupla1[0][1]) and self.pos_y == 0:
                self.direccion_filas = -1
                self.direccion_columnas = 1
                self.pos_x += self.direccion_filas
                self.pos_y += self.direccion_columnas
                for i in range(1,24):
                    matriz[i][1]=0

            elif self.pos_x in range(tupla1[1][0],tupla1[1][1]) and self.pos_y == 0:
                self.direccion_filas = 0
                self.direccion_columnas = 1
                self.pos_x += self.direccion_filas
                self.pos_y += self.direccion_columnas
                for i in range(1,24):
                    matriz[i][1]=0
            elif self.pos_x in range(tupla1[2][0],tupla1[2][1]) and self.pos_y == 0:
                self.direccion_filas = 1
                self.direccion_columnas = 1
                self.pos_x += self.direccion_filas
                self.pos_y += self.direccion_columnas
                for i in range(1,24):
                    matriz[i][1]=0
            elif self.pos_x in range(tupla2[0][0],tupla2[0][1]) and self.pos_y == 39:
                self.direccion_filas = -1
                self.direccion_columnas = -1
                self.pos_x += self.direccion_filas
                self.pos_y += self.direccion_columnas
                for i in range(1, 24):
                    matriz[i][38] = 0
            elif self.pos_x in range(tupla2[1][0],tupla2[1][1]) and self.pos_y == 39:
                self.direccion_filas = 0
                self.direccion_columnas = -1
                self.pos_x += self.direccion_filas
                self.pos_y += self.direccion_columnas
                for i in range(1, 24):
                    matriz[i][38] = 0
            elif self.pos_x in range(tupla2[2][0],tupla2[2][1]) and self.pos_y == 39:
                self.direccion_filas = 1
                self.direccion_columnas = -1
                self.pos_x += self.direccion_filas
                self.pos_y += self.direccion_columnas
                for i in range(1, 24):
                    matriz[i][38] = 0
            elif self.pos_x == 0 or self.pos_x == 24:
                self.direccion_filas = -self.direccion_filas
                self.pos_x += self.direccion_filas
                matriz[self.pos_x][(self.pos_y) - self.direccion_columnas] = 0

        else:
            matriz[self.pos_x-self.direccion_filas][(self.pos_y)-self.direccion_columnas] = 0  #Primero "apaga el cuadrante anterior"
            matriz[self.pos_x][self.pos_y] = 1                   #"Enciende el siguiente cuadrante

        return matriz                                            #Retorna la matriz
