class Modelo_bola():
    
    
    def __init__(self,cor2,tamanho,material):
        self.cor=cor2
        self.tamanho=tamanho
        self.material=material

    def trocar_cor(self,x,y,z):
        self.cor=x
        self.tamanho=y
        self.material=z
        print("\nModelagem alterada com sucesso!")

    def mostrar_cor(self):
        print(self.cor,self.tamanho,self.material)
