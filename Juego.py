class juego:
    n = 25
    m = 40
    matriz=[]

    def __init_(self,n,m,matriz):
        self.n=n
        self.m=m
        self.matriz=matriz

    def crear_matriz(self):
        for filas in range(self.n):
            self.matriz.append([])
            for columnas in range(self.m):
                self.matriz[filas].append(0)
        return self.matriz

juego=juego()
m1=juego.crear_matriz()
print(m1)


