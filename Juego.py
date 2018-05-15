class juego:
    n = 0
    m = 0
    matriz=[]

    def __init_(self,n,m,matriz):
        self.n=n
        self.m = m
        self.matriz=matriz

    def crear_matriz(self,n,m):
        for filas in range(n):
            self.matriz.append([])
            for columnas in range(m):
                if filas == 0 or filas ==24:
                    self.matriz[filas].append(1)
                else:
                    self.matriz[filas].append(0)
        return self.matriz



