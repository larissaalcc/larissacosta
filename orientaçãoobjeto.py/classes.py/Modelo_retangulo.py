class Modelo_retangulo():

    def __init__(self,base,altura):
        self.ladoA=base
        self.ladoB=altura

    def mudar_valor_dos_lados(self,a,b):
        self.ladoA=a
        self.ladoB=b
        print("Valores alterados com sucesso!")
        print("Novos valores:",a,"e",b)

    def calcular_area_e_perimetro(self,perimetro):
        self.area=self.ladoA*self.ladoB
        self.perimetro=self.ladoA**2+self.ladoB**2
        print( "Valor da área:",self.area)
        print("Valor do perímetro:",self,perimetro)


    



