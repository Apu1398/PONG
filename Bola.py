class Bola:

    """Clase bola"""


    def __init__(self ,pos_x,pos_y,direccion):
        self.direccion = direccion
        self.pos_x = pos_x
        self.pos_y = pos_y

    def dibujar_bola(self,matriz):
        matriz[self.pos_x][self.pos_y]=1
        return matriz


    def moverse_bola(self, matriz,tupla1, tupla2):

        self.pos_y += self.direccion                  #Siempre le suma o le resta a la posicion y que tenga actualamente

        if self.pos_y == 40:                          #Si la posicion es 40 la puntuacion cambia
            print("Punto")
            matriz[self.pos_x][self.pos_y-1]=0        #Pone en 0 la posicion en la que estaba la bola...
            self.pos_y=20                             #Para luego ponerla en el medio
            self.direccion = -self.direccion          #La bola iría en direccion contraria

        elif self.pos_y == -1:                        #Si la posicion es -1 uno la puntuacion cambia
            print("Punto")
            matriz[self.pos_x][self.pos_y+1]=0        #Pone en 0 la posicion en la que estaba la bola...
            self.pos_y=20                             #Para luego ponerla en el medio
            self.direccion = -self.direccion          #La bola iría en direccion contraria

        elif matriz[self.pos_x][self.pos_y] == 1:     #Si la siguiente posicion es 1 la bola "Rebota"

            if self.pos_x in range(tupla1[0][0],tupla1[0][1]) and self.pos_y == 0:
                print("Pego en la primera parte")
            elif self.pos_x in range(tupla1[1][0],tupla1[1][1]) and self.pos_y == 0:
                print ("Pego en la segunda parte")
            elif self.pos_x in range(tupla1[2][0],tupla1[2][1]) and self.pos_y == 0:
                print("Pego en la tercer parte")
            elif self.pos_x in range(tupla2[0][0],tupla2[0][1]) and self.pos_y == 39:
                print("Pego en la primera parte 2")
            elif self.pos_x in range(tupla2[1][0],tupla2[1][1]) and self.pos_y == 39:
                print ("Pego en la segunda parte 3")
            elif self.pos_x in range(tupla2[2][0],tupla2[2][1]) and self.pos_y == 39:
                print("Pego en la tercer parte 3")


            self.direccion = -self.direccion          #Por eso se le cambia la dirección
            self.pos_y += self.direccion              #Se aumenta o disminuye la posicion en y
            matriz[self.pos_x][self.pos_y] = 1        #La bola se mueve para el lado contrario

        else:                                                    #Si no, la bola se sigue moviendo
            matriz[self.pos_x][(self.pos_y)-self.direccion] = 0  #Primero "apaga el cuadrante anterior"
            matriz[self.pos_x][self.pos_y] = 1                   #"Enciende el siguiente cuadrante

        return matriz                                            #Retorna la matriz
