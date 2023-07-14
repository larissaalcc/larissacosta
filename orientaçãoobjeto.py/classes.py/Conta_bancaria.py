class Conta_bancaria():
    def __init__(self,nome,cpf,senha):
        self.nome=nome
        self.__saldo=0.0
        self.__cpf=cpf
        self.__senha=senha

    def extrato(self,s):
        #self.__senha=s
        if s!=self.__senha:
            print("Senha inválida")
        else:
            print(self.__saldo)

    def depositar(self,x):
        self.__saldo=self.__saldo+x
        print("\nDepósito efetuado com suceso")
        print("Seu saldo agora é:",self.__saldo)


    def sacar(self,s):
        if s!=self.__senha:
            print("Senha inválida")
        else:
            s1=float(input("Quanto você deseja sacar: "))
            self.__saldo=self.__saldo-s1
            print("Seu saldo:",self.__saldo)




