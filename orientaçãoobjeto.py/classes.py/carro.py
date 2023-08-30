class carro():
    def __init__(self,modelo, marca):
        self.modelo = modelo
        self.marca = marca 
        
        
    def acelerar(self):
        print("Acelera")
        
    def freio (self):
        print("Freia")
    
    def passar_marcha(self,marcha):
        self.marcha = marcha     
        print(f"Passando Marcha para",marcha)
        
carro1 = carro("x6","bmw")
print(carro1.modelo)
print(carro1.marca)
carro1.acelerar()
carro1.freio()
carro1.passar_marcha(2)
carro2 = carro("x1","bmw")




    
        
        