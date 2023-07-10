class conta():
    def __init__(self,agencia,conta,nome,fone,cpf):
        self.agencia=agencia
        self.conta=conta
        self.nome=nome
        self.fone=fone 
        self.cpf=cpf
        self.saldo=0
        
    def depositar(self,total):
        self.saldo+=total

    def sacar(self,total):
        self.saldo-=total
        
    def extrato(self):
        print(self.saldo)
    
        

