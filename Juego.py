class juego:
    """Clases encargada de la generacion de la matriz a utilizar para desarrollar el juego"""
    n = 0
    m = 0
    matriz=[]

    def __init_(self,n,m,matriz):
        self.n=n #se pide la cantidad n
        self.m = m #se pide la cantidad m
        self.matriz=matriz #variable para crear matriz

    def crear_matriz(self,n,m):
        #E:recibe el n y el m
        #S:Generar matriz
        #R:No presenta
        """Metodo que crea matriz  de 25x40"""

        for filas in range(n):
            self.matriz.append([])
            for columnas in range(m):
                if filas == 0 or filas ==24:
                    self.matriz[filas].append(1)
                else:
                    self.matriz[filas].append(0)
        return self.matriz