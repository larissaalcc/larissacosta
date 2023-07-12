class Modelo_quadrado():

    def __init__(self,lado):
        self.lado=lado
        self.area=self.lado**2
        print("A área do quadrado é igual a:",self.area)


    def mudar_valor_lado(self,x):
        self.lado=x
        self.area=self.lado**2
        print("Valor dos lados alterado com sucesso")
        print("A área do quadrado é igual a:",self.area)

 
        

